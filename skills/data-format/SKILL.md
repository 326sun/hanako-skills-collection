---
name: data-format
description: "Data format conversion and processing: JSON, YAML, TOML, CSV, XML, Markdown tables. Convert between formats, validate, query with jq/yq, and handle edge cases. 数据格式转换与处理：JSON、YAML、TOML、CSV、XML、Markdown 表格之间的互转、校验与查询。MANDATORY TRIGGERS: convert json to yaml, json to csv, 格式转换, 转成 JSON, 转成 YAML, parse csv, 解析 XML, jq, yq, markdown table, 数据格式, 格式化 JSON, validate json, 校验格式"
---

# Data Format Conversion

常见数据格式之间的转换、校验和查询。优先使用命令行工具（jq, yq, mlr）而非写脚本。

## 格式选型

| 格式 | 适用场景 | 不适合 |
|---|---|---|
| JSON | API 通信、前端配置、存储 | 人类手写维护、含注释的配置 |
| YAML | CI/CD、Docker、K8s | 深层嵌套、超大文件（性能差） |
| TOML | 项目配置（Cargo、pyproject） | 复杂嵌套结构 |
| CSV | 表格数据交换 | 嵌套数据、含逗号的非标准文本 |
| XML | 遗留系统、SOAP、文档格式 | 新项目（除非必须） |

## 命令行工具速查

### jq — JSON 查询

```bash
# 美化输出
cat data.json | jq .

# 提取字段
jq '.users[].name' data.json

# 过滤
jq '.[] | select(.age > 18)' data.json

# 聚合
jq 'group_by(.category) | map({cat: .[0].category, count: length})'

# 创建新 JSON
jq '{name: .user.name, email: .user.email}' data.json
```

### yq — YAML/JSON 互转

```bash
# YAML → JSON
yq -o=json config.yaml

# JSON → YAML
yq -P data.json            # -P 保留 YAML 格式

# 查询（兼容 jq 语法）
yq '.services | keys' docker-compose.yml

# 修改
yq -i '.version = "1.2.3"' package.yaml
```

### Miller (mlr) — CSV 处理

```bash
# CSV 预览
mlr --csv cat data.csv

# 统计
mlr --csv stats1 -a count,mean -f score data.csv

# 过滤
mlr --csv filter '$score > 60' data.csv

# CSV → JSON
mlr --c2j cat data.csv

# JSON → CSV
mlr --j2c cat data.json
```

## 常用转换

### JSON ↔ YAML

```bash
# json → yaml
yq -P data.json > config.yaml

# yaml → json
yq -o=json config.yaml > data.json
```

### CSV ↔ JSON

```bash
# csv → json (mlr)
mlr --c2j cat data.csv

# csv → json (Python)
python -c "
import csv,json,sys
r=csv.DictReader(sys.stdin)
json.dump(list(r),sys.stdout,indent=2)
" < data.csv

# json → csv (Python)
python -c "
import csv,json,sys
data=json.load(sys.stdin)
w=csv.DictWriter(sys.stdout,fieldnames=data[0].keys())
w.writeheader()
w.writerows(data)
" < data.json
```

### Markdown Table ↔ CSV

```bash
# csv → markdown table
mlr --icsv --omd cat data.csv

# markdown table → csv
# 用 Pandoc
pandoc table.md -t csv
```

### XML ↔ JSON

```bash
# xml → json
python -c "import xmltodict,json,sys; print(json.dumps(xmltodict.parse(sys.stdin.read()),indent=2))" < data.xml

# json → xml
# 用 xmltodict 的 unparse，或直接用 yq
```

## 常见问题

- **JSON 含注释** → JSON 标准不支持注释。用 JSONC（VS Code 格式）或 JSON5，或改用 YAML/TOML
- **CSV 含逗号** → 确保字段用双引号包裹：`"San Francisco, CA"`
- **YAML 缩进** → 只用空格，不用 Tab。2 空格缩进
- **大文件处理** → 不要 `jq` 加载整个文件到内存，用流式工具（Miller, `csvkit`）
- **编码问题** → 统一 UTF-8。Windows 生成的文件检查 BOM：`file data.csv`

## 原则

- 优先用专用工具（jq/yq/mlr）而非写循环脚本
- 转换前验证源格式：`jq empty data.json` / `yq eval 'true' config.yaml`
- 转换后验证目标格式，不信任中间结果
- 涉及敏感数据（密钥、token）时不在中间文件留存明文
