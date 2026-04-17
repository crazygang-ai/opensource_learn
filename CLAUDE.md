# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 仓库性质

这是一个 **纯文档知识库**，而不是可执行代码项目：

- 没有构建系统、测试框架、包管理器或 lint 配置
- 内容为 128+ 个开源项目的源码阅读笔记，每个项目一个独立的 `*_learn/` 子目录，内部仅包含一个 `README.md`
- 所有笔记使用 **中文** 撰写，技术术语、专有名词、代码标识符保留英文原文（继承自 `/Users/crazy/own_project/.claude/CLAUDE.md`）
- 根 `README.md` 是一个按 领域 → 分类 → 项目 组织的索引表格，链接到各子目录

## 目录组织

顶层分为两个领域：

- `ai/` —— 按子分类组织：`agent-framework`、`agent-system`、`app-platform`、`client`、`coding-tool`、`finance`、`infra`、`multimedia`、`resource`
- `dev-tools/` —— 按子分类组织：`frontend`、`infra`、`multimedia`、`networking`、`browser-extension`、`security`、`resource`、`productivity`

路径约定：`<领域>/<分类>/<项目名>_learn/README.md`。新增项目时必须遵循此约定，并在根 `README.md` 索引表格的对应分类中插入新行（注意调整该分类首行的 `rowspan`）。

## 笔记模板

每个 `*_learn/README.md` 遵循统一结构。新增或编辑笔记时应保持一致：

1. **标题** + 仓库地址链接 + 学习日期（绝对日期，如 `2026-04-17`）
2. `> **以下为 AI 源码分析**` 引用块，包含：
   - **一句话概括**
   - **要点速览**（核心模块 / 职责 / 关键文件 三列表格）
3. **项目简介** —— 定位与背景
4. **技术栈** —— 类别 / 技术 两列表格
5. **目录结构** —— 带行内注释的源码目录树
6. **架构设计** —— 分层说明，常配 Mermaid 图
7. 视项目而定的扩展章节（集成点、MCP、插件、部署等）

## 常见工作流

典型任务是"为某个开源项目新增一篇学习笔记"：

1. 在 `<领域>/<分类>/` 下创建 `<项目名>_learn/` 目录
2. 在其中创建 `README.md`，遵循上述模板
3. 在根 `README.md` 的对应分类表格行中插入条目，调整 `rowspan`
4. commit message 风格参考最近提交，形如：`Add N new learning notes and update README` 或 `Add <项目> learning note and update README`

注意 `.gitignore` 已忽略 `.DS_Store` 和 `.claude`，不要手动提交这些文件。

## 约束

- 笔记内容以中文为主，保留技术术语英文原文
- 不要在子目录中放置源码或构建产物 —— 这个仓库只存放 Markdown 学习笔记
- 根 `README.md` 的表格结构依赖 HTML `<table>` + `rowspan`，编辑时务必让 `rowspan` 数值与实际行数一致
