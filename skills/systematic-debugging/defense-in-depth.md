# 纵深防御验证

## 概述

修复一个由无效数据导致的 bug 时，在一个地方加验证感觉就够了。但那单个检查可以被不同的代码路径、重构或 mock 绕过。

**核心原则**：在数据流经的每一层都加验证。让 bug 在结构上不可能发生。

## 四层防护

### 第 1 层：入口验证

在 API 边界拒绝明显无效的输入。

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory cannot be empty');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory does not exist: ${workingDirectory}`);
  }
  // ... proceed
}
```

### 第 2 层：业务逻辑验证

确保数据对这个操作有意义。

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('projectDir required for workspace initialization');
  }
  // ... proceed
}
```

### 第 3 层：环境守卫

防止在特定上下文中执行危险操作。

```typescript
async function gitInit(directory: string) {
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `Refusing git init outside temp dir during tests: ${directory}`
      );
    }
  }
  // ... proceed
}
```

### 第 4 层：调试插桩

捕获上下文供取证分析。

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('About to git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
  // ... proceed
}
```

## 应用步骤

发现 bug 后：

1. **追溯数据流**：坏的值从哪里来？在哪里被使用？
2. **标出所有检查点**：列出数据经过的每个点
3. **在每层添加验证**：入口、业务、环境、调试
4. **测试每一层**：尝试绕过第 1 层，验证第 2 层能否捕获

## 关键洞察

四层都需要。测试中，不同层会捕获其他层漏掉的不同 bug：
- 不同代码路径绕过入口验证
- Mock 绕过业务逻辑检查
- 不同平台的边缘情况需要环境守卫
- 调试日志识别结构性误用

**不要只在一个验证点停下。在每一层都加检查。**
