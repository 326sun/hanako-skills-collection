---
name: shell-scripting
description: "Shell and PowerShell scripting best practices: error handling, cross-platform compatibility, input validation, and idempotency. Shell/PowerShell 脚本最佳实践：错误处理、跨平台兼容、输入校验、幂等性。Triggers: shell script, bash, PowerShell, .sh, .ps1, 写个脚本, 自动化脚本, batch script, cross-platform script, 命令行脚本"
---

# Shell Scripting

编写健壮、可维护的 Shell 和 PowerShell 脚本的规范。

## Bash 脚本模板

```bash
#!/usr/bin/env bash
set -euo pipefail  # 严格模式：遇错退出、未定义变量报错、管道错误传递

# === Configuration ===
readonly SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# === Functions ===
log_info()  { echo "[INFO]  $(date '+%Y-%m-%d %H:%M:%S') $*"; }
log_error() { echo "[ERROR] $(date '+%Y-%m-%d %H:%M:%S') $*" >&2; }

cleanup() {
  local exit_code=$?
  # 清理临时文件
  exit $exit_code
}
trap cleanup EXIT

# === Main ===
main() {
  log_info "Starting..."
  # 业务逻辑
}

main "$@"
```

## PowerShell 脚本模板

```powershell
#Requires -Version 7.0
[CmdletBinding()]
param(
    [Parameter(Mandatory=$false)]
    [string]$ConfigPath = "config.json"
)

$ErrorActionPreference = "Stop"

function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    Write-Host "[$Level] $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss') $Message"
}

try {
    Write-Log "Starting..."
    # 业务逻辑
} catch {
    Write-Log $_.Exception.Message "ERROR"
    exit 1
}
```

## 核心规则

1. **错误处理**：每个可能失败的命令都要处理返回值。bash 用 `set -euo pipefail`，PowerShell 用 `$ErrorActionPreference = "Stop"`
2. **输入校验**：参数存在性、类型、范围，不能假设用户会传正确的值
3. **幂等性**：脚本应该能安全地重复执行
4. **跨平台**：避免 `/tmp/` 硬编码，用 `mktemp`；路径用 `path.join` 等价物；避免 Linux 专有命令
5. **日志**：关键步骤记录时间戳和操作，错误输出到 stderr

## 不应做的事
- 不要 `rm -rf $UNCHECKED_VARIABLE` — 任何时候删东西前先确认路径非空且符合预期
- 不要在 PowerShell 里调用 `curl`（Windows 有别名问题，用 `curl.exe`）
- 不要假设当前目录是脚本目录
- 不要硬编码密码/密钥/Token

## 安全检查清单
- [ ] 是否使用了 `set -euo pipefail` 或等效？
- [ ] 敏感信息是否通过环境变量或配置文件传入？
- [ ] 临时文件是否在退出时清理？
- [ ] 路径是否处理了空格和特殊字符？
- [ ] 脚本是否可在不同机器上重复运行？
