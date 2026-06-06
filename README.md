# Hanako Skills Collection

**给你的 HanaAgent 装上脑子。** 一套经过实战验证的 skills 集合，覆盖学术写作、数据处理、文档操作、深度推理，外加一个让 AI 越用越聪明的自我进化系统。

---

## 这是什么

[HanaAgent](https://github.com/liliMozi/openhanako)（OpenHanako）是运行在你电脑上的个人 AI 助手。Skills 是它的能力插件——每个 skill 教它在特定场景下怎么做、做到什么标准。

HanaAgent 装好之后自带的 skills 很少。这个仓库把日常高频场景（写论文、审稿、画图、处理文档、深度推理）需要的 skills 打包好，下载即用。同时附赠一套自我进化系统，让 HanaAgent 在长期使用中自动发现自己的问题、生成改进方案。

## 适合谁

- **学术研究者**：写论文、画期刊配图、模拟同行评审、文献检索
- **工程师/开发者**：数据处理、科学可视化、MCP 服务器开发、Hana 插件开发
- **HanaAgent 新用户**：不知道装什么 skills？从这里开始

## 快速开始

```powershell
git clone https://github.com/326sun/hanako-skills-collection.git
cd hanako-skills-collection
.\install.ps1
```

重启 HanaAgent 即可生效。只想装某几个 skill？手动复制对应的文件夹到 `%USERPROFILE%\.hanako\skills\` 就行。

## 包含什么

### 学术套件（6 个）

| Skill | 一句话说明 |
|-------|-----------|
| `academic-suite` | 三合一审稿：导师反馈 + 同行评审 + 格式检查，投稿前自检 |
| `scientific-writing` | 英文学术写作规范，从时态到 hedging 全覆盖 |
| `thesis-docx` | 学位论文 Word 排版，样式规范化一键处理 |
| `literature-review` | 系统文献检索与综述，带可复现的检索策略 |
| `journal-figures` | Nature 风格的期刊配图设计指南（机制图、图形摘要、TOC 图） |
| `data-visualization` | matplotlib/seaborn 出版级科学图表，600 dpi SVG 输出 |

### 数据处理（1 个）

| Skill | 一句话说明 |
|-------|-----------|
| `data-analysis` | pandas/numpy/scipy 仿真数据处理 |

### 文档处理（1 个）

| Skill | 一句话说明 |
|-------|-----------|
| `office-documents` | Word/Excel/PPT/PDF 读写一条龙 |

### 推理增强（2 个）

| Skill | 一句话说明 |
|-------|-----------|
| `adaptive-reasoning` | 自动判断问题复杂度，简单问题不废话，复杂问题深思考 |
| `quiet-musing` | 五阶段深度推理框架：理解→拆解→多路径→执行→验证 |

### 开发工具（3 个）

| Skill | 一句话说明 |
|-------|-----------|
| `skill-creator` | 创建和修改 skills，带评测和自动迭代 |
| `mcp-builder` | MCP 服务器构建指南，Python 和 Node.js 双栈 |
| `hana-plugin-creator` | Hana 插件脚手架和 SDK 模板 |

### 图表与创作（3 个）

| Skill | 一句话说明 |
|-------|-----------|
| `mermaid-diagrams` | 流程图、时序图、架构图，自然语言→SVG/PNG |
| `algorithmic-art` | p5.js 算法艺术生成 |
| `canvas-design` | Canvas 设计，内置 30+ 开源字体 |

### 效率工具（2 个）

| Skill | 一句话说明 |
|-------|-----------|
| `article-extractor` | 从网页 URL 提取干净正文，去广告去导航 |
| `self-improving-agent` | 错误记录与经验积累，跨 session 持续改进 |

### 帮助（1 个）

| Skill | 一句话说明 |
|-------|-----------|
| `user-guide` | HanaAgent 使用说明书，功能查询和排障 |

### 自我进化系统

`self-evolution/` 目录包含一个完整的 Phase 1 进化管道：

```
任务执行 → 记录经验 → 扫描模式 → 计算 pattern_score → 生成周报 → 高分候选 → 人工审核
```

具体做什么：
- 每次复杂任务后自动记录 experience_log 和 error_log
- 每周自动扫描日志，按错误类型聚类，计算每个 pattern 的 skill 化价值
- 对高分 pattern 自动生成 skill 候选草案
- **不自动安装任何 skill**，所有改动必须人工审核

详见 [`self-evolution/README.md`](self-evolution/README.md)。

---

## 设计原则

1. **不重复**：skill 之间触发条件明确隔离，19 个 skill 无功能重叠
2. **低耦合**：每个 skill 可独立安装、独立移除
3. **实战验证**：全部在日常学术和开发工作中实际使用过
4. **不自动安装**：安装脚本跳过已有 skill，不覆盖不删除

## 更新

```powershell
git pull
.\install.ps1
```

## 许可

MIT
