#!/usr/bin/env python3
"""
score_patterns.py — 对聚类结果计算 pattern_score。

输入: stdin (JSON) — scan_experience.py 的输出
输出: stdout (JSON) — 带评分的 pattern 列表

公式:
  pattern_score =
      2 × repeat_count
    + 3 × explicit_correction_count
    + 2 × tool_complexity
    + 3 × impact_level
    + 3 × preference_signal
    + 2 × mechanical_score
    - 3 × contextual_score
    - 2 × one_off_flag
    - 2 × risk_level
"""

import json
import sys


def estimate_tool_complexity(cluster: dict) -> int:
    """根据任务类型估算工具调用复杂度 (1-5)。"""
    task_types = cluster.get("task_types", [])
    complexity_map = {
        "coding": 4,
        "document_processing": 3,
        "file_management": 2,
        "image_processing": 3,
        "research": 3,
        "planning": 2,
        "system_operation": 4,
        "communication": 2,
        "general": 2,
    }
    scores = [complexity_map.get(t, 2) for t in task_types]
    return max(scores) if scores else 2


def estimate_impact_level(cluster: dict) -> int:
    """估算影响等级 (1-5)。"""
    # 错误类型聚类：用 avg_severity
    if cluster.get("cluster_type") == "error":
        severity = cluster.get("avg_severity", 1)
        return min(5, max(1, int(severity)))
    # suggested_skill 聚类：如果被多次标记为 skill_candidate，影响高
    if cluster.get("cluster_type") == "suggested_skill":
        return min(5, max(1, cluster.get("repeat_count", 1)))
    # task_type 聚类：看非成功比例
    if cluster.get("cluster_type") == "task_type":
        dist = cluster.get("status_distribution", {})
        total = cluster.get("total_count", 1) or 1
        non_success = dist.get("failed", 0) + dist.get("corrected", 0) + dist.get("partial", 0)
        ratio = non_success / total
        if ratio > 0.5:
            return 5
        elif ratio > 0.3:
            return 4
        elif ratio > 0.1:
            return 2
        return 1
    return 1


def estimate_risk_level(cluster: dict) -> int:
    """估算自动化风险 (1-5)。"""
    task_types = cluster.get("task_types", [])
    high_risk_types = {"system_operation", "file_management"}
    medium_risk_types = {"coding", "image_processing"}
    
    risk = 1
    for t in task_types:
        if t in high_risk_types:
            risk = max(risk, 4)
        elif t in medium_risk_types:
            risk = max(risk, 3)
        elif t == "document_processing":
            risk = max(risk, 2)
    return risk


def score_cluster(cluster: dict) -> dict:
    """对单个聚类计算 pattern_score。"""
    
    repeat_count = cluster.get("repeat_count", 0)
    explicit_correction_count = cluster.get("explicit_correction_count", 0)
    tool_complexity = estimate_tool_complexity(cluster)
    impact_level = estimate_impact_level(cluster)
    
    # preference_signal: 从 corrections 数量估算
    preference_signal = 1 if explicit_correction_count >= 1 else 0
    
    # mechanical / contextual
    is_mechanical = cluster.get("is_mechanical", False)
    is_contextual = cluster.get("is_contextual", False)
    mechanical_score = 2 if is_mechanical else (0 if is_contextual else 1)
    contextual_score = 2 if is_contextual else 0
    
    # one_off: 如果 repeat_count <= 1，标记为一次性
    one_off_flag = 1 if repeat_count <= 1 else 0
    
    risk_level = estimate_risk_level(cluster)
    
    score = (
        2 * repeat_count
        + 3 * explicit_correction_count
        + 2 * tool_complexity
        + 3 * impact_level
        + 3 * preference_signal
        + 2 * mechanical_score
        - 3 * contextual_score
        - 2 * one_off_flag
        - 2 * risk_level
    )
    
    # 确定处理方式
    if score < 5:
        action = "只记录"
    elif score < 8:
        action = "进入 weekly_pattern_report"
    elif score < 12:
        action = "生成 skill_candidate 记录 + reason.md"
    elif score < 16:
        action = "生成 proposal（不生成完整 skill）"
    else:
        action = "生成完整 SKILL.draft.md + 测试样例"
    
    return {
        **cluster,
        "pattern_score": score,
        "score_breakdown": {
            "repeat_count": repeat_count,
            "explicit_correction_count": explicit_correction_count,
            "tool_complexity": tool_complexity,
            "impact_level": impact_level,
            "preference_signal": preference_signal,
            "mechanical_score": mechanical_score,
            "contextual_score": contextual_score,
            "one_off_flag": one_off_flag,
            "risk_level": risk_level,
        },
        "recommended_action": action,
    }


def main():
    scan_result = json.load(sys.stdin)
    clusters = scan_result.get("clusters", [])
    
    scored = [score_cluster(c) for c in clusters]
    # 按 pattern_score 降序排列
    scored.sort(key=lambda x: x["pattern_score"], reverse=True)
    
    result = {
        "score_date": scan_result.get("scan_date", ""),
        "total_clusters": len(scored),
        "scored_patterns": scored,
    }
    
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
