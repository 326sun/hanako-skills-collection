---
name: git-workflow
description: "Standardized git commit messages, branch naming, PR descriptions, and common git operations. 规范化 git 提交信息、分支命名、PR 描述和常用操作。Triggers: commit, git commit, 提交, merge, rebase, pull request, PR, branch name, 分支名, git log, changelog, 提交信息怎么写"
---

# Git Workflow

提供规范的 git 操作指导和自动化建议。

## Commit Message 规范

使用 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Type
| Type | 说明 |
|------|------|
| feat | 新功能 |
| fix | bug 修复 |
| docs | 文档变更 |
| style | 格式（不影响代码逻辑） |
| refactor | 重构 |
| perf | 性能优化 |
| test | 测试 |
| chore | 构建/工具 |
| ci | CI/CD |

### 规则
- Subject 用祈使语气（"add" 不是 "added"）
- Subject 不超过 50 字符
- Body 每行不超过 72 字符
- Body 解释 what 和 why，不是 how
- 关联 issue 用 `Closes #123` 或 `Refs #123`

## 分支命名

```
<type>/<short-description>

例：feat/user-login, fix/password-validation, refactor/auth-module
```

## PR 描述模板

```markdown
## 做了什么
简要描述变更

## 为什么要做
背景和动机

## 怎么测试
- 步骤 1
- 步骤 2

## 风险评估
- [ ] 兼容性检查
- [ ] 性能影响
- [ ] 文档更新
```

## 常用操作

| 场景 | 命令 |
|------|------|
| 撤销最近一次 commit（保留修改） | `git reset --soft HEAD~1` |
| 修改最近一次 commit 信息 | `git commit --amend` |
| 将当前分支 rebase 到 main | `git rebase main` |
| 交互式压缩最近 3 个 commit | `git rebase -i HEAD~3` |
| 暂存当前修改 | `git stash` |
| 恢复暂存 | `git stash pop` |
| 查看某个文件的修改历史 | `git log -p -- <file>` |
