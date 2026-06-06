# Hanako Skills Collection

> 为 HanaAgent (OpenHanako) 精选的 skills 集合 + 自我进化系统。
> 直接下载到 `%USERPROFILE%\.hanako\skills\` 即可使用。

---

## 包含内容

### Skills（20个）

| 类别 | Skill | 用途 |
|------|-------|------|
| 📝 学术 | `academic-suite` | 三合一审稿工具（导师/审稿人/写作助手） |
| 📝 学术 | `scientific-writing` | 英文学术写作规范 |
| 📝 学术 | `thesis-docx` | 学位论文 Word 排版 |
| 📝 学术 | `literature-review` | 系统文献检索与综述 |
| 📝 学术 | `journal-figures` | 期刊配图设计指南（Nature 风格） |
| 📊 数据 | `data-analysis` | pandas/numpy/scipy 数据处理 |
| 📊 数据 | `data-visualization` | matplotlib/seaborn 科学可视化 |
| 📄 文档 | `office-documents` | Word/Excel/PPT/PDF 通用操作 |
| 🧠 推理 | `adaptive-reasoning` | 自动评估任务复杂度并调整回答深度 |
| 🧠 推理 | `quiet-musing` | 深度推理框架（复杂问题专用） |
| 🔧 开发 | `skill-creator` | 创建和修改 skills |
| 🔧 开发 | `mcp-builder` | MCP 服务器构建指南 |
| 🔧 开发 | `hana-plugin-creator` | Hana 插件创建 |
| 📐 图表 | `mermaid-diagrams` | Mermaid 图表生成 |
| 🔍 工具 | `article-extractor` | 从 URL 提取干净文章 |
| 🔍 工具 | `self-improving-agent` | 错误记录与经验积累 |
| 🎨 创作 | `algorithmic-art` | p5.js 算法艺术 |
| 🎨 创作 | `canvas-design` | Canvas 设计 |
| 📖 帮助 | `user-guide` | HanaAgent 使用说明书 |

### 自我进化系统

`self-evolution/` 目录包含一个完整的自我进化管道（Phase 1），让 Hanako 能够：

- 记录每次复杂任务的经验和错误
- 自动扫描日志、发现重复模式
- 计算 pattern_score 判断是否值得 skill 化
- 生成周报和高分候选报告

详见 [`self-evolution/README.md`](self-evolution/README.md)。

---

## 一键安装

### Windows (PowerShell)

```powershell
# 克隆仓库
git clone https://github.com/YOUR_USERNAME/hanako-skills-collection.git
cd hanako-skills-collection

# 安装 skills 到 HanaAgent
.\install.ps1
```

`install.ps1` 会将所有 skills 复制到 `%USERPROFILE%\.hanako\skills\`，自我进化系统复制到当前工作目录。

### 手动安装

```powershell
# 复制 skills
Copy-Item -Recurse -Force .\skills\* $env:USERPROFILE\.hanako\skills\

# 复制自我进化系统到你想要的工作区
Copy-Item -Recurse -Force .\self-evolution\ D:\YourWorkspace\Hanako_Self_Evolution\
```

### 选择性安装

如果你只需要部分 skills，手动复制对应目录即可。例如：

```powershell
Copy-Item -Recurse -Force .\skills\academic-suite\ $env:USERPROFILE\.hanako\skills\
Copy-Item -Recurse -Force .\skills\journal-figures\ $env:USERPROFILE\.hanako\skills\
```

---

## Skills 设计原则

这个集合遵循以下原则：

1. **不重复**：skills 之间触发条件明确隔离，避免多个 skill 同时响应同一请求
2. **低耦合**：每个 skill 可独立安装和使用
3. **高质量**：经过实际使用验证，无冗余模板
4. **学术优先**：面向学术写作、数据处理、论文投稿场景优化

---

## 更新

```powershell
git pull
.\install.ps1
```

---

## 许可

MIT — 自由使用、修改、分发。

## 贡献

欢迎提 Issue 和 PR。如果你有好的 skill 想加入这个集合，请确保它满足上述设计原则。
