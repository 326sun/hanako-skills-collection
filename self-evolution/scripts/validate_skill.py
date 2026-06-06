#!/usr/bin/env python3
"""
validate_skill.py — 验证 skill 草案是否通过测试集。

输入: 命令行参数 — skill 目录路径
输出: stdout — 验证结果

Phase 2 建立测试集后启用。当前为壳。
"""

import sys
from pathlib import Path


def main():
    print("[壳] validate_skill.py — Phase 2 建立测试集后启用。")
    
    if len(sys.argv) < 2:
        print("用法: python validate_skill.py <proposal_dir>")
        print("当前只验证目录结构是否存在。")
        return
    
    proposal_dir = Path(sys.argv[1])
    required_files = [
        "SKILL.draft.md",
        "reason.md",
        "validation_plan.md",
        "validation_checklist.md",
        "test_cases.md",
    ]
    
    missing = [f for f in required_files if not (proposal_dir / f).exists()]
    
    if missing:
        print(f"[不通过] 缺少文件: {', '.join(missing)}")
    else:
        print("[结构检查通过] 所有必需文件存在。")
        print("完整验证需 Phase 2 测试集。")


if __name__ == "__main__":
    main()
