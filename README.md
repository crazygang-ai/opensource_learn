# Open Source Learn

> 开源项目源码学习与架构分析笔记集

本仓库是一个系统化的开源项目学习知识库，针对每个项目进行源码阅读、架构分析和技术总结。目前涵盖 AI 和开发工具两大领域，后续会扩展到更多技术方向。

## 项目列表

<table>
<tr>
  <th>领域</th>
  <th>分类</th>
  <th>项目</th>
  <th>简介</th>
</tr>
<tr>
  <td rowspan="99"><b>AI</b></td>
  <td rowspan="11">Agent 框架</td>
  <td><a href="./ai/agent-framework/A2A_learn">A2A</a></td>
  <td>Google Agent2Agent 开放协议，定义 AI Agent 间通信与协作标准</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/autogen_learn">AutoGen</a></td>
  <td>微软多 Agent 框架，基于 Actor 模型的消息驱动代理系统</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/deepagents_learn">Deep Agents</a></td>
  <td>LangChain 团队的 Agent 框架，基于 LangGraph 构建，内置规划、Shell 执行和 Sub-agent 等能力</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/deer-flow_learn">DeerFlow</a></td>
  <td>字节跳动基于 LangGraph 的 Agent 编排框架，支持子代理委派与沙箱执行</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/hermes-agent_learn">hermes-agent</a></td>
  <td>Nous Research 自我进化 AI Agent 框架，闭环学习 + 可插拔工具 + 子代理委派</td>
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
  <td><a href="./ai/agent-framework/ruflo_learn">Ruflo</a></td>
  <td>Claude Code 多 Agent 编排框架，100+ 专用 Agent 协同工作与 MCP 集成</td>
</tr>
<tr>
  <td><a href="./ai/agent-framework/vanna_learn">Vanna</a></td>
  <td>User-Aware LLM Agent 框架，自然语言转 SQL 并流式返回富 UI 组件</td>
</tr>
<tr>
  <td rowspan="7">Agent 系统</td>
  <td><a href="./ai/agent-system/DeepTutor_learn">DeepTutor</a></td>
  <td>Agent-Native 个性化 AI 教学平台，两层插件架构 + 多 Agent 协作实现教学全场景</td>
</tr>
<tr>
  <td><a href="./ai/agent-system/MiroFish_learn">MiroFish</a></td>
  <td>多 Agent 群体智能预测引擎，通过知识图谱和社交平台模拟生成预测报告</td>
</tr>
<tr>
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
  <td><a href="./ai/agent-system/pentagi_learn">PentAGI</a></td>
  <td>Multi-Agent 自主渗透测试系统，LLM 驱动 Agent 团队在隔离容器中执行安全测试</td>
</tr>
<tr>
  <td><a href="./ai/agent-system/zeroclaw_learn">ZeroClaw</a></td>
  <td>纯 Rust 个人 AI 助手，41+ 消息渠道、19+ LLM Provider、80+ 工具</td>
</tr>
<tr>
  <td rowspan="6">应用平台</td>
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
  <td><a href="./ai/app-platform/onyx_learn">Onyx</a></td>
  <td>开源 AI 应用平台，集成 Agentic RAG、深度研究、50+ 数据源连接器和 MCP 协议</td>
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
  <td rowspan="23">编程工具</td>
  <td><a href="./ai/coding-tool/Archon_learn">Archon</a></td>
  <td>开源 AI 编码工作流引擎，YAML DAG 定义开发流程，多平台驱动 AI 编码代理</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/cc-switch_learn">CC Switch</a></td>
  <td>五款 AI 编程 CLI 的统一 Provider 管理与一键切换跨平台桌面应用</td>
