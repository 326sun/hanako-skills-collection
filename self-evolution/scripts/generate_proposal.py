#!/usr/bin/env python3
"""
generate_proposal.py — 根据高分 pattern 生成 skill proposal。

输入: stdin (JSON) — 单个 pattern 的数据
输出: 在 proposals/<skill-name>/ 下创建 SKILL.draft.md, reason.md, validation_plan.md 等

Phase 3 之前不启用。当前为壳。
"""

import json
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PROPOSALS_DIR = BASE_DIR / "proposals"


def main():
    print("[壳] generate_proposal.py — Phase 3 之前不执行实际生成。")
    print("当前只验证输入格式。")
    
    try:
        data = json.load(sys.stdin)
        cluster_key = data.get("cluster_key", "unknown")
        score = data.get("pattern_score", 0)
        print(f"  pattern: {cluster_key}, score: {score}")
        if score >= 16:
            print(f"  [条件满足] 可生成完整 SKILL.draft.md")
        elif score >= 8:
            print(f"  [条件满足] 可生成 reason.md")
        else:
            print(f"  [条件不满足] score < 8，不生成 proposal")
    except json.JSONDecodeError:
        print("  [错误] 输入不是有效 JSON", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
