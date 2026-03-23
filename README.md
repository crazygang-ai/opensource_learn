# Open Source Learn

> 开源项目源码学习与架构分析笔记集

本仓库是一个系统化的开源项目学习知识库，针对每个项目进行源码阅读、架构分析和技术总结。目前涵盖 AI 领域，后续会扩展到更多技术方向。

## 项目列表

<table>
<tr>
  <th>领域</th>
  <th>分类</th>
  <th>项目</th>
  <th>简介</th>
</tr>
<tr>
  <td rowspan="43"><b>AI</b></td>
  <td rowspan="8">Agent 框架</td>
  <td><a href="./ai/agent-framework/A2A_learn">A2A</a></td>
  <td>Google Agent2Agent 开放协议，定义 AI Agent 间通信与协作标准</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/autogen_learn">AutoGen</a></td>
  <td>微软多 Agent 框架，基于 Actor 模型的消息驱动代理系统</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/deer-flow_learn">DeerFlow</a></td>
  <td>字节跳动基于 LangGraph 的 Agent 编排框架，支持子代理委派与沙箱执行</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/langchain_learn">LangChain</a></td>
  <td>LLM Agent 框架，通过 Runnable 接口和 LCEL 实现声明式组件编排</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/MetaGPT_learn">MetaGPT</a></td>
  <td>多智能体协作框架，模拟软件公司 SOP 完成从需求到代码的全流程</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/nanobot_learn">nanobot</a></td>
  <td>超轻量个人 AI 助手框架，完整 Agent Loop + 多平台对接</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/openai-agents-python_learn">openai-agents-python</a></td>
  <td>OpenAI 官方轻量级多 Agent 编排 SDK</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/vanna_learn">Vanna</a></td>
  <td>User-Aware LLM Agent 框架，自然语言转 SQL 并流式返回富 UI 组件</td>
</tr>
<tr>
  <td rowspan="4">Agent 系统</td>
  <td><a href="./ai/agent-system/openclaw_learn">OpenClaw</a></td>
  <td>自托管个人 AI 助手网关，统一接入 20+ 消息通道</td>
</tr>
<tr>
  <td><a href="./ai/agent-system/openfang_learn">OpenFang</a></td>
  <td>Rust 编写的 Agent Operating System，14 个模块化 crate</td>
</tr>
<tr>
  <td><a href="./ai/agent-system/OpenViking_learn">OpenViking</a></td>
  <td>字节跳动 Agent 上下文数据库，文件系统范式管理记忆、资源和技能</td>
</tr>
<tr>
  <td><a href="./ai/agent-system/zeroclaw_learn">ZeroClaw</a></td>
  <td>纯 Rust 个人 AI 助手，41+ 消息渠道、19+ LLM Provider、80+ 工具</td>
</tr>
<tr>
  <td rowspan="5">应用平台</td>
  <td><a href="./ai/app-platform/dify_learn">Dify</a></td>
  <td>开源 LLM 应用开发平台，可视化 Workflow + RAG + Agent + 插件系统</td>
</tr>
<tr>
  <td><a href="./ai/app-platform/langflow_learn">Langflow</a></td>
  <td>可视化 AI 工作流编排平台，拖拽构建 LLM Agent 和 RAG 流程</td>
</tr>
<tr>
  <td><a href="./ai/app-platform/n8n_learn">n8n</a></td>
  <td>开源工作流自动化平台，400+ 集成连接器 + LangChain AI 节点</td>
</tr>
<tr>
  <td><a href="./ai/app-platform/ragflow_learn">RAGFlow</a></td>
  <td>基于深度文档理解的 RAG 引擎，融合 Agent 编排能力</td>
</tr>
<tr>
  <td><a href="./ai/app-platform/youtu-rag_learn">Youtu-RAG</a></td>
  <td>腾讯优图下一代 Agentic RAG 系统，自主决策 + 双层记忆 + 多 Agent 协作</td>
</tr>
<tr>
  <td rowspan="9">编程工具</td>
  <td><a href="./ai/coding-tool/CLI-Anything_learn">CLI-Anything</a></td>
  <td>将任意 GUI 应用自动转换为 AI Agent 可操作的命令行接口</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/claude-mem_learn">claude-mem</a></td>
  <td>Claude Code 持久化记忆压缩系统，通过 Hooks 实现跨会话知识连续性</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/cli_learn">gws cli</a></td>
  <td>Rust 编写的 Google Workspace 动态 CLI，运行时生成命令 + 100+ Agent Skills</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/context7_learn">Context7</a></td>
  <td>为 AI 编程助手提供实时、版本准确的库文档和代码示例</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/everything-claude-code_learn">Everything Claude Code</a></td>
  <td>AI Agent 编码工具性能优化系统，28 个 Agent + 116 个 Skill</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/OpenHands_learn">OpenHands</a></td>
  <td>AI 驱动的软件开发平台，从 issue 到 pull request 全自动化</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/opencode_learn">OpenCode</a></td>
  <td>100% 开源终端 AI 编程助手，不绑定任何 AI 供应商</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/spec-kit_learn">spec-kit</a></td>
  <td>GitHub 官方 Spec-Driven Development 工具包，需求规格驱动 AI 生成代码</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/superpowers_learn">Superpowers</a></td>
  <td>AI 编程代理工作流框架，14 个可组合 Skills 覆盖全开发流程</td>
