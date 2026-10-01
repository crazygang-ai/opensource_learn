---
name: importer
description: 将一个 GitHub 仓库准备加入 opensource_learn 前必须使用。用户给出 GitHub URL、想判断是否已学习过、或想知道应该放到哪个分类目录时，使用本 skill。本 skill 只做 owner/repo 查重、读取目标仓库 README 后分类、必要时创建新分类目录，并最终只输出 GitHub 地址与绝对目标路径两行；不克隆源码、不生成学习笔记、不更新根 README。
---

# Importer

本 skill 是加入 `opensource_learn` 前的轻量准备步骤，只回答两个问题：

1. 这个 GitHub 仓库是否已经学习过。
2. 如果没学过，先看目标仓库 README，再按 `taxonomy.yaml` 判断学习笔记应该放到哪个分类目录。

它不克隆源码，不生成项目学习笔记，不更新根 `README.md`。

## 输入

必需输入：

- GitHub repository URL。

如果用户没有提供 URL，只询问 GitHub URL。不要主动询问展示名、简介、是否更新索引等额外问题。

## 必读上下文

开始前读取：

1. 当前仓库根 `taxonomy.yaml`

`REPO_ROOT` 指仓库根的绝对路径，使用此命令获取：

```bash
git rev-parse --show-toplevel
```

后续所有命令把 `<REPO_ROOT>` 替换成这条命令输出的绝对路径字面量。不要用 shell 变量拼接：每次 Bash 调用都是独立 shell，变量不会保留。

## 工作流程

### 1. 解析 GitHub URL

使用本 skill 的脚本解析 `owner`、`repo_name`、标准 GitHub URL 和学习目录名：

```bash
python3 "<REPO_ROOT>/.qoder/skills/importer/scripts/learn_target.py" parse "<github_url>"
```

学习目录名固定为：

```text
<owner>-<repo_name>-learn
```

### 2. 判断是否已学习过

使用本 skill 的脚本进行判断：

```bash
python3 "<REPO_ROOT>/.qoder/skills/importer/scripts/learn_target.py" check "<REPO_ROOT>" "<github_url>"
```

如果输出 `EXISTS`，说明已经学习过，立即结束，不继续分类，不创建目录。

已学习过时最终只输出：

```markdown
1. GitHub 地址：`<canonical_github_url>`
2. 目标路径：`<已存在学习目录的绝对路径>`（已学习过）
```

### 3. 读取目标仓库 README

如果未学习过，必须先读取目标 GitHub 仓库的 README，再判断分类。这是分类前置条件，不得只凭仓库名、已有记忆、根 `README.md` 样例或 `taxonomy.yaml` 直接分类。

统一使用本 skill 的脚本读取 README。脚本内部按 `api.github.com/repos/<owner>/<repo>/readme` → `raw.githubusercontent.com/<owner>/<repo>/HEAD/`（含常见 README 文件名变体）两级回退，联网对象仅限这两个 GitHub 官方 host；不克隆源码，不抓取 GitHub 页面：

```bash
python3 "<REPO_ROOT>/.qoder/skills/importer/scripts/learn_target.py" readme "<github_url>"
```

这条命令必须原样执行，不要追加 `| head`、`| sed`、`| tail` 或其他 pipeline：README 正文从 stdout 整读，`STATUS` / `WARN` / `META` / `ERROR` 诊断行只出现在 stderr。不要自己拼 `curl` 或 `gh api`；凭据由脚本从环境变量 `GH_TOKEN` / `GITHUB_TOKEN` 自行读取，命令行里不得出现 token、`Authorization`、`echo $GH_TOKEN`、`env | grep TOKEN`。

按脚本的退出码分支处理：