</tr>
<tr>
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
  <td><a href="./ai/coding-tool/cmux_learn">cmux</a></td>
  <td>基于 Ghostty 的原生 macOS 终端应用，专为 AI coding agent 并行工作设计</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/codex_learn">Codex CLI</a></td>
  <td>OpenAI 本地 AI 编程助手，沙箱化命令执行实现安全自主编码</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/context7_learn">Context7</a></td>
  <td>为 AI 编程助手提供实时、版本准确的库文档和代码示例</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/context-hub_learn">Context Hub</a></td>
  <td>为 AI 编程 Agent 提供精选版本化 API 文档和技能检索服务</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/everything-claude-code_learn">Everything Claude Code</a></td>
  <td>AI Agent 编码工具性能优化系统，28 个 Agent + 116 个 Skill</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/get-shit-done_learn">GSD</a></td>
  <td>轻量级元提示与上下文工程框架，解决 AI 编码代理的上下文衰变问题</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/gstack_learn">gstack</a></td>
  <td>基于 Markdown skill 的 AI 工程工作流框架，23 个专家角色覆盖完整 sprint 流程</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/GitNexus_learn">GitNexus</a></td>
  <td>将代码库索引为知识图谱，通过 MCP 协议为 AI Agent 提供深度代码感知</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/last30days-skill_learn">last30days-skill</a></td>
  <td>Claude Code / Gemini CLI Skill，跨 10+ 社交平台并行搜索生成结构化研究报告</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/multica_learn">multica</a></td>
  <td>AI Agent 管理平台，编码 Agent 在看板上领取任务、自主执行、积累 Skill</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/oh-my-claudecode_learn">oh-my-claudecode</a></td>
  <td>Claude Code 多智能体编排系统，19 个专业化代理实现零配置并行任务执行</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/oh-my-codex_learn">oh-my-codex</a></td>
  <td>Codex CLI 多 Agent 编排增强层，从需求澄清到并行执行的完整工程工作流</td>
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
  <td><a href="./ai/coding-tool/open-swe_learn">Open SWE</a></td>
  <td>基于 LangGraph 的开源编程 Agent 框架，支持多渠道触发和沙箱执行</td>
</tr>
<tr>
  <td><a href="./ai/coding-tool/OpenSpec_learn">OpenSpec</a></td>
  <td>AI 原生 spec-driven 开发框架，人类和 AI 在写代码前先对齐需求</td>
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
  <td rowspan="9">客户端</td>
  <td><a href="./ai/client/gallery_learn">AI Edge Gallery</a></td>
  <td>Google 官方 Android 端侧 AI 应用，本地离线运行 LLM 进行对话、图片理解和 Agent Skills</td>
</tr>
<tr>
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
  <td><a href="./ai/client/project-nomad_learn">Project N.O.M.A.D.</a></td>
  <td>自托管离线优先知识与教育服务器，集成 Ollama 聊天、离线百科、地图等多服务</td>
</tr>
<tr>
  <td><a href="./ai/client/quotio_learn">Quotio</a></td>
  <td>macOS 原生应用，集中管理多 AI Provider 账户、Quota 用量与 Model Fallback</td>
</tr>
<tr>
  <td><a href="./ai/client/waveterm_learn">Wave Terminal</a></td>
  <td>开源 AI 原生终端，Electron + Go 双进程架构，Block 化 UI 统一终端与 AI 对话</td>
</tr>
<tr>
  <td><a href="./ai/client/worldmonitor_learn">World Monitor</a></td>
  <td>AI 驱动的实时全球情报仪表盘，聚合 435+ 新闻源与 30+ 数据源</td>
</tr>
<tr>
  <td rowspan="18">基础设施</td>
  <td><a href="./ai/infra/autoresearch_learn">autoresearch</a></td>
  <td>Karpathy 的自主研究框架，AI Agent 在固定时间预算内自主迭代 LLM 训练实验</td>
</tr>
<tr>
  <td><a href="./ai/infra/BitNet_learn">BitNet</a></td>
  <td>微软 1-bit LLM 推理框架，基于 llama.cpp，三值权重模型快速无损推理</td>
</tr>
<tr>
  <td><a href="./ai/infra/browser_learn">Lightpanda Browser</a></td>
  <td>Zig 编写的无头浏览器，专为 AI agent 设计，内存占用为 Chrome 的 1/16</td>
</tr>
<tr>
  <td><a href="./ai/infra/chrome-devtools-mcp_learn">chrome-devtools-mcp</a></td>
  <td>MCP Server，让 AI 编程助手通过 CDP 协议控制和调试 Chrome 浏览器</td>
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
  <td><a href="./ai/infra/hindsight_learn">hindsight</a></td>
  <td>仿生记忆架构的 AI Agent 记忆系统，PostgreSQL + pgvector 多维记忆存储与检索</td>
