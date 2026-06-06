---
name: tech-doc-writer
description: "Technical documentation: API docs, README files, changelogs, architecture decision records (ADR), and onboarding guides. 技术文档写作：API 文档、README、Changelog、架构决策记录和新人指南。Triggers: write documentation, API docs, README, changelog, 写文档, 技术文档, ADR, architecture decision, 新人指南, onboarding guide, 更新 README"
---

# Tech Doc Writer

编写清晰、结构化、可维护的技术文档。

## 文档类型

### README

```markdown
# Project Name
一句话描述

## Quick Start（5 分钟能用）
## 为什么做这个项目
## 安装
## 使用示例
## API 参考
## 架构概览
## 贡献指南
## 许可证
```

规则：
- Quick Start 必须在 README 前半屏内
- 每个代码示例可独立运行
- 不要写 "顾名思义" — 每个概念都要解释

### API 文档

```markdown
## POST /api/v1/users

创建用户。

### Request
\`\`\`json
{ "name": "string (required)", "email": "string (required)" }
\`\`\`

### Response 201
\`\`\`json
{ "code": 0, "data": { "id": "uuid" } }
\`\`\`

### Errors
| Code | Message |
|------|---------|
| 40001 | name is required |
| 40901 | email already exists |
```

规则：
- 每个端点单独一节
- 必须有 Request/Response 示例
- 枚举所有可能的错误码
- 注明哪些参数是 required

### Changelog

```markdown
## [1.2.0] - 2026-06-06

### Added
- 新功能 A
- 新功能 B

### Changed
- 优化了 X 的性能

### Fixed
- 修复了 Y 场景下的崩溃

### Deprecated
- Z 方法将在 2.0 废弃
```

严格遵循 [Keep a Changelog](https://keepachangelog.com/) 格式，按语义化版本排序。

### ADR（架构决策记录）

```markdown
# ADR-001: 选择 PostgreSQL 作为主数据库

## 状态
已采纳

## 背景
需要在关系型数据库中选择一个...

## 决策
选择 PostgreSQL 16

## 备选方案
- MySQL 8.0 — 因窗口函数支持较弱而排除
- SQLite — 因并发写入限制而排除

## 影响
- 运维需要 PostgreSQL 相关技能
- 可利用 JSONB 减少 NoSQL 依赖
```

## 通用原则

1. **先写最重要的信息**（倒金字塔结构）
2. **一个段落只讲一件事**
3. **代码示例必须能跑**
4. **用主动语态**（"点击按钮"不是"按钮被点击"）
5. **术语首次出现时定义**
6. **超过 3 层的嵌套列表重新组织**
