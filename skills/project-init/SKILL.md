---
name: project-init
description: "Project initialization and scaffolding: directory structure, README template, license selection, changelog setup, and best practices for new projects in any language. 项目初始化与脚手架：目录结构、README 模板、许可证选择、Changelog 配置。MANDATORY TRIGGERS: init project, create project, 初始化项目, 新建项目, 项目脚手架, scaffold, project structure, 项目结构, 从零开始, 项目模板, README 怎么写, 许可证选什么, license, changelog, boilerplate"
---

# Project Initialization

从零创建项目的标准流程。不依赖特定框架 CLI，关注跨语言通用的项目骨架质量。

## 流程

1. 确认项目类型（库 / CLI / Web 服务 / 桌面应用）
2. 确认语言和运行时
3. 生成目录结构
4. 生成核心文件

## 通用目录结构

```
my-project/
├── src/              # 源代码
├── tests/            # 测试（或与 src 同级 __tests__）
├── docs/             # 文档（可选）
├── scripts/          # 构建/部署脚本（可选）
├── .github/          # CI/CD 和 Issue 模板
│   └── workflows/
├── README.md
├── LICENSE
├── CHANGELOG.md
├── .gitignore
└── .editorconfig
```

## README 模板

```markdown
# Project Name

一句话描述项目做什么。

## 安装

\`\`\`bash
# 安装命令
\`\`\`

## 快速开始

\`\`\`bash
# 最小可用示例
\`\`\`

## 文档

- [使用指南](docs/usage.md)

## 开发

\`\`\`bash
# 开发环境搭建
\`\`\`

## License

MIT
```

原则：安装 → 快速开始 → 文档 → 开发四步，新手 30 秒内跑通。

## 许可证选择

| 场景 | 推荐 |
|---|---|
| 开源库 / 最宽松 | MIT |
| 开源库 / 需保留版权声明 | Apache 2.0 |
| 开源库 / 要求衍生作品同样开源 | GPL 3.0 |
| CLI 工具 | MIT 或 GPL 3.0 |
| 不想被云厂商白嫖 | AGPL 3.0 或 SSPL |

复制对应许可证全文到 `LICENSE` 文件，不要只写 "MIT License" 标题。

## CHANGELOG.md

遵循 [Keep a Changelog](https://keepachangelog.com/) 格式：

```markdown
# Changelog

## [Unreleased]

## [0.1.0] - 2026-06-07
### Added
- Initial release

[Unreleased]: https://github.com/user/repo/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/user/repo/releases/tag/v0.1.0
```

## .gitignore

语言特定的 `.gitignore` 从 [gitignore.io](https://www.toptal.com/developers/gitignore) 或 GitHub 模板生成。关键条目：

- 编译产物（`dist/`、`build/`、`target/`、`__pycache__/`）
- 依赖（`node_modules/`、`.venv/`）
- 环境变量（`.env`、`.env.local`）
- 操作系统文件（`.DS_Store`、`Thumbs.db`）
- IDE 配置（`.idea/`、`.vscode/`，除非团队共享）

## 版本管理

使用语义版本（SemVer）：`MAJOR.MINOR.PATCH`

- `MAJOR`：不兼容的 API 变更
- `MINOR`：向后兼容的新功能
- `PATCH`：向后兼容的 bug 修复

`0.x.y` 阶段视为不稳定，允许频繁 breaking。

## 开发体验

- `make` / `just` / `npm scripts` 提供统一入口：`make test`、`make lint`、`make build`
- pre-commit hook 做格式化和 lint，用 [pre-commit](https://pre-commit.com) 或 [husky](https://github.com/typicode/husky) + [lint-staged](https://github.com/lint-staged/lint-staged)
- CI 文件放在 `.github/workflows/ci.yml`，包含 lint + test + build

## 原则

- 不要过度工程化——空项目不需要微服务架构
- README 是门面，先写 README 再写代码
- 许可证在第一次公开提交前确定
- `.gitignore` 在第一次 `git init` 前创建，避免误提交