</tr>
<tr>
  <td><a href="./ai/infra/LocalAI_learn">LocalAI</a></td>
  <td>开源本地 AI 推理引擎，兼容 OpenAI API，35+ 后端，支持 CPU/GPU 和分布式部署</td>
</tr>
<tr>
  <td><a href="./ai/infra/markitdown_learn">MarkItDown</a></td>
  <td>微软多格式文件转 Markdown 工具，支持 PDF/Word/Excel 等 18+ 种格式，专为 LLM 设计</td>
</tr>
<tr>
  <td><a href="./ai/infra/new-api_learn">new-api</a></td>
  <td>下一代 LLM 网关，统一代理 30+ 家 AI 供应商 API，智能路由与计费管理</td>
</tr>
<tr>
  <td><a href="./ai/infra/one-api_learn">one-api</a></td>
  <td>开源 AI 模型 API 网关，标准 OpenAI 格式代理所有主流大模型，内置计费与负载均衡</td>
</tr>
<tr>
  <td><a href="./ai/infra/OpenSandbox_learn">OpenSandbox</a></td>
  <td>阿里巴巴通用 AI 沙箱平台，多语言 SDK + Docker/K8s 运行时</td>
</tr>
<tr>
  <td><a href="./ai/infra/promptfoo_learn">promptfoo</a></td>
  <td>LLM 评估与红队测试工具，自动化 prompt 评估、模型对比和安全漏洞扫描</td>
</tr>
<tr>
  <td><a href="./ai/infra/ray_learn">Ray</a></td>
  <td>统一分布式计算框架，含 Data/Train/Serve/Tune/RLlib 等 AI 库生态</td>
</tr>
<tr>
  <td><a href="./ai/infra/RuView_learn">RuView</a></td>
  <td>基于 WiFi CSI 信号的感知平台，穿墙人体检测、姿态估计和生命体征监测</td>
</tr>
<tr>
  <td><a href="./ai/infra/sub2api_learn">sub2api</a></td>
  <td>AI API 网关平台，将订阅配额转化为标准 API Key 分发，多账号调度与负载均衡</td>
</tr>
<tr>
  <td><a href="./ai/infra/supermemory_learn">supermemory</a></td>
  <td>AI 应用记忆与上下文平台，跨会话事实提取、混合检索与遗忘策略</td>
</tr>
<tr>
  <td><a href="./ai/infra/unsloth_learn">unsloth</a></td>
  <td>高性能 LLM 微调框架，自研 Triton kernel 实现 2 倍加速和 70% 显存节省</td>
</tr>
<tr>
  <td rowspan="7">金融</td>
  <td><a href="./ai/finance/ai-hedge-fund_learn">ai-hedge-fund</a></td>
  <td>基于 LangGraph 多 Agent 的 AI 对冲基金系统，模拟 18 位投资大师生成交易决策</td>
</tr>
<tr>
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
  <td><a href="./ai/finance/timesfm_learn">TimesFM</a></td>
  <td>Google 时间序列基础模型，decoder-only Transformer 架构，支持零样本预测</td>
</tr>
<tr>
  <td><a href="./ai/finance/TradingAgents_learn">TradingAgents</a></td>
  <td>LangGraph 多 Agent 金融交易框架，模拟多空辩论与风控生成投资建议</td>
</tr>
<tr>
  <td><a href="./ai/finance/TradingAgents-CN_learn">TradingAgents-CN</a></td>
  <td>基于 LangGraph 的中文多智能体股票分析平台，多角色协作辩论输出投资建议</td>
