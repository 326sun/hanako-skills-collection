---
name: browser-automation
description: "Guide for browser-based tasks: when to use the browser tool, form interaction patterns, data extraction strategies, and anti-detection techniques. 浏览器自动化指南：何时使用 browser 工具、表单交互模式、数据提取策略和反检测技巧。Triggers: browser, 浏览器, scrape, 抓取, web automation, 网页自动化, fill form, 填表, screenshot, headless, login page, 登录页面"
---

# Browser Automation

教授 Agent 何时以及如何正确使用浏览器工具。

## 什么时候用浏览器

**必须用浏览器：**
- 页面需要 JavaScript 渲染（SPA、React/Vue 应用）
- 需要登录、填表、点击交互
- `web_fetch` 返回空内容或 403
- 需要截图或视觉验证

**不需要浏览器（用 web_fetch）：**
- 静态博客文章
- API 返回的 JSON
- 纯 HTML 文档页面
- Markdown 文档

## 操作模式

### 1. 导航 → 快照 → 操作循环

```
navigate(url)
  ↓
snapshot()  ← 获取元素引用 [ref=N]
  ↓
click(ref) / type(ref, text)
  ↓
snapshot()  ← 确认页面变化
  ↓
继续操作或提取结果
```

关键规则：
- **每次 navigate/click/type 后必须重新 snapshot**，元素引用会过期
- 等待页面稳定后再操作（`wait(state: "networkidle")`）
- 操作前确认目标元素存在于最新 snapshot 中

### 2. 表单填写

```markdown
1. snapshot → 确认所有表单字段的 ref
2. 逐个 type(ref, value)
3. 对下拉框用 select(ref, value)
4. 对复选框用 click(ref)
5. 最后 click 提交按钮
6. snapshot → 验证结果（成功提示/错误信息）
```

### 3. 数据提取

```javascript
// 提取结构化数据的通用模式
evaluate(`
  JSON.stringify(
    [...document.querySelectorAll('.item')].map(el => ({
      title: el.querySelector('.title')?.textContent?.trim(),
      price: el.querySelector('.price')?.textContent?.trim(),
      link: el.querySelector('a')?.href
    }))
  )
`)
```

## 反检测

- 不要在短时间内高频操作（每次操作间隔 0.5-1s）
- 不要固定操作节奏（随机化间隔）
- 遇到验证码或登录墙，停止并告知用户

## 错误处理

| 情况 | 处理 |
|------|------|
| 元素未找到 | 等待 2s 后重试一次，仍失败则 snapshot 检查页面状态 |
| 超时 | 增加 timeout 参数，检查网络连接 |
| 导航失败 | 检查 URL 格式，尝试 HTTP→HTTPS |
| 内容未加载 | `wait(state: "networkidle")` 后重试 |
