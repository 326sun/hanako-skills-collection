#!/usr/bin/env python3
"""
scan_experience.py — 读取经验日志，按维度聚类。

输入: experience/experience_log.jsonl, experience/error_log.jsonl
输出: stdout (JSON) — 聚类结果
"""

import json
import sys
from pathlib import Path
from collections import defaultdict
from datetime import datetime, timedelta

BASE_DIR = Path(__file__).resolve().parent.parent
EXPERIENCE_LOG = BASE_DIR / "experience" / "experience_log.jsonl"
ERROR_LOG = BASE_DIR / "experience" / "error_log.jsonl"
LOOKBACK_DAYS = 30


def load_jsonl(path: Path) -> list[dict]:
    """加载 JSONL 文件，跳过空行和无效行。"""
    records = []
    if not path.exists():
        return records
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def filter_recent(records: list[dict], days: int) -> list[dict]:
    """过滤最近 N 天内的记录。"""
    cutoff = datetime.now() - timedelta(days=days)
    recent = []
    for r in records:
        try:
            d = datetime.strptime(r.get("date", ""), "%Y-%m-%d")
            if d >= cutoff:
                recent.append(r)
        except (ValueError, TypeError):
            recent.append(r)  # 无法解析日期的保留
    return recent


def cluster_by_error_type(errors: list[dict]) -> list[dict]:
    """按 error_type 聚类错误日志。"""
    groups = defaultdict(list)
    for e in errors:
        key = e.get("error_type", "unspecified")
        groups[key].append(e)
    
    clusters = []
    for error_type, items in groups.items():
        # 聚合统计
        task_types = list(set(i.get("task_type", "") for i in items))
        severities = [i.get("severity", 1) for i in items]
        avg_severity = sum(severities) / len(severities) if severities else 0
        is_mechanical = any(i.get("is_mechanical", False) for i in items)
        is_contextual = any(i.get("is_contextual", False) for i in items)
        candidate_skills = list(set(
            i.get("candidate_skill", "") for i in items if i.get("candidate_skill")
        ))
        corrections = [i for i in items if i.get("user_correction")]
        
        clusters.append({
            "cluster_key": f"error:{error_type}",
            "cluster_type": "error",
            "error_type": error_type,
            "repeat_count": len(items),
            "explicit_correction_count": len(corrections),
            "task_types": task_types,
            "avg_severity": round(avg_severity, 1),
            "is_mechanical": is_mechanical,
            "is_contextual": is_contextual,
            "candidate_skills": candidate_skills,
            "sample_ids": [i.get("task_id", "") for i in items[:5]],
        })
    return clusters


def cluster_by_suggested_skill(experiences: list[dict], errors: list[dict]) -> list[dict]:
    """按 suggested_skill 聚类（来自 experience_log）。"""
    all_records = experiences + errors
    groups = defaultdict(list)
    
    for r in all_records:
        skill = r.get("suggested_skill") or r.get("candidate_skill")
        if skill:
            groups[skill].append(r)
    
    clusters = []
    for skill, items in groups.items():
        task_types = list(set(i.get("task_type", "") for i in items))
        corrections = [i for i in items if i.get("user_correction") or i.get("user_explicit_correction")]
        
        clusters.append({
            "cluster_key": f"skill:{skill}",
            "cluster_type": "suggested_skill",
            "suggested_skill": skill,
            "repeat_count": len(items),
            "explicit_correction_count": len(corrections),
            "task_types": task_types,
            "sample_ids": [i.get("task_id", "") for i in items[:5]],
        })
    return clusters


def cluster_by_task_type(experiences: list[dict]) -> list[dict]:
    """按 task_type 聚类，检测同一类型中反复出现的问题。"""
    groups = defaultdict(list)
    for e in experiences:
        key = e.get("task_type", "general")
        groups[key].append(e)
    
    clusters = []
    for task_type, items in groups.items():
        # 在该类型中，检测 result_status 分布
        statuses = defaultdict(int)
        for i in items:
            statuses[i.get("result_status", "success")] += 1
        
        # 检测同一类型中是否有高频 skill_candidate 标记
        skill_candidates = [i for i in items if i.get("skill_candidate")]
        
        clusters.append({
            "cluster_key": f"task_type:{task_type}",
            "cluster_type": "task_type",
            "task_type": task_type,
            "total_count": len(items),
            "status_distribution": dict(statuses),
            "skill_candidate_count": len(skill_candidates),
            "sample_ids": [i.get("task_id", "") for i in items[:5]],
        })
    return clusters


def main():
    experiences = load_jsonl(EXPERIENCE_LOG)
    errors = load_jsonl(ERROR_LOG)
    
    # 过滤最近的数据
    experiences = filter_recent(experiences, LOOKBACK_DAYS)
    errors = filter_recent(errors, LOOKBACK_DAYS)
    
    # 聚类
    clusters = []
    if errors:
        clusters.extend(cluster_by_error_type(errors))
    clusters.extend(cluster_by_suggested_skill(experiences, errors))
    clusters.extend(cluster_by_task_type(experiences))
    
    result = {
        "scan_date": datetime.now().strftime("%Y-%m-%d"),
        "lookback_days": LOOKBACK_DAYS,
        "total_experiences": len(experiences),
        "total_errors": len(errors),
        "total_clusters": len(clusters),
        "clusters": clusters,
    }
    
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
