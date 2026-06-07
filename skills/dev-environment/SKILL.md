---
name: dev-environment
description: "Cross-platform development environment setup: Node.js, Python, C/C++, environment variables, path configuration, and common troubleshooting. 跨平台开发环境配置：Node.js、Python、C/C++、环境变量、路径配置与常见排障。MANDATORY TRIGGERS: setup dev environment, install python, install node, 配置开发环境, 装环境, 环境变量, PATH, virtualenv, venv, conda, nvm, 开发环境报错, 装不上, 依赖冲突, environment setup, dev setup"
---

# Development Environment

跨平台开发环境配置参考。不追求最新版本，追求稳定可复现。

## 通用原则

- 优先使用包管理器而非手动安装，确保可卸载和可升级
- 项目级依赖优先于全局依赖（`venv` / `nvm` / `local node_modules`）
- Windows 下避免路径含中文和空格
- 装完后立即验证：`node --version` / `python --version` / `gcc --version`

## Node.js

### 安装

| 平台 | 推荐方式 |
|---|---|
| Windows | [nvm-windows](https://github.com/coreybutler/nvm-windows) 管理多版本 |
| macOS | `brew install node` 或 `nvm` |
| Linux | `nvm`（curl 脚本安装） |

```powershell
# nvm-windows 常用命令
nvm list available      # 可安装版本
nvm install 20.11.0     # 安装 LTS
nvm use 20.11.0         # 切换版本
```

### 常见问题

- **`npm install` 报 node-gyp 错误** → 装 Visual Studio Build Tools（Windows）或 Xcode CLI（macOS）
- **`node_modules` 不完整** → `rm -rf node_modules && npm cache clean --force && npm install`
- **PowerShell 执行策略** → `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser`
- **npm 全局包找不到** → 检查 `npm root -g` 是否在 PATH 中

## Python

### 安装

| 平台 | 推荐方式 |
|---|---|
| Windows | [Python.org](https://python.org) 安装包，**勾选 "Add Python to PATH"** |
| macOS | `brew install python@3.12` |
| Linux | 系统包管理器，或 [pyenv](https://github.com/pyenv/pyenv) |

### 虚拟环境

```powershell
# venv（内置）
python -m venv .venv
.venv\Scripts\activate       # Windows
source .venv/bin/activate    # macOS/Linux

# conda
conda create -n myenv python=3.12
conda activate myenv
```

### 常见问题

- **`pip install` 权限错误** → 不要用 `sudo pip`，用虚拟环境
- **多版本 Python 冲突** → `where python`（Windows）/ `which -a python`（macOS/Linux）查路径优先级
- **`ModuleNotFoundError`** → 检查是否在正确的虚拟环境中，`pip list` 确认包已安装
- **SSL 证书错误** → `pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org`

## C/C++

| 平台 | 编译器 | 安装 |
|---|---|---|
| Windows | MSVC | Visual Studio Build Tools，选 "C++桌面开发" |
| Windows | MinGW | `winget install -e --id GnuWin32.Make` + [MinGW-w64](https://www.mingw-w64.org/) |
| macOS | Clang | `xcode-select --install` |
| Linux | GCC | `sudo apt install build-essential` 或 `sudo dnf groupinstall "Development Tools"` |

## 环境变量

### Windows

```powershell
# 临时设置（当前 shell）
$env:MY_VAR = "value"

# 永久设置
[Environment]::SetEnvironmentVariable("MY_VAR", "value", "User")

# 查看
[Environment]::GetEnvironmentVariable("PATH", "User")
```

### macOS / Linux

```bash
# 临时
export MY_VAR="value"

# 永久（zsh）
echo 'export MY_VAR="value"' >> ~/.zshrc
# 永久（bash）
echo 'export MY_VAR="value"' >> ~/.bashrc
```

## 验证清单

装完环境后依次验证：
1. ✅ 编译器 / 解释器能打印版本号
2. ✅ 包管理器能安装一个简单包
3. ✅ 能创建一个最小项目并运行
4. ✅ PATH 中包含必要的 bin 目录
