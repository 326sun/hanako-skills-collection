---
name: docker-deploy
description: "Docker best practices: multi-stage builds, layer optimization, security hardening, and docker-compose patterns. Docker 最佳实践：多阶段构建、层优化、安全加固和 Compose 编排模式。Triggers: Docker, Dockerfile, docker-compose, container, 容器, 部署, deploy, 镜像, containerize, 容器化"
---

# Docker Deploy

编写生产级 Dockerfile 和 Compose 文件的规范。

## Dockerfile 最佳实践

### 模板：Node.js 应用

```dockerfile
# Stage 1: Build
FROM node:22-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --omit=dev
COPY . .
RUN npm run build

# Stage 2: Production
FROM node:22-alpine
RUN addgroup -S app && adduser -S app -G app
WORKDIR /app
COPY --from=builder --chown=app:app /app/dist ./dist
COPY --from=builder --chown=app:app /app/node_modules ./node_modules
COPY --from=builder --chown=app:app /app/package.json ./
USER app
EXPOSE 3000
HEALTHCHECK --interval=30s CMD wget -qO- http://localhost:3000/health || exit 1
CMD ["node", "dist/main.js"]
```

### 核心规则

1. **使用具体版本标签**，不用 `latest`
2. **多阶段构建**：构建环境和运行环境分离
3. **非 root 用户运行**
4. **`.dockerignore` 排除** `node_modules`, `.git`, `*.log`
5. **层合并**：相关命令用 `&&` 连接以减少层数
6. **凭据管理**：不在镜像中硬编码密钥，用 build secrets

## Docker Compose 模式

```yaml
services:
  app:
    build: .
    ports: ["3000:3000"]
    environment:
      - NODE_ENV=production
    env_file: .env.production
    depends_on:
      db:
        condition: service_healthy
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "wget", "-qO-", "http://localhost:3000/health"]
      interval: 30s
      retries: 3

  db:
    image: postgres:16-alpine
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      POSTGRES_DB: app
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s

volumes:
  pgdata:
```

## 安全检查清单

- [ ] 基础镜像是否来自官方且使用固定版本？
- [ ] 是否以非 root 用户运行？
- [ ] 是否配置了 HEALTHCHECK？
- [ ] 敏感信息是否通过 env_file/secrets 注入？
- [ ] 是否限制了容器资源（mem_limit, cpus）？
- [ ] 是否暴露了不必要的端口？
