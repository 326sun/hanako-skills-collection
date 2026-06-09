# 条件等待

## 概述

脆弱的测试经常用任意延时猜测时序。这制造竞态条件：测试在快机器上通过，在负载下或 CI 中失败。

**核心原则**：等待你真正关心的条件，而不是猜测需要多长时间。

## 什么时候用

- 测试中有任意延时（`setTimeout`、`sleep`）
- 测试不稳定（有时通过，有时失败）
- 并行运行时测试超时
- 等待异步操作完成

**不用的时候**：测试实际的时序行为（debounce、throttle 间隔）。如果必须用任意超时，注释清楚为什么。

## 核心模式

```typescript
// ❌ 之前：猜测时序
await new Promise(r => setTimeout(r, 50));
const result = getResult();
expect(result).toBeDefined();

// ✅ 之后：等待条件
await waitFor(() => getResult() !== undefined);
const result = getResult();
expect(result).toBeDefined();
```

## 速查

| 场景 | 模式 |
|---|---|
| 等待事件 | `waitFor(() => events.find(e => e.type === 'DONE'))` |
| 等待状态 | `waitFor(() => machine.state === 'ready')` |
| 等待计数 | `waitFor(() => items.length >= 5)` |
| 等待文件 | `waitFor(() => fs.existsSync(path))` |
| 复杂条件 | `waitFor(() => obj.ready && obj.value > 10)` |

## 通用实现

```typescript
async function waitFor<T>(
  condition: () => T | undefined | null | false,
  description: string,
  timeoutMs = 5000
): Promise<T> {
  const startTime = Date.now();

  while (true) {
    const result = condition();
    if (result) return result;

    if (Date.now() - startTime > timeoutMs) {
      throw new Error(`Timeout waiting for ${description} after ${timeoutMs}ms`);
    }

    await new Promise(r => setTimeout(r, 10)); // 每 10ms 轮询一次
  }
}
```

## 常见错误

- ❌ 轮询太快：`setTimeout(check, 1)` 浪费 CPU
- ✅ 修复：每 10ms 轮询一次\
- ❌ 没有超时：条件永远不满足时永远循环
- ✅ 修复：始终包含超时，附带清晰错误信息
- ❌ 过期数据：循环外缓存状态
- ✅ 修复：在循环内调用 getter 获取最新数据

## 仅在正确使用任意超时时

```typescript
// 工具每 100ms tick 一次，需要 2 个 tick 验证部分输出
await waitForEvent(manager, 'TOOL_STARTED'); // 首先：等待条件
await new Promise(r => setTimeout(r, 200));   // 然后：等待时序行为
// 200ms = 100ms 间隔下 2 个 tick，已记录并解释原因
```

**要求**：
1. 先等待触发条件
2. 基于已知时序（不是猜测）
3. 注释解释原因
