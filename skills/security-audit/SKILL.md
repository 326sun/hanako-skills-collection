---
name: security-audit
description: "Security audit checklist: dependency vulnerabilities, hardcoded secrets, OWASP Top 10, and configuration hardening. 安全审计清单：依赖漏洞、硬编码密钥、OWASP Top 10、配置加固。Triggers: security audit, security check, 安全检查, 安全审计, vulnerability scan, 漏洞扫描, dependency check, 依赖检查, harden, 加固, OWASP, secret detection, 密钥泄露"
---

# Security Audit

系统性的安全审计框架，覆盖代码、依赖、配置三个层面。

## 审计流程

### 1. 依赖安全
- 运行 `npm audit` / `pip audit` / `cargo audit` 检查已知漏洞
- 检查是否有超过 1 年未更新的依赖
- 检查间接依赖中是否有已被废弃的包
- 验证依赖的来源（registry 是否可信，是否有可能的拼写欺骗）

### 2. 密钥和敏感信息

搜索以下模式：

```
# 硬编码密钥
/secret\s*[:=]\s*['"][^'"]+['"]/
/key\s*[:=]\s*['"][^'"]+['"]/
/password\s*[:=]\s*['"][^'"]+['"]/
/token\s*[:=]\s*['"][^'"]+['"]/

# 私钥文件
-----BEGIN (RSA|EC|OPENSSH|DSA) PRIVATE KEY-----

# 常见服务密钥格式
sk-[a-zA-Z0-9]{48}           # OpenAI
ghp_[a-zA-Z0-9]{36}          # GitHub
AKIA[0-9A-Z]{16}             # AWS Access Key
```

### 3. OWASP Top 10 检查

| 类别 | 检查点 |
|------|-------|
| Broken Access Control | 每个 API 端点是否有权限校验？是否有越权风险？ |
| Cryptographic Failures | 是否用了 MD5/SHA1？是否自己实现加密？ |
| Injection | SQL/NoSQL/OS 命令是否用了参数化？ |
| Insecure Design | 是否有速率限制？错误信息是否泄露内部信息？ |
| Security Misconfiguration | CORS 是否过于宽松？HTTP Headers 是否配置？ |
| Vulnerable Components | 第三方库是否有已知 CVE？ |
| Auth Failures | 密码策略、session 管理、2FA 支持？ |
| Software & Data Integrity | CI/CD 管道是否安全？依赖签名验证？ |
| Logging & Monitoring | 是否记录了安全事件？是否有告警？ |
| SSRF | 用户控制的 URL 是否校验了目标？ |

### 4. 配置加固

```
# HTTP 安全头
Content-Security-Policy: default-src 'self'
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Strict-Transport-Security: max-age=31536000

# 环境
.env 文件是否在 .gitignore 中？
生产环境 DEBUG 是否关闭？
错误页面是否暴露了堆栈追踪？
```

## 报告格式

```
## 安全审计报告

### Critical（必须立即修复）
- [位置] 问题 → 修复方案

### High（本周内修复）
- [位置] 问题 → 修复方案

### Medium（下个迭代修复）

### Low（记录为技术债务）

### 总体评价
```
