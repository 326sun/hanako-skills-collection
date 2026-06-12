<p align="center">
  <strong>Hanako Skills Collection</strong><br>
  <sub>装完即用，不再到处找</sub>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/skills-41-blue" alt="skills">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="license">
  <img src="https://img.shields.io/badge/pr-welcome-brightgreen" alt="pr">
</p>

---

## 这是什么

Hanako 生态中持续增长的开源 skills 集合。每个 skill 是一份文本指令，告诉 Agent 在特定场景下怎么思考、怎么操作、怎么输出。

**目标：装完这个仓库，日常场景不再需要去别处找 skills。**

覆盖七个领域——学术写作、数据处理、开发运维、代码审查、图表创作、办公效率、深度推理。每个 skill 都经过实战验证，独立安装，独立移除。

---

## 目录

- [快速开始](#快速开始)
- [Skills 目录](#skills-目录)
- [按场景查找](#按场景查找)
- [生态系统](#生态系统)
- [自我进化](#自我进化)
- [设计原则](#设计原则)
- [参与贡献](#参与贡献)
- [相关项目](#相关项目)

---

## 快速开始

```powershell
git clone https://github.com/326sun/hanako-skills-collection.git
cd hanako-skills-collection
.\install.ps1
```

重启 Hanako 生效。已安装的 skill 会自动跳过，不会覆盖。

只想装某几个？手动复制：

```powershell
Copy-Item -Recurse .\skills\academic-suite $env:USERPROFILE\.hanako\skills\
```

---

## Skills 目录

### 学术写作

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `academic-suite` | 三合一审稿：导师反馈 + 同行评审 + 格式检查 | 论文反馈、学位论文审查、投稿前检查 |
| `scientific-writing` | 英文学术写作规范 | 时态选择、hedging、术语一致性 |
| `thesis-docx` | 学位论文 Word 排版 | 样式规范化、标题编号、页眉页脚 |
| `literature-review` | 系统文献检索 | 可复现检索策略、PRISMA 流程图 |
| `journal-figures` | Nature 风格配图 | 图形摘要、机制图、TOC 图 |
| `data-visualization` | matplotlib/seaborn 出版级图表 | 600 dpi、SVG 输出、配色方案 |

### 数据处理与文档

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `data-analysis` | pandas/numpy/scipy 仿真数据处理 | 实验数据清洗、统计分析 |
| `office-documents` | Word / Excel / PPT / PDF 读写 | 打开、解析、修改、格式转换 |

### 深度推理

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `adaptive-reasoning` | 自动判断任务复杂度 | 简单不废话，复杂深思考 |
| `quiet-musing` | 五阶段深度推理框架 | 多步骤问题、架构设计、权衡决策 |

### 代码审查与安全

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `code-reviewer` | 四级严重度系统审查 | 安全、正确性、性能、可维护性 |
| `security-audit` | 安全审计清单 | 依赖漏洞、OWASP Top 10、配置加固 |
| `test-generator` | 自动生成测试用例 | 单元测试、边界测试、集成测试 |

### 开发工具

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `api-designer` | RESTful API 设计 | OpenAPI 规范、错误码体系、版本策略 |
| `database-design` | SQL 优化与表设计 | 索引策略、查询优化、迁移管理 |
| `docker-deploy` | Dockerfile 最佳实践 | 镜像瘦身、多阶段构建、安全加固 |
| `git-workflow` | 规范化 git 操作 | Commit message、分支命名、PR 描述 |
| `shell-scripting` | Shell/PowerShell 脚本 | 跨平台兼容、幂等性、错误处理 |
| `regex-builder` | 正则表达式构造与解释 | 模式匹配、测试用例生成 |
| `mcp-builder` | MCP 服务器构建 | Python FastMCP + Node.js SDK |
| `hana-plugin-creator` | Hana 插件脚手架 | SDK 模板、manifest 配置 |
| `config-generator` | 配置文件模板生成 | .env、docker-compose、CI/CD、tsconfig |
| `package-management` | 跨语言包管理器速查 | npm、pip、cargo、go mod、apt、brew |
| `project-init` | 项目初始化和脚手架 | 目录结构、README、许可证、CHANGELOG |
| `dev-environment` | 开发环境配置 | Node、Python、C/C++、环境变量排障 |
| `data-format` | 数据格式转换 | JSON/YAML/TOML/CSV/XML 互转与校验 |
| `subagent-driven-development` | 子 Agent 驱动开发：按计划派发 + 两阶段审查 | 实现计划执行、任务分发、独立审查管道 |
| `grill-with-docs` | 需求对齐审问 + 共享语言 + ADR | 新功能规划、架构方案讨论、项目启动 |
| `tdd` | 测试驱动开发：红绿重构循环 | 新功能开发、bug 修复、测试覆盖 |
| `diagnose` | 五阶段高纪律调试：反馈回路→复现→多假设→探测→修复 | 任何 bug、性能退化、偶发问题，禁止无回路就修 |

### 写作与翻译

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `translator` | 中英互译 | 学术术语一致性、语域匹配 |
| `tech-doc-writer` | 技术文档写作 | API 文档、README、ADR、Changelog |

### 图表与设计

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `mermaid-diagrams` | 自然语言 → 流程图 / SVG | 架构图、时序图、ER 图 |
| `algorithmic-art` | p5.js 算法艺术 | 流场、粒子系统、生成艺术 |
| `canvas-design` | Canvas 设计 | 海报、封面、30+ 开源字体 |
| `apple-minimal-ui` | Apple 极简风格前端规范 | 网页/组件/仪表板，禁用论文配图 |

### 办公效率

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `presentation-builder` | 演示文稿生成 | 大纲、幻灯片内容、演讲备注 |
| `browser-automation` | 浏览器自动化指南 | 填表、截图、数据提取 |
| `article-extractor` | URL → 干净正文 | 去广告、去导航栏 |

### 技能开发

| Skill | 一句话 | 触发场景 |
|---|---|---|
| `skill-creator` | 创建和迭代 skills | 评估、基准测试、自动优化 |
| `user-guide` | Hanako 使用说明书 | 功能查询、排障、技巧 |

---

## 按场景查找

**我要写论文**
→ `academic-suite` `scientific-writing` `thesis-docx` `literature-review` `journal-figures` `data-visualization`

**我要做数据分析**
→ `data-analysis` `data-visualization` `office-documents`

**我要写代码**
→ `code-reviewer` `test-generator` `api-designer` `database-design` `git-workflow` `shell-scripting` `regex-builder` `project-init`

**我要按计划执行复杂开发任务**
→ `subagent-driven-development` `quiet-musing` `code-reviewer`

**我要做需求对齐 / 讨论方案**
→ `grill-with-docs` `quiet-musing`

**我要做测试驱动开发**
→ `tdd` `test-generator`

**我要调试 bug / 排障**
→ `diagnose` `quiet-musing` `test-generator`

**我要部署上线**
→ `docker-deploy` `security-audit` `mcp-builder` `config-generator` `dev-environment`

**我要做设计/图表**
→ `mermaid-diagrams` `algorithmic-art` `canvas-design` `journal-figures`

**我要写前端界面**
→ `apple-minimal-ui`

**我要写文档**
→ `tech-doc-writer` `translator` `presentation-builder`

**我要开发 Hanako 插件或 Skills**
→ `hana-plugin-creator` `skill-creator` `mcp-builder`

**我需要深度思考**
→ `adaptive-reasoning` `quiet-musing`

**我要管理系统环境**
→ `dev-environment` `package-management` `data-format` `config-generator`

---

## 生态系统

```
┌──────────────────────────────────────────────────┐
│ Hanako Agent（Pi 框架）                            │
├──────────────────────────────────────────────────┤
│                                                  │
│  hanako-skills-collection  ← 这个仓库             │
│  ┌────────────────────┐                          │
│  │ 41 个 skills        │  文本指令                │
│  │ 教 Agent 怎么做事    │  独立安装 独立移除         │
│  └────────────────────┘                          │
│                                                  │
│  hanako-runtime-learner  ← 插件（运行时）          │
│  ┌────────────────────┐                          │
│  │ 观察交互 · 发现模式  │  可执行代码               │
│  │ 自动注入 · 持续进化  │  让 skills 越用越好       │
│  └────────────────────┘                          │
│                                                  │
│  hanako-ui-beautify  ← 插件（视觉）               │
│  ┌────────────────────┐                          │
│  │ 鸿蒙黑体 · 动效补丁  │  可执行代码               │
│  │ Spring Animation   │  asar 注入               │
│  └────────────────────┘                          │
└──────────────────────────────────────────────────┘
```

三者的分工：**skills 定义行为标准，runtime-learner 让 skills 在使用中动态优化，ui-beautify 改善视觉体验。**

---

## 自我进化

`self-evolution/` 是一个 Phase 1 离线进化管道。它在本地运行，扫描 task 日志，从重复模式中提取 skill 候选草案。

```
任务执行 → 记录日志 → 模式扫描 → 评分聚类 → 周报 + skill 候选草案
                                                      ↓
                                                 人工审核后安装
```

这与 `hanako-runtime-learner` 插件（Phase 2 实时进化）互补。Phase 1 做离线深度分析，Phase 2 做在线实时学习。

**安全声明**：进化管道不会自动安装任何 skill。所有候选必须经过人工审核。

详见 [`self-evolution/README.md`](self-evolution/README.md)。

---

## 设计原则

- **触发条件明确** 每个 skill 的 `description` 都包含 `MANDATORY TRIGGERS`，确保在正确场景激活
- **不重复** 41 个 skill 的触发条件经过审查，避免功能重叠导致的激活冲突。`diagnose` 已替代旧版 `systematic-debugging`
- **低耦合** 每个 skill 是独立目录，一个 SKILL.md 就是全部。复制即安装，删除即卸载
- **实战验证** 全部在学术写作和日常开发中使用过，不是理论设计
- **可组合** 复杂任务可以同时触发多个 skill，比如写论文时 `academic-suite` + `scientific-writing` + `journal-figures` 协同工作

---

## 更新

```powershell
git pull
.\install.ps1
```

---

## 参与贡献

欢迎提交新 skill 或改进已有 skill。贡献前请确认：

- [ ] 触发条件不与已有 skill 冲突
- [ ] 指令具体可执行，非泛泛建议
- [ ] 如涉及外部工具，声明依赖和兼容性
- [ ] 使用 `skill-creator` 辅助创建，确保格式规范

新 skill 应放入 `skills/` 下对应的分类目录（如无合适分类可新建）。

```powershell
# 1. Fork 本仓库
# 2. 使用 skill-creator 创建新 skill
# 3. 放入 skills/ 对应目录
# 4. 提交 Pull Request
```

---

## 相关项目

- [hanako-runtime-learner](https://github.com/326sun/hanako-runtime-learner) — 运行时自学习插件，让 skills 越用越精准
- [hanako-ui-beautify](https://github.com/326sun/hanako-ui-beautify) — 鸿蒙黑体 + Spring Animation 美化插件
- [Hanako](https://github.com/liliMozi/openhanako) — 上游项目

---

## License

MIT
