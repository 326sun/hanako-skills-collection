# Hanako 自我进化系统

> 让 Hanako 把重复错误、重复流程和用户长期偏好，转化为可验证、可审核、可回滚的工作规则。

## 当前阶段：Phase 1（仅检测与报告）

**不自动安装 skill，不自动修改已有 skill。**

---

## 目录结构

```
Hanako_Self_Evolution/
├── experience/          # 经验日志
│   ├── experience_log.jsonl   # 每次复杂任务后记录
│   ├── error_log.jsonl        # 错误和纠正记录
│   ├── corrections.md         # 用户明确偏好
│   └── preference_log.md      # 隐式偏好记录
├── reports/             # 自动生成报告
│   ├── weekly_pattern_report.md
│   ├── skill_candidates.md
│   ├── risk_report.md
│   └── evolution_metrics.md
├── proposals/           # skill 候选草案（Phase 3）
├── test_sets/           # 验证测试集（Phase 2）
│   ├── general/
│   ├── document_processing/
│   ├── coding/
│   ├── file_management/
│   ├── research/
│   └── planning/
├── registry/            # skill 注册表
│   ├── skill_registry.json
│   └── skill_history.md
├── scripts/             # 自动化脚本
│   ├── scan_experience.py    # Phase 1：读取日志、聚类
│   ├── score_patterns.py     # Phase 1：计算 pattern_score
│   ├── generate_report.py    # Phase 1：生成周报
│   ├── generate_proposal.py  # Phase 3：生成 skill 草案（壳）
│   ├── validate_skill.py     # Phase 2：验证 skill（壳）
│   └── update_registry.py    # 更新注册表（壳，基础功能可用）
└── README.md
```

---

## 如何记录经验

### experience_log.jsonl

每次复杂任务结束后，追加一条 JSON 记录：

```json
{
  "date": "2026-06-06",
  "task_id": "task_20260606_001",
  "task_type": "document_processing",
  "project": "general",
  "user_intent": "用户要求处理 Word 文档排版",
  "task_summary": "调整了三级标题样式和表格宽度",
  "tools_used": ["read", "write", "bash"],
  "tool_call_count": 3,
  "result_status": "success",
  "user_feedback": "accepted",
  "user_explicit_correction": false,
  "error_type": "none",
  "failure_point": "none",
  "correction": "none",
  "impact_level": 1,
  "repeatability": "medium",
  "one_off": false,
  "skill_candidate": false,
  "suggested_skill": null,
  "notes": ""
}
```

### error_log.jsonl

当任务出现失败或用户纠正时，记录：

```json
{
  "date": "2026-06-06",
  "task_id": "task_20260606_001",
  "task_type": "coding",
  "error_type": "missing_backup",
  "error_description": "修改文件前没有创建备份",
  "root_cause_guess": "缺少固定安全流程",
  "user_correction": "以后修改前必须备份",
  "fix_applied": "已补充备份步骤",
  "repeat_count_estimate": 2,
  "severity": 4,
  "is_mechanical": true,
  "is_contextual": false,
  "candidate_skill": "safe-file-editing-protocol"
}
```

### corrections.md

当用户说"以后都这样做""后续统一按这个格式""不要再这样"等高信号语句时，追加记录。

---

## 如何运行扫描

```bash
# 一条管道完成扫描→评分→生成报告
python scripts/scan_experience.py | python scripts/score_patterns.py | python scripts/generate_report.py

# 或者分步执行，查看中间结果：
python scripts/scan_experience.py > /tmp/scan.json
python scripts/score_patterns.py < /tmp/scan.json > /tmp/scored.json
python scripts/generate_report.py < /tmp/scored.json
```

---

## 如何查看周报

周报自动生成在 `reports/weekly_pattern_report.md`。

包含：
- 本周任务概览
- 高频模式列表
- 高风险模式
- skill 候选及建议动作
- 不建议 skill 化的内容

---

## 如何判断 skill candidate

pattern_score 分级：

| pattern_score | 处理方式 |
|---|---:|
| < 5 | 只记录 |
| 5–7 | 进入周报 |
| 8–11 | 生成 skill_candidate 记录 + reason.md |
| 12–15 | 生成 proposal（不生成完整 skill） |
| ≥ 16 | 生成完整 SKILL.draft.md + 测试样例 |

公式：

```
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
```

---

## 如何进入 testing

1. pattern_score >= 16
2. 生成完整 proposal（SKILL.draft.md + reason.md + validation_plan.md + test_cases.md）
3. 通过测试集验证
4. 用户审核通过
5. `python scripts/update_registry.py <skill_name> testing`

---

## 如何回滚或禁用 skill

```bash
# 禁用
python scripts/update_registry.py <skill_name> disabled

# 回退到 review 状态
python scripts/update_registry.py <skill_name> review
```

注意：`update_registry.py` 只更新注册表状态，不会自动删除或修改 skill 文件。手动删除/禁用 skill 需要在 Hanako skills 目录中操作。

---

## 安全规则

所有操作必须遵守：

1. 不覆盖原始文件
2. 不删除用户文件
3. 不自动安装 skill（Phase 1-2）
4. 不自动修改已有 stable skill
5. 不处理账号、密码、token、密钥
6. 不跨出用户指定工作区
7. 修改类任务必须保留备份或 diff

---

## 停止条件

出现以下情况，暂停自我进化，只保留日志：

- 连续 2 周没有高价值 pattern
- 生成的 proposal 大多无法通过测试
- 用户审核耗时超过节省时间
- skill 上线后错误率没有下降
- skill 之间出现频繁冲突
- 排查 Hanako 行为的时间明显增加
- 判断上下文型任务占主导

---

## 版本

v0.1 — Phase 1 就绪
