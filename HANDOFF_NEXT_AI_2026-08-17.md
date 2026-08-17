# ClawSkills 项目交接档案

更新日期：2026-08-17

交接对象：下一位负责继续维护、验证或发布 ClawSkills 的 AI

仓库：`D:\Development\ClawSkills\ClawSkills`

GitHub：<https://github.com/EnglandTong/ClawSkills>

## 1. 交接结论

本项目当前已完成一次 Agent Loop / CMS 2.1.1 升级，并已推送到 GitHub `main`。两个独立 Skill 和一个 Bundle Plugin 都已经提交到 ClawHub：

- `agent-loop-engineering`：2.1.1
- `cms-project-governance`：2.1.1
- `@englandtong/ai-engineering-expert`：1.1.1

本次升级的核心是隔离型多子 Agent执行协议，用于减少主 Agent 保留的上下文，而不是无条件增加并发 Agent 数量。

当前 Git 状态：工作树干净，`main` 已推送。

权威提交：

```text
edaa50270ffcf9421d3bed8d6da1cd39e29511bf
```

远端 `origin/main` 已验证指向同一个 SHA。

## 2. 已完成内容

### Agent Loop Engineering 2.1.1

源码位置：`skills/agent-loop-engineering`

已加入：

- 隔离高输出日志分析、历史扫描、只读调查、嘈杂验证和独立 QA；
- 默认最多三个活跃 Worker；
- 一个 Packet 只有一个协调写者；
- 并行 Developer 必须使用不重叠 Work Order 和文件范围；
- Worker 只接收有界任务包、相关路径、必要验收项、authority fingerprint 和必要摘录；
- Worker 只返回摘要、证据路径、失败签名和唯一下一步；
- 禁止将完整父对话、无关历史、完整命令输出、期望判定、密钥或 Session 传给 Worker；
- 增加通用 Host Cost Controls；
- 增加 Claude Code 适配：`/clear`、`/compact`、`@file`、`/rewind`、模型/effort 稳定性；
- 保持 `contract_version: "2.0"` 和 `record_version: "2.1"` 向后兼容；
- 校验器增加 `max_parallel_agents` 和 `single_writer` 等 Packet 策略检查。

关键参考文件：

- `skills/agent-loop-engineering/references/en/isolated-delegation.md`
- `skills/agent-loop-engineering/references/zh-CN/isolated-delegation.md`
- `skills/agent-loop-engineering/references/en/host-cost-controls.md`
- `skills/agent-loop-engineering/references/zh-CN/host-cost-controls.md`

### CMS Project Governance 2.1.1

源码位置：`skills/cms-project-governance`

已加入：

- 只在高输出且可分离的工作中授权隔离 Worker；
- 小型、高耦合或需要频繁澄清的任务留在主 Loop；
- 默认最多三个 Worker、一个协调写者；
- 共享 fingerprint 和必要摘录，不复制全部治理历史；
- Worker 回传摘要和证据，不回传过程性长文本；
- 保留独立 QA、Owner 门禁、目标对齐和交付类别边界。

### Plugin 1.1.1

Plugin 位置：`plugins/ai-engineering-expert`

包含：

- `agent-loop-engineering` 2.1.1；
- `cms-project-governance` 2.1.1；
- Claude/OpenClaw/Qoder 相关 manifests；
- 中英文 Skill 文件和参考资料；
- Qoder Plugin 文件。

Plugin manifest 版本已经同步为 `1.1.1`，包括：

- `package.json`；
- `openclaw.plugin.json`；
- `.claude-plugin/plugin.json`；
- `.qoder-plugin/plugin.json`。

## 3. ClawHub 发布状态

### 独立 Skill

Agent Loop：

- URL：<https://clawhub.ai/englandtong/skills/agent-loop-engineering>
- 版本：`2.1.1`
- 独立 listing 保留，没有 Merge Listing；
- Categories：`development, automation, agents`；
- Topics：`ai-coding, autonomous-agents, software-testing, context-management, execution-loops`。

CMS：

- URL：<https://clawhub.ai/englandtong/skills/coding-management-system>
- 本地目录名是 `cms-project-governance`，ClawHub 现有 canonical slug 是 `coding-management-system`；不要另建重复 listing；
- 版本：`2.1.1`；
- Categories：`agents, productivity, development`；
- Topics：`project-governance, requirements-analysis, goal-alignment, qa-acceptance, token-efficiency`。

