---
name: indexer
description: 同步 opensource_learn 根 README 项目索引和 taxonomy.yaml 分类覆盖时必须使用。用户提到 /indexer、更新根 README、补齐未索引学习笔记、调整 rowspan、同步分类体系、学习完成后整理项目列表时使用。本 skill 不学习新仓库、不克隆源码。
---

# Indexer

维护两件事：

1. 根 `README.md` 项目索引。
2. 根 `taxonomy.yaml` 分类目录覆盖。

## 严格边界

- 只允许修改根 `README.md` 和根 `taxonomy.yaml`。
- 不学习新仓库，不 `git clone`，不 `curl`，不创建或删除 `*-learn` 目录。
- 不主动删除 `stale-link` 或 `stale-taxonomy-path`；发现后先在最终备注中说明，除非用户明确要求删除。
- 不运行 `git status`、`git diff`、`grep | head`、`cat | head` 等额外检查命令。
- Bash 命令必须简单直接：不要使用 pipeline、`&&`、`;`、`$()`、重定向或临时脚本。

## 固定流程

### 1. 获取仓库根目录

只运行：

```bash
git rev-parse --show-toplevel
```

后续命令使用得到的绝对路径，不要用 shell 变量拼接。

### 2. 运行校验

只运行：

```bash
python3 /absolute/repo/.claude/skills/indexer/scripts/validate_index.py /absolute/repo
```

结果处理：

- `PASS`：不修改文件，直接最终汇报。
- `unindexed-dir`：把对应学习目录补进根 `README.md`，这是正常待同步项。
- `missing-taxonomy-category`：补齐根 `taxonomy.yaml` 的分类定义。
- `rowspan`：修正根 `README.md` 中对应领域或分类的 `rowspan`。
- `stale-link`、`stale-taxonomy-path`：不自动修复，只汇报。

### 3. 补齐 README 索引

对每个 `unindexed-dir`：

1. 读取该目录的 `README.md`。
2. 展示名优先用标题；标题不清楚时用仓库 repo 名。
3. 简介优先用 `> ### 一句话概括` 后的第一段，压缩成一行中文。
4. 按路径插入到根 `README.md` 对应分类的 HTML table 中。
5. 同步修正领域和分类 `rowspan`。

项目行格式固定：

```html
<tr>
  <td><a href="./dev-tools/security/soxoj-maigret-learn">maigret</a></td>
  <td>一行中文简介</td>
</tr>
```

### 4. 补齐 taxonomy

只在校验出现 `missing-taxonomy-category` 时修改 `taxonomy.yaml`。

每个新增分类只写：

```yaml
slug:
  label: 简洁中文名
  path: domain/category
  include:
    - 一句中文收纳规则。
  examples: []
```

同时更新 `last_updated` 为当天日期。`taxonomy.yaml` 不记录单个学习项目。

### 5. 重新校验

每次修改后必须重新运行第 2 步校验。只有输出 `PASS` 才能按成功汇报。

## 最终汇报

只使用以下格式：

```markdown
## 索引同步结果

| 项目 | 结果 |
|------|------|
| 状态 | `<已同步/无需修改/失败>` |
| 根 README | `<已更新/未修改>` |
| taxonomy.yaml | `<已更新/未修改>` |
| 新增索引 | `<数量>` |
| 删除失效索引 | `<数量/未执行>` |
| 新增 taxonomy 分类 | `<数量>` |

### 验证

| 检查项 | 结果 |
|--------|------|
| 根索引与 taxonomy 校验 | `<PASS/FAIL；摘要>` |

### 备注

<如无异常，写“无”。>
```