</tr>
<tr>
  <td rowspan="8">多媒体</td>
  <td><a href="./ai/multimedia/Deep-Live-Cam_learn">Deep-Live-Cam</a></td>
  <td>基于 InsightFace 的实时人脸替换工具，单张图片即可换脸</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/fish-speech_learn">fish-speech</a></td>
  <td>Fish Audio 多语言 TTS 系统，Dual-AR 架构，80+ 语言和快速语音克隆</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/MockingBird_learn">MockingBird</a></td>
  <td>基于 SV2TTS 的中文实时语音克隆系统，few-shot 语音克隆</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/ml-sharp_learn">SHARP</a></td>
  <td>Apple 单照片 3D Gaussian Splatting，一次前馈推理（< 1 秒）实现实时新视角合成</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/MoneyPrinterTurbo_learn">MoneyPrinterTurbo</a></td>
  <td>输入主题由 LLM 写稿、拉取素材、TTS 配音、字幕合成，全自动生成短视频</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/MoneyPrinterV2_learn">MoneyPrinterV2</a></td>
  <td>Ollama + Selenium 自动化变现工具，覆盖 YouTube Shorts 生成、Twitter 发帖、联盟营销等</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/supervision_learn">supervision</a></td>
  <td>Roboflow 计算机视觉工具库，统一检测数据结构、可视化注解和多目标追踪</td>
</tr>
<tr>
  <td><a href="./ai/multimedia/VibeVoice_learn">VibeVoice</a></td>
  <td>微软语音 AI 模型家族，支持长达 90 分钟 TTS 和 60 分钟 ASR</td>
</tr>
<tr>
  <td rowspan="10">学习资料</td>
  <td><a href="./ai/resource/agency-agents_learn">agency-agents</a></td>
  <td>AI Agent 人格集合，150+ 专业化 Agent 提示词模板，支持 11 种 AI 编码工具</td>
</tr>
<tr>
  <td><a href="./ai/resource/andrej-karpathy-skills_learn">andrej-karpathy-skills</a></td>
  <td>Claude Code 行为准则插件，基于 Karpathy 对 LLM 编码缺陷的观察提炼四条行为原则</td>
</tr>
<tr>
  <td><a href="./ai/resource/claude-howto_learn">claude-howto</a></td>
  <td>Claude Code 全功能教学指南，10 大模块 117+ 功能点，从入门到精通</td>
</tr>
<tr>
  <td><a href="./ai/resource/impeccable_learn">impeccable</a></td>
  <td>跨 AI 编码工具的前端设计 skill 分发系统，统一源格式转换为 11 个 provider 专属格式</td>
</tr>
<tr>
  <td><a href="./ai/resource/learn-claude-code_learn">learn-claude-code</a></td>
  <td>渐进式拆解 Claude Code Agent 内部机制的教学项目，12 个 Python 实现 + Web 平台</td>
</tr>
<tr>
  <td><a href="./ai/resource/marketingskills_learn">marketingskills</a></td>
  <td>AI Agent 营销技能知识库，33 个技能文件和 60+ CLI 工具，覆盖 CRO、SEO 等</td>
</tr>
<tr>
  <td><a href="./ai/resource/minimind_learn">minimind</a></td>
  <td>从零训练超小 LLM 全流程项目，覆盖预训练、SFT、LoRA、DPO、RLHF 等</td>
</tr>
<tr>
  <td><a href="./ai/resource/notebooklm-py_learn">notebooklm-py</a></td>
  <td>逆向工程 Google NotebookLM RPC 协议的非官方 Python API 客户端</td>
</tr>
<tr>
  <td><a href="./ai/resource/skills_learn">skills</a></td>
  <td>开源 Claude Code Agent Skills 集合，覆盖 TDD、架构改进到 GitHub 工作流</td>
</tr>
<tr>
  <td><a href="./ai/resource/system-prompts-and-models-of-ai-tools_learn">system-prompts-and-models-of-ai-tools</a></td>
  <td>30+ AI 工具的 System Prompt 与 Tool 定义收集库</td>
</tr>
<tr>
  <td rowspan="20"><b>开发工具</b></td>
  <td rowspan="1">前端</td>
  <td><a href="./dev-tools/frontend/ui_learn">shadcn/ui</a></td>
  <td>基于 Radix UI 和 Tailwind CSS 的组件集合，CLI 工具将源码直接复制到项目中</td>
</tr>
<tr>
  <td rowspan="5">基础设施</td>
  <td><a href="./dev-tools/infra/dolt_learn">Dolt</a></td>
  <td>MySQL 兼容数据库，基于 Prolly Tree 存储引擎提供 Git 级别版本控制能力</td>
</tr>
<tr>
  <td><a href="./dev-tools/infra/harness_learn">Harness</a></td>
  <td>集代码托管、CI/CD Pipeline、云开发环境和制品仓库于一体的开源 DevOps 平台</td>
