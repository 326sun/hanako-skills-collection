---
name: test-generator
description: "Automatically generate unit tests, integration tests, edge case tests, and test fixtures. 自动生成单元测试、集成测试、边界用例和测试固件。Triggers: write tests, generate tests, add test coverage, 写测试, 生成测试, 测试用例, unit test, 单元测试, missing tests, 补测试"
---

# Test Generator

根据被测代码的特征自动生成测试用例。

## 测试类型优先级

先判断被测代码的性质：

| 代码类型 | 优先测试 |
|---------|---------|
| 纯函数 | 边界值、等价类、异常输入 |
| 有副作用的函数 | mock 外部依赖、验证副作用 |
| 异步代码 | 超时、并发、错误回调 |
| API 接口 | 状态码、响应体、认证 |
| 数据库操作 | 事务回滚、约束违反、并发写入 |

## 测试用例清单

对每个函数至少覆盖：

1. **Happy path** — 正常输入，预期正常输出
2. **边界值** — 空值、零值、最大值、最小值
3. **异常输入** — 错误类型、null/undefined、超长字符串
4. **组合场景** — 多个参数的组合边界

## 输出格式

```markdown
## [函数名] 测试计划

### Happy Path
\`\`\`language
// 正常输入 → 预期正常输出
\`\`\`

### 边界测试
\`\`\`language
// 空值、零值、极值
\`\`\`

### 异常测试
\`\`\`language
// 错误输入 → 预期错误处理
\`\`\`
```

## 原则

- 测试应该验证行为，不是验证实现
- 每个测试只测一件事
- 测试名描述场景：`should_returnError_when_inputIsEmpty`
- 不要为了覆盖率写无意义的测试
- mock 只 mock 外部边界（网络、文件系统、数据库），不 mock 内部函数
