#!/usr/bin/env python3
"""
update_registry.py — 更新 skill_registry.json 和 skill_history.md。

输入: 命令行参数 — skill 名称 + 新状态
输出: 更新 registry/skill_registry.json 和 registry/skill_history.md

所有 skill 状态变更必须通过此脚本。当前为壳。
"""

import json
import sys
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent
REGISTRY_FILE = BASE_DIR / "registry" / "skill_registry.json"
HISTORY_FILE = BASE_DIR / "registry" / "skill_history.md"


def main():
    print("[壳] update_registry.py — 有待注册的 skill 时启用。")
    
    if len(sys.argv) < 3:
        print("用法: python update_registry.py <skill_name> <status>")
        print("状态: candidate | testing | stable | review | disabled")
        return
    
    skill_name = sys.argv[1]
    new_status = sys.argv[2]
    valid_statuses = {"candidate", "testing", "stable", "review", "disabled"}
    
    if new_status not in valid_statuses:
        print(f"[错误] 无效状态: {new_status}，有效值: {valid_statuses}", file=sys.stderr)
        sys.exit(1)
    
    # 加载现有注册表
    registry = {"skills": []}
    if REGISTRY_FILE.exists():
        with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
            registry = json.load(f)
    
    # 查找或创建 skill 条目
    found = False
    for skill in registry.get("skills", []):
        if skill.get("skill_name") == skill_name:
            old_status = skill.get("status", "unknown")
            skill["status"] = new_status
            skill["last_updated"] = datetime.now().strftime("%Y-%m-%d")
            found = True
            print(f"[OK] {skill_name}: {old_status} → {new_status}")
            break
    
    if not found:
        registry.setdefault("skills", []).append({
            "skill_name": skill_name,
            "status": new_status,
            "version": "0.1.0",
            "created_at": datetime.now().strftime("%Y-%m-%d"),
            "last_updated": datetime.now().strftime("%Y-%m-%d"),
        })
        print(f"[OK] {skill_name} 已注册，状态: {new_status}")
    
    # 写回
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, ensure_ascii=False, indent=2)
    
    # 追加历史记录
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n- {datetime.now().strftime('%Y-%m-%d')} | {skill_name} | → {new_status}\n")


if __name__ == "__main__":
    main()
