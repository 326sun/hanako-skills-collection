# 根因追溯

## 概述

Bug 经常在调用栈深处显现。在错误出现处修复是修症状。

**核心原则**：沿调用链向后追溯，找到原始触发点，在源头修复。

## 追溯过程

### 1. 观察症状

```
Error: git init failed in ~/project/packages/core
```

### 2. 找到直接原因

什么代码直接导致了这个问题？

```typescript
await execFileAsync('git', ['init'], { cwd: projectDir });
```

### 3. 问：谁调用了这个？

```typescript
WorktreeManager.createSessionWorktree(projectDir, sessionId)
  → Session.initializeWorkspace() 调用
  → Session.create() 调用
  → test 中 Project.create() 调用
```

### 4. 继续向上追溯

传入了什么值？

- `projectDir = ''`（空字符串）
- 空字符串作为 `cwd` 解析为 `process.cwd()`
- 那恰好是源代码目录

### 5. 找到原始触发点

空字符串从哪里来？

```typescript
const context = setupCoreTest(); // 返回 { tempDir: '' }
Project.create('name', context.tempDir); // 在 beforeEach 之前访问
```

### 6. 在源头修复

根因：顶层变量初始化时访问了空值。

修复：让 `tempDir` 变成 getter，在 `beforeEach` 之前访问就抛出。

## 添加堆栈插桩

无法手动追溯时，添加插桩：

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  console.error('DEBUG git init:', {
    directory,
    cwd: process.cwd(),
    nodeEnv: process.env.NODE_ENV,
    stack,
  });

  await execFileAsync('git', ['init'], { cwd: directory });
}
```

**关键**：测试中用 `console.error()`（不用 logger，可能被抑制）

## 查找污染源

如果某个问题在测试中出现但不知道是哪个测试导致的，逐个运行测试直到找到第一个触发者。

## 核心原则

**永远不要在症状处修复。** 追溯直到找到原始触发点，在那里修复。然后在数据流的每一层添加验证（见 `defense-in-depth.md`），让这个 bug 在结构上不可能再发生。
