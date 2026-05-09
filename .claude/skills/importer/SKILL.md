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

`REPO_ROOT` 使用此命令获取：

```bash
git rev-parse --show-toplevel
```

## 工作流程

### 1. 解析 GitHub URL

使用本 skill 的脚本解析 `owner`、`repo_name`、标准 GitHub URL 和学习目录名：

```bash
python3 "$REPO_ROOT/.claude/skills/importer/scripts/learn_target.py" parse "$GITHUB_URL"
```

学习目录名固定为：

```text
<owner>-<repo_name>-learn
```

### 2. 判断是否已学习过

使用本 skill 的脚本进行判断：

```bash
python3 "$REPO_ROOT/.claude/skills/importer/scripts/learn_target.py" check "$REPO_ROOT" "$GITHUB_URL"
```

如果输出 `EXISTS`，说明已经学习过，立即结束，不继续分类，不创建目录。

已学习过时最终只输出：

```markdown
1. GitHub 地址：`<canonical_github_url>`
2. 目标路径：`<已存在学习目录的绝对路径>`（已学习过）
```

### 3. 读取目标仓库 README

如果未学习过，必须先读取目标 GitHub 仓库的 README，再判断分类。这是分类前置条件，不得只凭仓库名、已有记忆、根 `README.md` 样例或 `taxonomy.yaml` 直接分类。

固定使用 `raw.githubusercontent.com` 的 `HEAD` 引用获取完整 README 内容，不使用 GitHub REST API、GitHub 页面、`gh repo view` 或临时 clone：

```bash
curl -fsSL "https://raw.githubusercontent.com/<owner>/<repo_name>/HEAD/README.md"
```

这条命令必须原样执行，不要追加 `| head`、`| sed`、`| tail` 或其他 pipeline。`HEAD` 会跟随仓库默认分支，避免猜 `main` / `master`。如果 `curl` 失败，立即停止，不要输出猜测分类。只需要读取 README，不做深度源码分析。

进入下一步分类前，必须已经获得目标 README 的实际内容片段或等价 metadata 输出。如果 README 获取失败，停止流程并简短说明无法读取目标 README；不要输出猜测的目标路径。

从目标 README 中提取：

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

目标路径必须是分类父目录的绝对路径，例如：

```text
/Users/crazy/own_project/opensource_learn/ai/coding-tool
```

不要提前创建最终 `<owner>-<repo_name>-learn` 学习目录；本 skill 只输出分类父目录。

### 5. 现有分类不满足时

如果 `taxonomy.yaml` 中没有任何现有分类能合理容纳该项目，就提出一个新分类目录。

新分类要求：

- slug 使用 lower-kebab-case。
- label 使用简洁中文。
- path 必须是绝对路径，例如 `/Users/crazy/own_project/opensource_learn/dev-tools/security`。
- 说明为什么现有分类不合适，以及新分类适合收纳什么项目。

### 6. 目录不存在时

判断出分类目录后，必须用命令显式确认目录是否存在：

```bash
test -d "<absolute_category_path>" && echo "EXISTS_DIR <absolute_category_path>" || echo "MISSING_DIR <absolute_category_path>"
```

只有看到 `EXISTS_DIR`，最终输出才可以标注 `（已存在分类目录）`。

如果判断出的分类目录不存在，直接创建：

```bash
mkdir -p "<absolute_category_path>"
```

如果看到 `MISSING_DIR`，再创建分类目录；创建后也要同步更新 `taxonomy.yaml`，补充该分类的 `label`、`path`、`include`、`exclude`（如有）和 `examples`（可为空）。
- 不修改根 `README.md`。

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
