# Hanako Skills Collection — 一键安装脚本
# 将 skills 复制到 HanaAgent skills 目录，自我进化系统复制到当前目录

param(
    [switch]$SkipSelfEvolution,
    [switch]$DryRun
)

$ErrorActionPreference = "Stop"

$SkillsSource = Join-Path $PSScriptRoot "skills"
$SkillsDest = Join-Path $env:USERPROFILE ".hanako\skills"
$SelfEvoSource = Join-Path $PSScriptRoot "self-evolution"
$SelfEvoDest = Join-Path (Get-Location) "Hanako_Self_Evolution"

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Hanako Skills Collection — 安装脚本" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# --- 1. 安装 Skills ---
Write-Host "[1/2] 安装 Skills..." -ForegroundColor Yellow
Write-Host "  源目录: $SkillsSource" -ForegroundColor Gray
Write-Host "  目标目录: $SkillsDest" -ForegroundColor Gray
Write-Host ""

if (-not (Test-Path $SkillsSource)) {
    Write-Host "  [错误] 未找到 skills 目录: $SkillsSource" -ForegroundColor Red
    Write-Host "  请在仓库根目录运行此脚本。" -ForegroundColor Red
    exit 1
}

# 确保目标目录存在
if (-not (Test-Path $SkillsDest)) {
    Write-Host "  创建目标目录: $SkillsDest" -ForegroundColor Gray
    if (-not $DryRun) {
        New-Item -ItemType Directory -Force -Path $SkillsDest | Out-Null
    }
}

# 逐个复制 skill 目录
$skillDirs = Get-ChildItem -Directory $SkillsSource
$installed = 0
$skipped = 0

foreach ($dir in $skillDirs) {
    $destDir = Join-Path $SkillsDest $dir.Name
    
    if (Test-Path $destDir) {
        Write-Host "  [跳过] $($dir.Name) — 目标已存在" -ForegroundColor DarkYellow
        $skipped++
    } else {
        Write-Host "  [安装] $($dir.Name)" -ForegroundColor Green
        if (-not $DryRun) {
            Copy-Item -Recurse -Force $dir.FullName $SkillsDest
        }
        $installed++
    }
}

Write-Host ""
Write-Host "  Skills: 安装 $installed 个, 跳过 $skipped 个" -ForegroundColor White
Write-Host ""

# --- 2. 安装自我进化系统 ---
if (-not $SkipSelfEvolution) {
    Write-Host "[2/2] 安装自我进化系统..." -ForegroundColor Yellow
    Write-Host "  源目录: $SelfEvoSource" -ForegroundColor Gray
    Write-Host "  目标目录: $SelfEvoDest" -ForegroundColor Gray
    Write-Host ""

    if (-not (Test-Path $SelfEvoSource)) {
        Write-Host "  [警告] 未找到 self-evolution 目录，跳过。" -ForegroundColor DarkYellow
    } elseif (Test-Path $SelfEvoDest) {
        Write-Host "  [跳过] 目标已存在: $SelfEvoDest" -ForegroundColor DarkYellow
    } else {
        Write-Host "  [安装] Hanako_Self_Evolution" -ForegroundColor Green
        if (-not $DryRun) {
            Copy-Item -Recurse -Force $SelfEvoSource $SelfEvoDest
        }
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  安装完成！" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  运行 'python Hanako_Self_Evolution\scripts\scan_experience.py' 测试自我进化系统。" -ForegroundColor Gray
Write-Host ""

if ($DryRun) {
    Write-Host "  (预演模式，未实际复制任何文件)" -ForegroundColor DarkYellow
}
