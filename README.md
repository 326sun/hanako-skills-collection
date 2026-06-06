# Hanako Skills Collection

为 [Hanako](https://github.com/liliMozi/openhanako) 精选的 32 个 skills，覆盖学术写作、数据处理、
文档操作、深度推理、开发工具与安全，外加一套自我进化管道。

```
hanako-skills-collection
├── skills/              ← 32 个即装即用 skills
├── self-evolution/      ← Phase 1 进化管道（日志→模式→候选→审核）
└── install.ps1          ← 一键安装
```

## 与 Hanako 生态的关系

```
┌─────────────────────────────────────────────┐
│ Hanako 核心（Pi 框架）                        │
│ 工具调用 · 会话管理 · 插件系统 · EventBus       │
├─────────────────────────────────────────────┤
│                                             │
│  hanako-skills-collection  ← 这个仓库        │
│  ┌─────────────┐  ┌──────────────────────┐  │
│  │ 19 个 skills │  │ self-evolution 管道   │  │
│  │ 文本指令      │  │ 日志→模式→候选→审核   │  │
│  └─────────────┘  └──────────────────────┘  │
│                                             │
│  hanako-ui-beautify       ← 插件             │
│  ┌─────────────────────┐                    │
│  │ 鸿蒙黑体 + 动效补丁   │                    │
│  │ 可执行代码（full-access）│                 │
│  └─────────────────────┘                    │
│                                             │
│  hanako-runtime-learner   ← 插件             │
│  ┌─────────────────────┐                    │
│  │ Phase 2 运行时学习    │                    │
│  │ 观察→检测→注入→审核   │                    │
│  └─────────────────────┘                    │
└─────────────────────────────────────────────┘
```

Skills 是文本指令，教 Hanako 在特定场景下怎么做；插件是可执行代码，
扩展 Hanako 的运行时能力。两者互补：skills 定义行为标准，
runtime-learner 让 skills 在使用中被动态优化。

## 快速开始

```powershell
git clone https://github.com/326sun/hanako-skills-collection.git
cd hanako-skills-collection
.\install.ps1
```

重启 Hanako 生效。只想装某几个？手动复制对应文件夹到 `~\.hanako\skills\`。

## Skills 目录

### 学术写作

| Skill | 做什么 |
|-------|--------|
| `academic-suite` | 三合一审稿：导师反馈 + 同行评审 + 格式检查 |
| `scientific-writing` | 英文学术写作规范，时态、hedging、术语一致性 |
| `thesis-docx` | 学位论文 Word 排版，样式规范化 |
| `literature-review` | 系统文献检索与综述，可复现检索策略 |
| `journal-figures` | Nature 风格配图设计（机制图、图形摘要、TOC 图） |
| `data-visualization` | matplotlib/seaborn 出版级图表，600 dpi SVG |

### 数据处理

| Skill | 做什么 |
|-------|--------|
| `data-analysis` | pandas/numpy/scipy 仿真数据处理 |

### 文档操作

| Skill | 做什么 |
|-------|--------|
| `office-documents` | Word/Excel/PPT/PDF 读写 |

### 推理增强

| Skill | 做什么 |
|-------|--------|
| `adaptive-reasoning` | 自动判断复杂度，简单不废话，复杂深思考 |
| `quiet-musing` | 五阶段深度推理：理解 → 拆解 → 多路径 → 执行 → 验证 |

### 开发与工具

| Skill | 做什么 |
|-------|--------|
| `skill-creator` | 创建和修改 skills，带评测和自动迭代 |
| `mcp-builder` | MCP 服务器构建，Python + Node.js 双栈 |
| `hana-plugin-creator` | Hana 插件脚手架和 SDK 模板 |
| `code-reviewer` | 代码审查：安全漏洞、性能、架构、最佳实践 |
| `git-workflow` | 规范化 commit message、分支命名、PR 描述 |
| `test-generator` | 自动生成单元测试、边界测试、集成测试 |
| `api-designer` | RESTful API 设计，OpenAPI 规范，错误码体系 |
| `docker-deploy` | Dockerfile 最佳实践、Compose 编排、安全加固 |
| `database-design` | SQL 查询优化、表结构设计、索引策略、迁移管理 |
| `shell-scripting` | Shell/PowerShell 脚本规范，跨平台兼容，幂等性 |
| `regex-builder` | 正则表达式构造、解释和测试用例生成 |
| `security-audit` | 依赖漏洞、硬编码密钥、OWASP Top 10、配置加固 |

### 写作与翻译

| Skill | 做什么 |
|-------|--------|
| `translator` | 中英互译，学术级术语一致性和语域匹配 |
| `tech-doc-writer` | API 文档、README、Changelog、ADR 架构决策记录 |

### 办公效率

| Skill | 做什么 |
|-------|--------|
| `presentation-builder` | 从主题生成演示文稿大纲、幻灯片内容和演讲备注 |
| `browser-automation` | 浏览器工具使用指南：填表、截图、数据提取、反检测 |

### 图表与创作

| Skill | 做什么 |
|-------|--------|
| `mermaid-diagrams` | 自然语言 → 流程图/时序图/架构图 SVG/PNG |
| `algorithmic-art` | p5.js 算法艺术生成 |
| `canvas-design` | Canvas 设计，30+ 开源字体 |

### 效率

| Skill | 做什么 |
|-------|--------|
| `article-extractor` | URL → 干净正文，去广告去导航 |
| `self-improving-agent` | 错误记录与经验积累，跨 session 改进 |

### 帮助

| Skill | 做什么 |
|-------|--------|
| `user-guide` | Hanako 使用说明书，功能查询和排障 |

## 自我进化系统

`self-evolution/` 是一个 Phase 1 离线进化管道，与 `hanako-runtime-learner` 插件配合使用：

```
Phase 1（本仓库）                       Phase 2（runtime-learner 插件）
─────────────────                       ─────────────────────────────
任务执行 → 记录日志                          EventBus → 实时模式检测
      ↓                                         ↓
扫描模式 · 聚类 · 评分                      衰减分数 · 自动注入 SKILL.md
      ↓                                         ↓
周报 + skill 候选草案                       人工审核 · 批准/拒绝/回滚
      ↓
人工审核 → 手动安装
```

**安全原则**：进化系统不会自动安装任何 skill。所有改动（无论是 Phase 1 的候选草案
还是 Phase 2 的注入提示）都必须经过人工审核。

详见 [`self-evolution/README.md`](self-evolution/README.md)。

## 设计原则

- **不重复** — 32 个 skill 触发条件明确隔离，无功能重叠
- **低耦合** — 每个 skill 独立安装、独立移除
- **实战验证** — 全部在学术写作和日常开发中实际使用过
- **不自动安装** — 安装脚本跳过已有 skill，不覆盖不删除

## 更新

```powershell
git pull
.\install.ps1
```

## 参与贡献

欢迎提交新的 skill 或改进已有 skill。

1. Fork 本仓库
2. 使用 `skill-creator` skill 辅助创建新 skill
3. 放入 `skills/` 对应分类目录
4. 确保 `SKILL.md` 包含清晰的触发条件（MANDATORY TRIGGERS）
5. 提交 Pull Request

新 skill 审核标准：
- 触发条件明确，不与其他 skill 冲突
- 指令具体可执行，非泛泛建议
- 如涉及外部工具，声明依赖和兼容性

## 相关项目

- [hanako-ui-beautify](https://github.com/326sun/hanako-ui-beautify) — 鸿蒙黑体 + 动效美化插件
- [hanako-runtime-learner](https://github.com/326sun/hanako-runtime-learner) — Phase 2 运行时自学习插件
- [Hanako](https://github.com/liliMozi/openhanako) — 上游项目

## 许可

MIT