- `0`：stdout 即 README 正文，继续第 4 步。`token_source=anonymous` 属正常降级，不要因为没有 token 就停止；`WARN TOKEN_INVALID` 表示环境变量里的 token 已失效，属运维问题，不要因此停止，也不要写进最终两行输出。
- `2`：URL 无效，或仓库不存在 / 不可访问（可能为私有仓库）。停止，向用户转述 stderr 里的 `ERROR` 行，不要输出猜测分类或目标路径。
- `3`：两级都失败（网络故障或限流）。停止，转述 stderr 最后一条 `ERROR` 的原因与 URL，不要输出猜测分类。
- `4`：仓库存在但没有 README。改用 stderr 里的 `META` 行（`description` / `topics` / `language` / `default_branch`）继续第 4 步分类，仍然不得只凭仓库名分类。
- `5`：取回内容疑似错误页。停止并转述 stderr 的 `ERROR`。

只需要读取 README，不做深度源码分析。

从目标 README（或退出码 `4` 时的 `META` 行）中提取：

- 项目一句话定位。
- 核心功能和主要使用者。
- 是否以 AI / LLM / Agent 为核心价值。
- 技术栈和运行形态，例如 SDK、CLI、Web app、desktop client、infra service、resource collection。
- README 中出现的 topics、badges、安装/使用方式和典型场景。

### 4. 按 taxonomy 判断目标分类目录

拿目标仓库 README 信息对照 `taxonomy.yaml` 判断分类：

- 优先使用 `taxonomy.yaml` 的 `include` / `exclude` / `examples`。
- 如果 `taxonomy.yaml` 信息不足，再对照根 `README.md` 中的领域、分类、已有项目样例。
- 最后只核对最终目标目录是否真实存在。

目标路径必须是分类父目录的绝对路径，其中 `<REPO_ROOT>` 是「必读上下文」里 `git rev-parse --show-toplevel` 得到的绝对路径：

```text
<REPO_ROOT>/ai/coding-tool
```

不要提前创建最终 `<owner>-<repo_name>-learn` 学习目录；本 skill 只输出分类父目录。

### 5. 现有分类不满足时

如果 `taxonomy.yaml` 中没有任何现有分类能合理容纳该项目，就提出一个新分类目录。

新分类要求：

- slug 使用 lower-kebab-case。
- label 使用简洁中文。
- path 指分类目录相对仓库根的位置，固定写成 `domain/category`，例如 `dev-tools/security`，不要带前导 `/`，也不要用 `<REPO_ROOT>` 拼接。
- 说明为什么现有分类不合适，以及新分类适合收纳什么项目。

只有第 7 步输出给用户的目标路径才使用绝对路径，例如 `<REPO_ROOT>/dev-tools/security`。`taxonomy.yaml` 里写绝对路径会让 `validate_index.py` 的 `path:` 正则匹配失败，直接报 `missing-taxonomy-category`。

### 6. 确认并按需创建分类目录

判断出分类目录后，必须用命令显式确认目录是否存在：

```bash
test -d "<absolute_category_path>" && echo "EXISTS_DIR <absolute_category_path>" || echo "MISSING_DIR <absolute_category_path>"
```

按输出分支处理，不要跳过检测直接 `mkdir`：

- `EXISTS_DIR`：不创建目录，最终输出标注 `（已存在分类目录）`。
- `MISSING_DIR`：用下面的命令创建目录，最终输出标注 `（已创建分类目录）`。

```bash
mkdir -p "<absolute_category_path>"
```

创建后同步更新 `taxonomy.yaml`：补充该分类的 `label`、`path`、`include`、`exclude`（如有）和 `examples`（可为空），并把顶层 `last_updated` 更新为当天日期（`YYYY-MM-DD`）。`path` 写相对路径 `domain/category`，不带前导 `/`。

分类条目的缩进层级、以及 `validate_index.py` 对 `path:` 的匹配行为，以 `.qoder/skills/indexer/SKILL.md` 第 4 步为唯一规范来源。写入前先读该节，不要凭记忆缩进。

本 skill 不修改根 `README.md`。

### 7. 最终输出

成功判断后，最终输出只使用两行编号格式。最终回答必须直接从 `1.` 开始，不能在两行之前或之后追加任何解释性文字、分类理由、验证表格、备注或后续说明：

```markdown
1. GitHub 地址：`<canonical_github_url>`
2. 目标路径：`<absolute_path>`<可选状态说明>
```

状态说明只允许使用这几种简短括号：

- `（已学习过）`
- `（已存在分类目录）`
- `（已创建分类目录）`
