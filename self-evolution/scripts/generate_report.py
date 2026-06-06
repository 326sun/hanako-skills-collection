#!/usr/bin/env python3
"""
generate_report.py — 根据评分结果生成周报和候选报告。

输入: stdin (JSON) — score_patterns.py 的输出
输出: 写入 reports/weekly_pattern_report.md 和 reports/skill_candidates.md
"""

import json
import sys
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
REPORTS_DIR = BASE_DIR / "reports"
WEEKLY_REPORT = REPORTS_DIR / "weekly_pattern_report.md"
CANDIDATES_REPORT = REPORTS_DIR / "skill_candidates.md"


def generate_weekly_report(scored_data: dict) -> str:
    """生成周报 Markdown。"""
    patterns = scored_data.get("scored_patterns", [])
    score_date = scored_data.get("score_date", datetime.now().strftime("%Y-%m-%d"))
    
    # 统计
    total = len(patterns)
    high_freq = [p for p in patterns if p["pattern_score"] >= 5]
    high_risk = [p for p in patterns if p.get("score_breakdown", {}).get("risk_level", 0) >= 4]
    candidates = [p for p in patterns if p["pattern_score"] >= 8]
    not_recommended = [p for p in patterns if p["pattern_score"] < 5]
    
    lines = [
        "# Hanako 自我进化周报",
        "",
        f"> 自动生成于 {score_date}",
        "",
        "---",
        "",
        "## 1. 本周任务概览",
        "",
        f"- 总聚类数：{total}",
        f"- 高频模式（score >= 5）：{len(high_freq)}",
        f"- 候选 skill（score >= 8）：{len(candidates)}",
        f"- 高风险模式：{len(high_risk)}",
        "",
    ]
    
    # 高频模式
    lines.extend([
        "## 2. 高频模式",
        "",
        "| pattern | 聚类键 | pattern_score | 重复次数 | 是否机械重复 | 建议动作 |",
        "|---|---:|---:|---|---|",
    ])
    for p in high_freq:
        key = p.get("cluster_key", "unknown")
        score = p.get("pattern_score", 0)
        repeat = p.get("repeat_count", 0)
        mechanical = "是" if p.get("is_mechanical") else "否"
        action = p.get("recommended_action", "")
        lines.append(f"| {key} | {score} | {repeat} | {mechanical} | {action} |")
    
    lines.append("")
    
    # 高风险模式
    lines.extend([
        "## 3. 高风险模式",
        "",
    ])
    if high_risk:
        for p in high_risk:
            key = p.get("cluster_key", "unknown")
            risk = p.get("score_breakdown", {}).get("risk_level", "?")
            lines.append(f"- **{key}**：风险等级 {risk}/5")
    else:
        lines.append("本周未检测到高风险模式。")
    
    lines.append("")
    
    # skill 候选
    lines.extend([
        "## 4. skill 候选",
        "",
        "| skill_name | pattern_score | 状态 | 建议动作 |",
        "|---|---:|---|---|",
    ])
    for p in candidates:
        name = p.get("suggested_skill") or p.get("cluster_key", "unknown")
        score = p.get("pattern_score", 0)
        status = "candidate"
        action = p.get("recommended_action", "")
        lines.append(f"| {name} | {score} | {status} | {action} |")
    
    lines.append("")
    
    # 不建议 skill 化
    lines.extend([
        "## 5. 本周不建议 skill 化的内容",
        "",
    ])
    if not_recommended:
        for p in not_recommended:
            key = p.get("cluster_key", "unknown")
            score = p.get("pattern_score", 0)
            reason = "一次性" if p.get("repeat_count", 0) <= 1 else "分值不足"
            lines.append(f"- {key}（score={score}）：{reason}")
    else:
        lines.append("无。")
    
    lines.append("")
    
    # 下周建议
    lines.extend([
        "## 6. 下周建议",
        "",
    ])
    if candidates:
        top = candidates[:3]
        for i, p in enumerate(top, 1):
            lines.append(f"{i}. 对「{p.get('cluster_key', '')}」生成详细 proposal")
    else:
        lines.append("继续积累经验日志，等待模式出现。")
    
    return "\n".join(lines)


def generate_candidates_report(scored_data: dict) -> str:
    """生成 skill 候选报告 Markdown。"""
    patterns = scored_data.get("scored_patterns", [])
    candidates = [p for p in patterns if p["pattern_score"] >= 8]
    score_date = scored_data.get("score_date", datetime.now().strftime("%Y-%m-%d"))
    
    lines = [
        "# Skill 候选列表",
        "",
        f"> 自动生成于 {score_date}",
        f"> pattern_score >= 8 的候选：{len(candidates)} 个",
        "",
        "---",
        "",
    ]
    
    for i, p in enumerate(candidates, 1):
        breakdown = p.get("score_breakdown", {})
        lines.extend([
            f"## 候选 {i}：{p.get('cluster_key', 'unknown')}",
            "",
            f"- **pattern_score**：{p.get('pattern_score', 0)}",
            f"- **重复次数**：{p.get('repeat_count', 0)}",
            f"- **用户纠正次数**：{p.get('explicit_correction_count', 0)}",
            f"- **任务类型**：{', '.join(p.get('task_types', []))}",
            f"- **是否机械重复**：{'是' if p.get('is_mechanical') else '否'}",
            f"- **建议动作**：{p.get('recommended_action', '')}",
            "",
            "### 评分明细",
            "",
            f"| 变量 | 值 |",
            f"|---|---|",
        ])
        for var, val in breakdown.items():
            lines.append(f"| {var} | {val} |")
        
        lines.extend([
            "",
            "### 样本任务 ID",
            "",
        ])
        for sid in p.get("sample_ids", [])[:5]:
            lines.append(f"- {sid}")
        
        lines.extend(["", "---", ""])
    
    return "\n".join(lines)


def main():
    scored_data = json.load(sys.stdin)
    
    # 生成周报
    weekly = generate_weekly_report(scored_data)
    with open(WEEKLY_REPORT, "w", encoding="utf-8") as f:
        f.write(weekly)
    print(f"[OK] 周报已写入 {WEEKLY_REPORT}")
    
    # 生成候选报告
    candidates = generate_candidates_report(scored_data)
    with open(CANDIDATES_REPORT, "w", encoding="utf-8") as f:
        f.write(candidates)
    print(f"[OK] 候选报告已写入 {CANDIDATES_REPORT}")


if __name__ == "__main__":
    main()
