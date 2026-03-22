# Open Source Learn

> 开源项目源码学习与架构分析笔记集

本仓库是一个系统化的开源项目学习知识库，针对每个项目进行源码阅读、架构分析和技术总结。目前涵盖 AI 领域，后续会扩展到更多技术方向。

## 项目列表

| 领域 | 分类 | 项目 | 简介 |
| --- | --- | --- | --- |
| AI | Agent 框架 | [A2A](./ai/agent-framework/A2A_learn) | Google Agent2Agent 开放协议，定义 AI Agent 间通信与协作标准 |
| | | [AutoGen](./ai/agent-framework/autogen_learn) | 微软多 Agent 框架，基于 Actor 模型的消息驱动代理系统 |
| | | [DeerFlow](./ai/agent-framework/deer-flow_learn) | 字节跳动基于 LangGraph 的 Agent 编排框架，支持子代理委派与沙箱执行 |
| | | [LangChain](./ai/agent-framework/langchain_learn) | LLM Agent 框架，通过 Runnable 接口和 LCEL 实现声明式组件编排 |
| | | [MetaGPT](./ai/agent-framework/MetaGPT_learn) | 多智能体协作框架，模拟软件公司 SOP 完成从需求到代码的全流程 |
| | | [nanobot](./ai/agent-framework/nanobot_learn) | 超轻量个人 AI 助手框架，完整 Agent Loop + 多平台对接 |
| | | [openai-agents-python](./ai/agent-framework/openai-agents-python_learn) | OpenAI 官方轻量级多 Agent 编排 SDK |
| | | [Vanna](./ai/agent-framework/vanna_learn) | User-Aware LLM Agent 框架，自然语言转 SQL 并流式返回富 UI 组件 |
| | Agent 系统 | [OpenClaw](./ai/agent-system/openclaw_learn) | 自托管个人 AI 助手网关，统一接入 20+ 消息通道 |
| | | [OpenFang](./ai/agent-system/openfang_learn) | Rust 编写的 Agent Operating System，14 个模块化 crate |
| | | [OpenViking](./ai/agent-system/OpenViking_learn) | 字节跳动 Agent 上下文数据库，文件系统范式管理记忆、资源和技能 |
| | | [ZeroClaw](./ai/agent-system/zeroclaw_learn) | 纯 Rust 个人 AI 助手，41+ 消息渠道、19+ LLM Provider、80+ 工具 |
| | 应用平台 | [Dify](./ai/app-platform/dify_learn) | 开源 LLM 应用开发平台，可视化 Workflow + RAG + Agent + 插件系统 |
| | | [Langflow](./ai/app-platform/langflow_learn) | 可视化 AI 工作流编排平台，拖拽构建 LLM Agent 和 RAG 流程 |
| | | [n8n](./ai/app-platform/n8n_learn) | 开源工作流自动化平台，400+ 集成连接器 + LangChain AI 节点 |
| | | [RAGFlow](./ai/app-platform/ragflow_learn) | 基于深度文档理解的 RAG 引擎，融合 Agent 编排能力 |
| | 编程工具 | [CLI-Anything](./ai/coding-tool/CLI-Anything_learn) | 将任意 GUI 应用自动转换为 AI Agent 可操作的命令行接口 |
| | | [claude-mem](./ai/coding-tool/claude-mem_learn) | Claude Code 持久化记忆压缩系统，通过 Hooks 实现跨会话知识连续性 |
| | | [gws cli](./ai/coding-tool/cli_learn) | Rust 编写的 Google Workspace 动态 CLI，运行时生成命令 + 100+ Agent Skills |
| | | [Context7](./ai/coding-tool/context7_learn) | 为 AI 编程助手提供实时、版本准确的库文档和代码示例 |
| | | [Everything Claude Code](./ai/coding-tool/everything-claude-code_learn) | AI Agent 编码工具性能优化系统，28 个 Agent + 116 个 Skill |
| | | [OpenHands](./ai/coding-tool/OpenHands_learn) | AI 驱动的软件开发平台，从 issue 到 pull request 全自动化 |
| | | [OpenCode](./ai/coding-tool/opencode_learn) | 100% 开源终端 AI 编程助手，不绑定任何 AI 供应商 |
| | | [spec-kit](./ai/coding-tool/spec-kit_learn) | GitHub 官方 Spec-Driven Development 工具包，需求规格驱动 AI 生成代码 |
| | | [Superpowers](./ai/coding-tool/superpowers_learn) | AI 编程代理工作流框架，14 个可组合 Skills 覆盖全开发流程 |
| | 客户端 | [AnythingLLM](./ai/client/anything-llm_learn) | 全功能私有化 AI 应用平台，支持 37+ LLM 提供商和 10+ 向量数据库 |
| | | [Chatbox](./ai/client/chatbox_learn) | 跨平台 AI 聊天桌面客户端，插件化接入 20+ LLM 服务商 |
| | | [Cherry Studio](./ai/client/cherry-studio_learn) | Electron 跨平台 AI 桌面客户端，支持 MCP 协议和知识库 RAG |
| | | [Open WebUI](./ai/client/open-webui_learn) | 自托管 AI 平台，类 ChatGPT Web 界面，支持 Ollama/OpenAI 等多后端 |
| | | [Quotio](./ai/client/quotio_learn) | macOS 原生应用，集中管理多 AI Provider 账户、Quota 用量与 Model Fallback |
| | | [World Monitor](./ai/client/worldmonitor_learn) | AI 驱动的实时全球情报仪表盘，聚合 435+ 新闻源与 30+ 数据源 |
| | 基础设施 | [Daytona](./ai/infra/daytona_learn) | 安全弹性的 Sandbox 基础设施平台，亚 90ms 创建隔离沙箱执行 AI 生成代码 |
| | | [Firecrawl](./ai/infra/firecrawl_learn) | 将任意网站转换为 LLM 可消费数据（Markdown/JSON/截图）的 API 服务 |
| | | [OpenSandbox](./ai/infra/OpenSandbox_learn) | 阿里巴巴通用 AI 沙箱平台，多语言 SDK + Docker/K8s 运行时 |
| | | [Ray](./ai/infra/ray_learn) | 统一分布式计算框架，含 Data/Train/Serve/Tune/RLlib 等 AI 库生态 |
| | 金融 | [daily_stock_analysis](./ai/finance/daily_stock_analysis_learn) | 基于 AI 大模型的 A股/港股/美股自选股智能分析与多渠道推送系统 |
| | | [OpenBB](./ai/finance/OpenBB_learn) | 开源金融数据平台，插件化对接 30+ 数据源，支持 MCP Server |
| | | [Qlib](./ai/finance/qlib_learn) | 微软 AI 驱动量化投资平台，覆盖数据、因子、模型、回测全链路 |
| | 多媒体 | [Deep-Live-Cam](./ai/multimedia/Deep-Live-Cam_learn) | 基于 InsightFace 的实时人脸替换工具，单张图片即可换脸 |
| | | [MockingBird](./ai/multimedia/MockingBird_learn) | 基于 SV2TTS 的中文实时语音克隆系统，few-shot 语音克隆 |
| | 学习资料 | [system-prompts-and-models-of-ai-tools](./ai/resource/system-prompts-and-models-of-ai-tools_learn) | 30+ AI 工具的 System Prompt 与 Tool 定义收集库 |

## 笔记内容

每个子目录通常包含：

- **项目一句话介绍** — 快速了解项目定位
- **核心要点概览** — 关键模块与职责划分
- **技术栈分析** — 使用的语言、框架和工具
- **目录结构注解** — 带说明的源码目录树
- **架构设计解析** — 核心架构模式与设计哲学
- **集成与扩展点** — MCP、插件系统等

## License

[MIT](./LICENSE)