### Bundle Plugin

- 名称：`@englandtong/ai-engineering-expert`；
- 版本：`1.1.1`；
- Family：`bundle-plugin`；
- Bundle format：`claude`；
- Categories：`context, tools`；
- Topics：`ai-coding, autonomous-agents, project-governance, context-management, quality-assurance`；
- Release ID：`rd7db9asgg20gd51rny7a5et098cg21k`；
- Publication status：`published`；
- Plugin 发布时绑定的 source commit：`edaa50270ffcf9421d3bed8d6da1cd39e29511bf`；
- Plugin 文件数：60；
- Plugin 总大小：224,749 bytes。

不要再次发布 2.1.1 或 1.1.1。下一次功能发布应递增到两个 Skill 的 `2.1.2` 或更高版本，并将 Plugin 递增到 `1.1.2` 或更高版本。

## 4. 验证证据

已执行并通过：

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\agent-loop-engineering
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" skills\cms-project-governance
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" plugins\ai-engineering-expert\skills\agent-loop-engineering
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" plugins\ai-engineering-expert\skills\cms-project-governance
node skills\agent-loop-engineering\scripts\test-state-tools.mjs
```

测试结果：13 个状态工具回归测试通过，包含：

- 冲突时零写入；
- R21/R23 状态冲突；
- QA 标题与正文冲突；
- 多个 Current Assignment；
- Current Effective override；
- 历史 Old 目录识别；
- Contract 不升级为 Runtime；
- 旧 JSONL 字段聚合；
- 权威路径逃逸；
- Stage Reviewer 失败、返修、复验；
- Stage Reviewer 不得签最终验收；
- write scope 越界；
- 不安全并发 Worker 设置。

已执行 Node 语法检查：

```powershell
node --check skills\agent-loop-engineering\scripts\state-tools-lib.mjs
node --check skills\agent-loop-engineering\scripts\bootstrap-active-packet.mjs
node --check skills\agent-loop-engineering\scripts\validate-loop-state.mjs
```

结果通过。

Plugin Inspector：

- Breakages：0；
- Warnings：0；
- Findings：none；
- 文件数：60。

源 Skill 与 Plugin 内嵌副本已经逐文件 SHA256 比较，结果一致：

- Agent Loop：28 files identical；
- CMS：24 files identical。

## 5. 发布档案

Skill ZIP：

- [agent-loop-engineering-v2.1.1.zip](D:/Development/ClawSkills/ClawSkills/release/ClawHub-v2.1.1/agent-loop-engineering-v2.1.1.zip)
- [cms-project-governance-v2.1.1.zip](D:/Development/ClawSkills/ClawSkills/release/ClawHub-v2.1.1/cms-project-governance-v2.1.1.zip)

Plugin/Qoder ZIP：

- [ai-engineering-expert-v1.1.1-qoder.zip](D:/Development/ClawSkills/ClawSkills/release/AI-Engineering-Expert-v1.1.1/ai-engineering-expert-v1.1.1-qoder.zip)

发布说明：

- `release/ClawHub-v2.1.1/RELEASE_NOTES.md`；
- `release/AI-Engineering-Expert-v1.1.1/RELEASE_NOTES.md`。

SHA256：

```text
d8e4c9eb9976c33a89ac68e8c86dd6af36d26c8a41fc20ba82e7a3d481b90320  agent-loop-engineering-v2.1.1.zip
0d86f8afa1fbb3094e0f4900f331ac579df7aab6f62e0c6e2c44d76979daf71c  cms-project-governance-v2.1.1.zip
250638d853cb3597eef9cc72bae2d76b4aceb1c2e250564a226e7f625e056c39  ai-engineering-expert-v1.1.1-qoder.zip
```

## 6. 当前未完成事项

### 必须优先处理

1. 将本机已安装的旧 Skill 更新到 2.1.1。

当前已发现：

```text
C:\Users\engla\.codex\skills\agent-loop-engineering\SKILL.md  -> Version: 2.1.0
C:\Users\engla\.codex\skills\cms-project-governance\SKILL.md -> Version: 2.1.0
```

仓库源码和 ClawHub 已是 2.1.1。接手 AI 不应继续使用本机旧副本进行验证或开发。建议使用正式安装/更新流程，或在确认安装边界后从仓库同步 2.1.1。更新后必须重新读取完整 `SKILL.md` 并检查本地安装版本。

2. 确认当前运行环境实际加载的是哪个 Skill 副本。

可能同时存在：

- 仓库源码：`D:\Development\ClawSkills\ClawSkills\skills\...`；
- Plugin 内嵌副本：`D:\Development\ClawSkills\ClawSkills\plugins\ai-engineering-expert\skills\...`；
- 本机 Codex 安装副本：`C:\Users\engla\.codex\skills\...`；
- 其他 Host 自己的安装缓存。

不要只看仓库文件就假设运行时已经更新。

### 发布后持续工作

- 用真实项目执行至少十轮迁移前后对比，记录平台真实 Token（若 Host 提供）、读取文件数、工具输出字符、回传字符和全量回归次数；
- 验证使用隔离 Worker 后，主 Agent 上下文是否真正下降；
- 对小任务测量委派开销，避免所有任务都启动子 Agent；
- 检查并发 Worker 是否在实际 Host 上支持独立上下文、文件权限和进程隔离；
- 对 Claude、Qoder、OpenClaw 分别写 Host Adapter 的真实验证记录；
- 如需要更新 listing summary/categories/topics，先读取现有 ClawHub listing，保留两个 listing 独立，不执行 Merge。

## 7. 下一位 AI 的推荐第一步

先做只读确认，不要立即修改仓库：

```powershell
Set-Location D:\Development\ClawSkills\ClawSkills
git status --short
git rev-parse HEAD
Get-Content skills\agent-loop-engineering\SKILL.md -Encoding UTF8 | Select-Object -First 12
Get-Content skills\cms-project-governance\SKILL.md -Encoding UTF8 | Select-Object -First 12
Get-Content plugins\ai-engineering-expert\package.json -Encoding UTF8 | Select-Object -First 12
```

然后：

1. 读取本交接文件；
2. 读取两个仓库 Skill 的完整 `SKILL.md`；
3. 检查本机实际安装副本版本；
4. 运行 13 个状态工具测试；
5. 确认 ClawHub 当前版本，不要重复发布；
6. 如果用户没有新需求，不要创建新的 2.1.2 版本；
7. 如果用户提出新功能，先判断是 Skill 核心规则、Host Adapter、Plugin manifest、验证器还是发布资料的变更。

## 8. 重要设计边界

### 多子 Agent 不是默认并发

只有在任务可分离且读取/输出量较大时才委派。适合日志、大型只读扫描、嘈杂测试和独立 QA。小修复或高耦合工作留在主 Agent。

### 单写者和独立验收不能破坏

一个 Active Packet 只能有一个协调写者。并行 Developer 不能修改重叠文件。Stage Reviewer 不能冒充 Standard/Full 的 Independent QA。

### 不要把 Host 细节写进通用契约

模型价格、缓存时间、输出阈值、具体命令和版本号属于 Host Adapter。核心 Skill 只定义通用的上下文、委派、证据和边界原则。

### 不要把成本控制变成完成证明

上下文更小、Token 更少、测试输出更短，都不能证明产品已完成。仍然必须区分 Contract、Governance、Artifact 和 Runtime 证据。

### 不要恢复旧项目的文档膨胀

优先使用一个 Active Packet、Loop Runs、必要时一个合并 Work Order 和最终 QA 记录。不要为每个小阶段重复创建状态、Handoff、QA 和完成文件。

## 9. 接手时的停止条件

遇到以下情况，先停在当前状态并报告，不要自行猜测：

- GitHub commit、ClawHub source commit 和本地源码不一致；
- 当前目标、Non-Goals、Work Order 或验收标准冲突；
- 需要改变公开 listing、Owner、版本策略或 canonical slug；
- 需要删除历史 Skill、执行 Merge Listing 或改名；
- 需要写入项目目录之外；
- 需要凭证、生产数据、付费资源、系统安装、提权或破坏性操作；
- 需要把 Stage Review 改成最终 Accepted；
- 需要修改 `contract_version` 或破坏旧记录兼容性。

## 10. 当前唯一建议动作

先将运行环境实际加载的两个 Skill 更新并确认到 2.1.1，然后在一个低风险、只读或小型项目任务上验证隔离 Worker 的真实上下文收益。没有这个实测，不要宣称固定 Token 降幅。