</tr>
<tr>
  <td><a href="./dev-tools/infra/neko_learn">neko</a></td>
  <td>基于 Docker + WebRTC 的自托管虚拟浏览器/远程桌面，支持多人协作</td>
</tr>
<tr>
  <td><a href="./dev-tools/infra/open-im-server_learn">open-im-server</a></td>
  <td>Go 微服务架构的开源即时通讯服务端，Kafka 异步解耦消息投递</td>
</tr>
<tr>
  <td><a href="./dev-tools/infra/uv_learn">uv</a></td>
  <td>Rust 编写的超高性能 Python 包管理器，替代 pip/poetry，速度快 10-100 倍</td>
</tr>
<tr>
  <td rowspan="3">多媒体</td>
  <td><a href="./dev-tools/multimedia/arnis_learn">Arnis</a></td>
  <td>Rust 编写，将真实地理数据（OSM + 高程 + 卫星）转换为 Minecraft 世界</td>
</tr>
<tr>
  <td><a href="./dev-tools/multimedia/iina_learn">IINA</a></td>
  <td>基于 mpv 的现代 macOS 视频播放器，Swift 原生 UI + JavaScript 插件系统</td>
</tr>
<tr>
  <td><a href="./dev-tools/multimedia/openscreen_learn">OpenScreen</a></td>
  <td>Electron + React + PixiJS 开源屏幕录制与视频编辑桌面应用</td>
</tr>
<tr>
  <td rowspan="1">网络</td>
  <td><a href="./dev-tools/networking/sing-box_learn">sing-box</a></td>
  <td>Go 编写的通用代理平台，模块化架构支持 25+ 种代理协议的统一调度与路由</td>
</tr>
<tr>
  <td rowspan="1">浏览器扩展</td>
  <td><a href="./dev-tools/browser-extension/github-chinese_learn">github-chinese</a></td>
  <td>Tampermonkey 用户脚本，MutationObserver 实时翻译 GitHub 界面为中文</td>
</tr>
<tr>
  <td rowspan="2">安全</td>
  <td><a href="./dev-tools/security/katana_learn">katana</a></td>
  <td>ProjectDiscovery 下一代 Web 爬虫框架，三种爬取模式，专为安全自动化设计</td>
</tr>
<tr>
  <td><a href="./dev-tools/security/sherlock_learn">Sherlock</a></td>
  <td>OSINT 工具，并发搜索 400+ 社交网络上的用户名是否存在</td>
</tr>
<tr>
  <td rowspan="1">资源</td>
  <td><a href="./dev-tools/resource/awesome-mac_learn">awesome-mac</a></td>
  <td>社区驱动的 macOS 优质应用收录清单，自动化构建发布为网站与 npm 包</td>
</tr>
<tr>
  <td rowspan="6">效率工具</td>
  <td><a href="./dev-tools/productivity/atuin_learn">Atuin</a></td>
  <td>Rust 编写的 shell 历史管理工具，SQLite 存储 + 端到端加密跨机器同步</td>
</tr>
<tr>
  <td><a href="./dev-tools/productivity/drawio-desktop_learn">drawio-desktop</a></td>
  <td>基于 Electron 的桌面绘图应用，draw.io 核心编辑器的本地封装</td>
</tr>
<tr>
  <td><a href="./dev-tools/productivity/Ice_learn">Ice</a></td>
  <td>macOS 菜单栏管理工具，隐藏/显示/分组管理菜单栏图标</td>
</tr>
<tr>
  <td><a href="./dev-tools/productivity/starship_learn">Starship</a></td>
  <td>Rust 编写的极速跨 shell prompt 生成器，模块化插件架构与并行计算</td>
</tr>
<tr>
  <td><a href="./dev-tools/productivity/yazi_learn">Yazi</a></td>
  <td>Rust 编写的高性能异步终端文件管理器，tokio 运行时 + Lua 插件系统</td>
</tr>
<tr>
  <td><a href="./dev-tools/productivity/zellij_learn">Zellij</a></td>
  <td>Rust 编写的终端多路复用器，WebAssembly 插件系统实现可扩展 UI</td>
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
