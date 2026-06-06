---
name: database-design
description: "SQL query optimization, schema design, indexing strategy, and migration management. SQL 查询优化、表结构设计、索引策略和迁移管理。Triggers: SQL, database, schema, index, migration, query, 数据库, 建表, 索引, 查询优化, ER diagram, 表结构, postgres, mysql, sqlite"
---

# Database Design

数据库设计、查询优化和迁移管理的规范和检查清单。

## Schema 设计原则

1. **每个表必须有主键** — 优先自增整数或 UUID
2. **范式化到 3NF** — 除非有明确的性能理由才反范式
3. **命名规范** — 表名用复数 snake_case（`user_orders`），列名见下表
4. **时间戳标配** — `created_at` 和 `updated_at` 每个业务表都应包含
5. **软删除优先** — 用 `deleted_at` 代替物理删除，除非有合规要求

### 列命名

| 类型 | 命名 | 示例 |
|------|------|------|
| 主键 | `id` | `id BIGSERIAL PRIMARY KEY` |
| 外键 | `{table}_id` | `user_id REFERENCES users(id)` |
| 时间 | `{action}_at` | `created_at`, `updated_at`, `deleted_at` |
| 布尔 | `is_{adjective}` | `is_active`, `is_verified` |
| 计数 | `{noun}_count` | `login_count` |

## 索引策略

```
-- 1. 主键自动建索引
-- 2. 外键必须建索引
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- 3. WHERE 条件高频列
CREATE INDEX idx_users_email ON users(email) WHERE deleted_at IS NULL;

-- 4. 复合索引：等值在前，范围在后
CREATE INDEX idx_orders_user_status ON orders(user_id, status);
-- 查询：WHERE user_id = ? AND status = ?  √
-- 查询：WHERE status = ?                 ✗（不走索引）

-- 5. 避免在索引列上使用函数
-- WHERE LOWER(email) = ?  → 建函数索引或应用层小写化
```

## 查询审查清单

执行每个 SQL 查询前检查：

- [ ] 是否有对应的索引支持？
- [ ] 是否避免了 `SELECT *`？（只取需要的列）
- [ ] 是否限制了返回行数？（`LIMIT`、分页）
- [ ] JOIN 的表是否都有索引在 JOIN 列上？
- [ ] 是否避免了 N+1 查询模式？
- [ ] 大表查询是否有合适的 WHERE 条件？
- [ ] 事务范围是否尽可能小？

## 迁移规范

1. 每次迁移应该是可逆的（有 up 就有 down）
2. 不要在迁移中包含数据迁移和 Schema 迁移混合
3. 大表加列：先加列（允许 NULL），再回填数据，最后加 NOT NULL
4. 大表改列类型：新建列 → 双写 → 回填 → 切换 → 删旧列
5. 部署前在 staging 环境验证迁移耗时
