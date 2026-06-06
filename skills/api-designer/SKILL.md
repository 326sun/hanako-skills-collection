---
name: api-designer
description: "RESTful API design with OpenAPI 3.1 specification: endpoint naming, error codes, pagination, versioning, and security patterns. RESTful API 设计，OpenAPI 3.1 规范：端点命名、错误码体系、分页、版本控制和安全模式。Triggers: design API, API design, REST API, OpenAPI, Swagger, endpoint, 设计接口, API 文档, API 规范, 后端接口"
---

# API Designer

设计一致、可预测的 RESTful API。

## 端点命名规范

```
GET    /api/v1/users          # 列表（支持分页、筛选、排序）
GET    /api/v1/users/:id      # 详情
POST   /api/v1/users          # 创建
PUT    /api/v1/users/:id      # 全量更新
PATCH  /api/v1/users/:id      # 部分更新
DELETE /api/v1/users/:id      # 删除

# 子资源
GET    /api/v1/users/:id/orders

# 动作（非 CRUD）
POST   /api/v1/users/:id/activate
```

规则：
- 用名词复数，不用动词（`/users` 不是 `/getUsers`）
- 用 kebab-case（`/order-items` 不是 `/orderItems` 或 `/order_items`）
- 版本号在前缀（`/api/v1/`）

## 统一响应格式

```json
{
  "code": 0,
  "message": "success",
  "data": {},
  "requestId": "uuid"
}
```

错误时：
```json
{
  "code": 40401,
  "message": "User not found",
  "detail": "No user with id=12345 exists",
  "requestId": "uuid"
}
```

## 错误码体系

```
格式：HTTP_STATUS + 2位业务码

40001  参数校验失败
40101  未认证
40102  Token 过期
40301  无权限
40401  资源不存在
40901  版本冲突（乐观锁）
42201  业务规则校验失败
42901  频率限制
50001  服务器内部错误
50301  服务不可用
```

## 分页规范

```
GET /api/v1/users?page=1&pageSize=20&sort=createdAt&order=desc

Response:
{
  "code": 0,
  "data": {
    "list": [...],
    "pagination": {
      "page": 1,
      "pageSize": 20,
      "total": 156,
      "totalPages": 8
    }
  }
}
```

## 安全要求

- 所有 API 默认需要认证（除非明确标记 public）
- 敏感数据（密码、Token）不出现在 URL 中
- 输入必须校验类型、长度、范围
- 输出只返回必要字段，不泄露内部实现
- 设置合理的速率限制
