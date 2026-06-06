---
name: code-reviewer
description: "Systematic code review covering security vulnerabilities, performance issues, architectural flaws, and best-practice violations. 系统性代码审查，覆盖安全漏洞、性能问题、架构缺陷和最佳实践违规。Triggers: review this code, code review, check my code, 代码审查, 审查代码, 帮我看看这段代码, find bugs, security check, 安全检查"
---

# Code Reviewer

系统性地审查代码，按严重程度分级报告问题。

## 审查维度

按以下顺序逐项检查：

### 1. 安全（Critical）
- SQL 注入、XSS、命令注入
- 敏感信息硬编码（密钥、token、密码）
- 权限校验缺失
- 不安全的反序列化
- 路径遍历风险

### 2. 正确性（High）
- 边界条件处理（null、空数组、零值）
- 错误处理完整性（try/catch 范围、错误传播）
- 并发安全（竞态条件、死锁风险）
- 类型安全（隐式转换、不安全的 any）

### 3. 性能（Medium）
- 不必要的循环嵌套
- N+1 查询
- 大对象深拷贝
- 未使用缓存的热路径
- 阻塞 I/O 在异步上下文

### 4. 可维护性（Low）
- 函数过长（>50 行建议拆分）
- 魔法数字和硬编码
- 不一致的命名风格
- 缺少关键注释的复杂逻辑

## 输出格式

```
## 审查结果

### Critical
- [文件:行号] 问题描述 → 修复建议

### High
- [文件:行号] 问题描述 → 修复建议

### Medium
- [文件:行号] 问题描述 → 修复建议

### Low
- [文件:行号] 问题描述 → 修复建议

### 总体评价
一段话总结代码质量和最需要优先修复的问题。
```

## 原则
- 每条问题必须有具体文件和行号
- 每条问题必须有可操作的修复建议
- 不确定的问题标为 "INFO" 而非强行评级
- 不要只列问题不提建议
- 对初学者代码降低严格度，对生产代码提高严格度
