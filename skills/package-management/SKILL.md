---
name: package-management
description: "Cross-language package manager reference: npm, pip, cargo, go mod, NuGet, brew, winget, apt, dnf. Install, remove, audit, lock file management, dependency conflict resolution. 跨语言包管理器速查：安装、卸载、审计、锁文件、依赖冲突解决。MANDATORY TRIGGERS: install package, 安装包, npm install, pip install, cargo add, go get, 依赖管理, dependency, package manager, update packages, 更新依赖, lock file, audit fix, 安全漏洞, 依赖冲突, 怎么装这个包"
---

# Package Management

跨语言包管理器速查。按语言和生态组织，覆盖安装、更新、审计、故障处理。

## npm / pnpm / Yarn

```bash
# 安装
npm install <pkg>           # 依赖（dependencies）
npm install -D <pkg>        # 开发依赖
npm install -g <pkg>        # 全局安装
npm ci                      # 从 lock 文件精确安装

# 审计与更新
npm audit                   # 安全审计
npm audit fix               # 自动修复
npm outdated                # 查看过时依赖
npm update <pkg>            # 更新单个

# 清理
npm cache clean --force
rm -rf node_modules package-lock.json && npm install   # 重装
```

**npm vs pnpm vs Yarn**：pnpm 磁盘效率最高（全局缓存 + 硬链接），npm 兼容性最好，Yarn 生态最成熟。新项目推荐 pnpm。

## pip / pipx

```bash
# 安装
pip install <pkg>
pip install -r requirements.txt
pip install -e .            # 可编辑安装（开发模式）

# 应用级工具（不污染全局环境）
pipx install <tool>

# 审计
pip list --outdated
pip check                   # 检查依赖冲突

# 锁文件
pip freeze > requirements.txt       # 简单方式
pip-compile requirements.in         # pip-tools 方式（推荐）
```

**常见问题**：
- 依赖冲突 → 删 `requirements.txt` 底部具体版本，用 `>=` 而非 `==`
- `pip install` 太慢 → `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple <pkg>`

## cargo (Rust)

```bash
cargo add <crate>           # 添加依赖
cargo add -D <crate>        # 开发依赖
cargo update                # 更新 Cargo.lock
cargo update -p <crate>     # 更新单个
cargo audit                 # 安全审计（需 cargo-audit）
cargo tree                  # 依赖树
```

## Go Modules

```bash
go get <pkg>                # 添加依赖
go get <pkg>@v1.2.3         # 指定版本
go get -u <pkg>             # 更新到最新 minor
go mod tidy                 # 清理未使用依赖
go mod verify                # 校验 go.sum
go list -m -u all           # 查看可更新依赖
```

## NuGet (.NET)

```bash
dotnet add package <pkg>
dotnet add package <pkg> --version 1.2.3
dotnet list package --outdated
dotnet list package --vulnerable
```

## 系统包管理器

### Windows (winget)

```powershell
winget search <pkg>
winget install <id>
winget upgrade --all
winget list                  # 已安装列表
```

### macOS (Homebrew)

```bash
brew install <pkg>
brew upgrade <pkg>
brew list
brew cleanup                 # 清理旧版本
brew doctor                  # 诊断
```

### Linux

```bash
# Debian/Ubuntu
sudo apt update && sudo apt install <pkg>
sudo apt upgrade

# RHEL/Fedora
sudo dnf install <pkg>
sudo dnf update

# Arch
sudo pacman -S <pkg>
sudo pacman -Syu
```

## 依赖冲突解决

1. **锁文件优先**：`package-lock.json` / `Cargo.lock` / `go.sum` 是真相源，不要随便删
2. **版本范围用 `^` 而非 `*`**：`^1.2.3` 允许自动 minor/patch 更新但锁主版本
3. **npm 冲突** → `npm ls <pkg>` 看依赖树，用 `overrides`（npm）或 `resolutions`（Yarn）强制版本
4. **pip 冲突** → 用 `pip-tools` 的 `pip-compile` 解析完整依赖图
5. **安全预警** → `npm audit` 只是提示，不一定是实际可利用的漏洞。先查 CVE 详情再决定升级