</tr>
<tr>
  <td rowspan="6">客户端</td>
  <td><a href="./ai/client/anything-llm_learn">AnythingLLM</a></td>
  <td>全功能私有化 AI 应用平台，支持 37+ LLM 提供商和 10+ 向量数据库</td>
</tr>
<tr>
  <td><a href="./ai/client/chatbox_learn">Chatbox</a></td>
  <td>跨平台 AI 聊天桌面客户端，插件化接入 20+ LLM 服务商</td>
</tr>
<tr>
  <td><a href="./ai/client/cherry-studio_learn">Cherry Studio</a></td>
  <td>Electron 跨平台 AI 桌面客户端，支持 MCP 协议和知识库 RAG</td>
</tr>
<tr>
  <td><a href="./ai/client/open-webui_learn">Open WebUI</a></td>
  <td>自托管 AI 平台，类 ChatGPT Web 界面，支持 Ollama/OpenAI 等多后端</td>
</tr>
<tr>
  <td><a href="./ai/client/quotio_learn">Quotio</a></td>
  <td>macOS 原生应用，集中管理多 AI Provider 账户、Quota 用量与 Model Fallback</td>
</tr>
<tr>
  <td><a href="./ai/client/worldmonitor_learn">World Monitor</a></td>
  <td>AI 驱动的实时全球情报仪表盘，聚合 435+ 新闻源与 30+ 数据源</td>
</tr>
<tr>
  <td rowspan="5">基础设施</td>
  <td><a href="./ai/infra/autoresearch_learn">autoresearch</a></td>
  <td>Karpathy 的自主研究框架，AI Agent 在固定时间预算内自主迭代 LLM 训练实验</td>
</tr>
<tr>
  <td><a href="./ai/infra/daytona_learn">Daytona</a></td>
  <td>安全弹性的 Sandbox 基础设施平台，亚 90ms 创建隔离沙箱执行 AI 生成代码</td>
</tr>
<tr>
  <td><a href="./ai/infra/firecrawl_learn">Firecrawl</a></td>
  <td>将任意网站转换为 LLM 可消费数据（Markdown/JSON/截图）的 API 服务</td>
</tr>
<tr>
  <td><a href="./ai/infra/OpenSandbox_learn">OpenSandbox</a></td>
  <td>阿里巴巴通用 AI 沙箱平台，多语言 SDK + Docker/K8s 运行时</td>
</tr>
<tr>
  <td><a href="./ai/infra/ray_learn">Ray</a></td>
  <td>统一分布式计算框架，含 Data/Train/Serve/Tune/RLlib 等 AI 库生态</td>
</tr>
<tr>
  <td rowspan="3">金融</td>
  <td><a href="./ai/finance/daily_stock_analysis_learn">daily_stock_analysis</a></td>
  <td>基于 AI 大模型的 A股/港股/美股自选股智能分析与多渠道推送系统</td>
</tr>
<tr>
  <td><a href="./ai/finance/OpenBB_learn">OpenBB</a></td>
  <td>开源金融数据平台，插件化对接 30+ 数据源，支持 MCP Server</td>
</tr>
<tr>
  <td><a href="./ai/finance/qlib_learn">Qlib</a></td>
  <td>微软 AI 驱动量化投资平台，覆盖数据、因子、模型、回测全链路</td>
</tr>
<tr>
  <td rowspan="2">多媒体</td>
  <td><a href="./ai/multimedia/Deep-Live-Cam_learn">Deep-Live-Cam</a></td>
  <td>基于 InsightFace 的实时人脸替换工具，单张图片即可换脸</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/MockingBird_learn">MockingBird</a></td>
  <td>基于 SV2TTS 的中文实时语音克隆系统，few-shot 语音克隆</td>
</tr>
<tr>
  <td rowspan="1">学习资料</td>
  <td><a href="./ai/resource/system-prompts-and-models-of-ai-tools_learn">system-prompts-and-models-of-ai-tools</a></td>
  <td>30+ AI 工具的 System Prompt 与 Tool 定义收集库</td>
</tr>
</table>

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
