---
name: config-generator
description: "Generate configuration files: .env, docker-compose.yml, CI/CD pipelines, tsconfig.json, pyproject.toml, .editorconfig, and other common configs with best-practice defaults. 生成配置文件模板：.env、docker-compose、CI/CD 管道、语言项目配置等。MANDATORY TRIGGERS: generate config, create config file, 配置文件, 帮我写个配置, .env, docker-compose, dockerfile, tsconfig, pyproject, eslint, prettier, github actions, CI 配置, Makefile, .gitignore, .editorconfig, 项目配置"
---

# Configuration File Generator

根据项目上下文生成最佳实践的配置文件。每个配置附带注释解释关键选项。

## 使用方式

告诉 Agent 项目类型和需要的配置：

- "帮我生成一个 Node.js 项目的 tsconfig 和 eslint 配置"
- "给这个 Python 项目写 pyproject.toml 和 .env.example"
- "写一个 docker-compose.yml，包含 PostgreSQL 和 Redis"

## 通用配置

### .editorconfig

```ini
root = true

[*]
charset = utf-8
end_of_line = lf
indent_style = space
indent_size = 2
insert_final_newline = true
trim_trailing_whitespace = true

[*.md]
trim_trailing_whitespace = false

[Makefile]
indent_style = tab
```

### .gitignore

根据项目类型生成。先判断语言/框架，再选择合适的模板。Node.js 项目至少包含：

```gitignore
node_modules/
dist/
.env
.env.local
*.log
.DS_Store
```

## 语言项目配置

### TypeScript — tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "sourceMap": true
  },
  "include": ["src"],
  "exclude": ["node_modules", "dist"]
}
```

### Python — pyproject.toml

```toml
[project]
name = "my-project"
version = "0.1.0"
requires-python = ">=3.10"

[build-system]
requires = ["setuptools>=68.0"]
build-backend = "setuptools.build_meta"

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

### Rust — Cargo.toml (关键字段)

```toml
[package]
name = "my-project"
version = "0.1.0"
edition = "2021"

[dependencies]

[profile.release]
opt-level = 3
lto = true
```

## 容器与编排

### Dockerfile

```dockerfile
# 多阶段构建模板
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json ./
EXPOSE 3000
USER node
CMD ["node", "dist/index.js"]
```

### docker-compose.yml

```yaml
services:
  app:
    build: .
    ports:
      - "3000:3000"
    env_file: .env
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: ${DB_USER}
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: ${DB_NAME}
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${DB_USER}"]
      interval: 5s
      timeout: 5s
      retries: 5

volumes:
  pgdata:
```

## CI/CD

### GitHub Actions — Node.js

```yaml
name: CI
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm test
      - run: npm run lint
```

### GitHub Actions — Python

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-python@v5
    with:
      python-version: "3.12"
      cache: pip
  - run: pip install -r requirements.txt
  - run: pytest
  - run: ruff check .
```

## 环境变量

### .env.example

```bash
# 数据库
DB_HOST=localhost
DB_PORT=5432
DB_USER=app_user
DB_PASSWORD=change_me
DB_NAME=app_db

# API
API_KEY=your_api_key_here
API_BASE_URL=https://api.example.com

# 应用
NODE_ENV=development
PORT=3000
LOG_LEVEL=info
```

## 原则

- 每个配置项加注释解释用途，不是无注释的模板堆砌
- 优先推荐社区主流方案（ruff → pylint，pnpm → yarn）
- 生成前先确认项目类型和已有配置，不覆盖用户自定义
- `.env` 和密钥类配置一律生成 `.env.example`，不含真实值
