# CMS: AI Coding Management System

状态：Draft for review  
日期：2026-06-10  
用途：给其他 Agent、开发者或审阅者理解并评估 CMS 架构。  

## 1. 定义

CMS，全称 **AI Coding Management System**，是一套管理 AI Coding Agent 的工程体系。

它不是单个 Prompt、单个 Skill、单个 MCP、单个 Runner，也不是某一个 AI 编程软件。它是一套把 AI Agent 当作可管理执行单元的系统方法。

核心定义：

> CMS 把大模型当作“知识丰富、执行很快、但缺少工作经验、短期记忆不稳定、容易早报完成的新人”，通过目标管理、标准作业、验证门禁、异常停止、根因分析、状态记录和持续改善，把 Agent 的能力放大，同时控制方向和质量。

CMS 的目标不是让 Agent “听话”，而是让 AI 编程过程变得：

- 可控制。
- 可验证。
- 可追溯。
- 可复盘。
- 可持续改善。
- 可由多个 Agent 接力。
- 可在需要时升级给管理人员。

## 1.1 方法来源：采购、新品研发和食品生产管理经验

CMS 的方法来源不是抽象管理学，而是来自长期真实生产和品质管理经验。

该体系的提出者有 20 年采购、新品研发和食品生产经验。核心经验是：

- 如何控制品质。
- 如何把风险提前发现，尽量避免问题发生。
- 如何写好 SOP，让不同人员按稳定方式执行。
- 问题发生时，如何快速识别、隔离、处理和升级。
- 出现新问题后，如何 review、形成 action plan，并把经验沉淀回流程。

这些经验与 AI Coding 管理是同构问题。

| 采购 / 新品研发 / 食品生产经验 | CMS 对应机制 |
| --- | --- |
| 控制品质 | Completion Gate / Evaluator / Rubric |
| 风险提前发现 | Risk Analysis / Hazard Analysis |
| 尽量避免问题 | Preventive Controls / Poka-Yoke |
| 写好 SOP | Execution Contract / Templates |
| 问题发生时的处理流程 | Stop Rules / Corrective Action |
| 新问题 review | Retrospective / Evaluation |
| Action Plan | `PENDING.md` / `NEXT_ACTIONS.md` / `DECISIONS.md` |

核心立场：

> 品质不能靠人或 Agent 自觉。风险要前置，关键步骤要 SOP 化，异常要有处理机制，新问题要 review 并转化为 action plan。

因此，CMS 不是为了限制 Agent，而是为了像管理真实生产一样，把 AI Coding 变成有方向、有标准、有检查、有异常处理、有持续改善的工作系统。

## 2. 问题背景

AI Coding Agent 通常具备很强的知识和执行能力，但默认存在类似初入职场新人的问题：

- 会写代码，但不一定主动复核。
- 会修 bug，但不一定追根因。
- 会执行一步，但不一定做到可验收。
- 会说完成，但不一定有证据。
- 能运行很久，但可能目标漂移。
- 能找出错误，但不一定持续修到通过。
- 上下文压缩或换 Agent 后，容易丢失关键约束。

因此，CMS 要解决的不是“AI 会不会写代码”，而是：

> 如何通过流程、标准、检查、异常处理、门禁和持续改善，让多个 AI Agent 稳定地产出合格结果。

## 3. 核心原则

CMS 的核心原则：

1. 大方向可以软，当前阶段必须硬。
2. Agent 可以自由写代码，但不能自由宣布完成。
3. 没有验证，不允许 Done。
4. 没有证据，不许自信。
5. 异常即停止，失败要追根因。
6. 每轮只做当前必要的最小增量。
7. Evaluator 不接受 Developer 自述作为通过证据。
8. 默认不是做下一步，而是做到可验收状态。
9. 不相信聊天记忆，优先相信项目文件里的状态合同。
10. 管理系统应该渐进启用，不能一开始就给所有任务套重治理。

## 4. CMS 与现有 Skill 的关系

CMS 是总方法论。

`agent-loop-engineering` 是 CMS 的第一个 Skill 实现。

现有 Skill 关系：

| Skill | 在 CMS 中的位置 |
| --- | --- |
| `agent-loop-engineering` | Coding loop 总控、状态协议、停止门禁、完成门禁 |
| `daily-workflow` | checkpoint、handoff、恢复上下文 |
| `ai-workflow-os` | 非编码研究、资料治理、知识组织 |
| `project-lifecycle-navigator` | 目标澄清、阶段判断、项目生命周期 |
| `web-search-rules` | 外部资料、网页、API 文档、来源可信度 |

CMS 不应该让 Agent 每轮加载所有 Skill，而是按当前任务和项目等级路由。

## 5. 四层架构

CMS 可以分为四层：

```text
L1 Management Layer
  目标、方向、项目分级、人工介入规则

L2 Process Layer
  Plan -> Do -> Verify -> Debug -> Re-verify -> Evaluate -> Continue/Stop

L3 Control Layer
  Templates、Stop Gates、Completion Gates、Checker、Runner

L4 Tool Layer
  MCP、CI、Browser、GitHub、Tests、Logs、Screenshots、Metrics
```

### L1 Management Layer

管理层决定：

- 目标是什么。
- 当前阶段是什么。
- 什么算完成。
- 什么不做。
- 什么时候必须问人。
- 项目属于小任务、中任务、大项目还是产品级项目。

### L2 Process Layer

流程层定义 Agent 每轮怎么工作：

```text
Understand target
-> Select next action
-> Implement minimal change
-> Verify
-> Debug failures
-> Re-verify
-> Evaluate
-> Continue / Done / Done with Risk / Blocked
```

### L3 Control Layer

控制层把软规则变成可检查机制：

- 模板控制文件格式。
- Checker 检查状态是否合法。
- Runner 决定是否进入下一轮。
- Completion Gate 防止假完成。
- Stop Gate 防止越权和危险执行。

### L4 Tool Layer

工具层提供真实环境能力：

- 测试、类型检查、构建。
- 浏览器、截图、DOM、控制台日志。
- GitHub、CI、日志系统。
- MCP 工具。
- 本地脚本。

## 6. 项目分级入口

CMS 先判断项目等级，再决定启用哪些流程和工具。

| 项目类型 | 人类工程量 | AI loop | Agent 角色 | 工作流 |
| --- | ---: | ---: | --- | --- |
| 小任务 | 0.5-2 人天 | 1-3 loops | 1 个 Agent | 单 Agent 闭环 |
| 中任务 | 3-10 人天 | 3-8 loops | Developer + Evaluator | 开发 + 独立评估 |
| 大项目 | 2 周以上 | 8+ loops | Planner + Developer + Evaluator | 阶段目标 + 多轮反馈 |
| 产品级项目 | 1 月以上 | 多阶段 loops | 多 Agent + Runner + Rubric | Production System / Harness |

判断时不要用 AI 实际执行速度判断大小，而要用人类工程师工作量判断复杂度。AI loop 数用于估算自动化执行成本，Agent 角色数用于判断是否需要分工。

## 7. 文件治理：渐进式 Docs/

文件不是越多越专业。CMS 应默认使用最小文件集，随着项目复杂度升级。

### 7.1 文件分层

```text
Core:
  TARGET.md
  ACCEPTANCE.md
  EVALUATION.md

Working:
  STATUS.md
  NEXT_ACTIONS.md
  PENDING.md

Control:
  LOOP_CONFIG.md
  STOP_RULES.md
  LOOP_RUNS.jsonl
  DECISIONS.md

Quality:
  RUBRIC.md
  QUALITY_VISION.md

Handoff:
  COMPLETED.md
  HANDOFF.md
```

### 7.2 按项目等级启用

小任务：

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  EVALUATION.md
```

中任务：

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  STATUS.md
  NEXT_ACTIONS.md
  EVALUATION.md
  PENDING.md
```

如涉及 UI、体验、主观质量，再加：

```text
Docs/
  RUBRIC.md
  QUALITY_VISION.md
```

大项目：

```text
Docs/
  DIRECTION.md
  TARGET.md
  ACCEPTANCE.md
  STATUS.md
  NEXT_ACTIONS.md
  EVALUATION.md
  PENDING.md
  DECISIONS.md
  LOOP_CONFIG.md
  LOOP_RUNS.jsonl
```

产品级项目：

```text
Docs/
  DIRECTION.md
  TARGET.md
  ACCEPTANCE.md
  EXECUTION_CONTRACT.md
  LOOP_CONFIG.md
  STOP_RULES.md
  NEXT_ACTIONS.md
  EVALUATION.md
  LOOP_RUNS.jsonl
  STATUS.md
  PENDING.md
  COMPLETED.md
  DECISIONS.md
  RUBRIC.md
  QUALITY_VISION.md
  HANDOFF.md
```

说明：`EXECUTION_CONTRACT.md` 可作为产品级或长期项目的总工作合同；小任务不必单独创建，可由 Skill 顶层规则提供默认合同。

## 8. 目标管理

大项目无法在第一天明确所有最终细节。因此 CMS 不要求一开始写完整终局目标，而要求目标分层。

```text
Direction / North Star
  -> Phase Target
    -> Sprint Goal
      -> Acceptance Criteria
```

规则：

- 大方向可以演化。
- 当前阶段目标必须明确。
- 当前验收标准必须明确。
- 方向变化必须记录到 `DECISIONS.md`。
- 如果当前动作与 `TARGET.md` 冲突，必须停止并问人。

## 9. 角色模型

CMS 默认角色：

| 角色 | 类比 | 职责 |
| --- | --- | --- |
| Manager / User | 管理者 | 定方向、批准重大变化、最终验收 |
| Planner Agent | 产品/技术规划新人 | 澄清目标、拆阶段、写验收 |
| Developer Agent | 开发新人 | 实现、修复、运行基础验证 |
| Evaluator Agent | QA/审计新人 | 独立检查，不接受 Developer 自述 |
| Runner | 班组长/调度器 | 控制循环、预算、停止条件 |
| Checker | 质检门禁 | 判断状态是否合法、能否继续 |
| CMS Docs | 管理台账 | 保存目标、证据、决策、日志 |

### 9.1 上下文隔离

Evaluator 默认不读取 Developer 的实现思路说明，只读取：

- 目标。
- 验收标准。
- Rubric。
- 运行证据。
- 代码和可观察行为。

这样避免 Developer 的解释污染 Evaluator 判断。

## 10. 标准执行流

CMS 的标准执行流：

```text
Classify Task
  -> Define Direction / Target / Acceptance
  -> Select Workflow
  -> Execute Standard Work
  -> Verify Evidence
  -> Debug Root Cause
  -> Re-verify
  -> Evaluate Gate
  -> Continue / Done / Done with Risk / Blocked
```

默认完成语义：

```text
Unless the user explicitly asks for analysis only, a coding request means:
understand the target, implement, verify, debug failures, re-verify, evaluate, and stop only at Done, Done with Risk, Blocked, or budget exhausted.
```

中文：

```text
除非用户明确只要求分析，否则编程任务默认包含理解目标、实现、验证、失败修复、再验证和完成判定。
Agent 只能在 Done、Done with Risk、Blocked 或预算耗尽时停止。
```

## 11. 完成状态

CMS 只允许这几种状态：

| 状态 | 含义 |
| --- | --- |
| `Continue` | 仍有明确下一步，且没有触发停止门禁 |
| `Done` | 成功标准满足，且有足够自动验证和功能验证证据 |
| `Done with Risk` | 核心目标完成，但存在明确未验证边界、环境限制或低风险缺口 |
| `Blocked` | 需要人提供信息、权限、密钥、环境、决策或方向确认 |
| `Invalid State` | 状态文件不完整、证据缺失、Done 声明不合法或日志不可解析 |

`Invalid State` 是给 checker / runner 用的状态，代表系统记录本身不可信，不能继续自动运行。

## 12. 完成门禁

Agent 不能自由宣布完成。

| 情况 | 允许状态 |
| --- | --- |
| 代码改了但没测试 | 不允许 Done |
| 测试失败但没修 | Continue 或 Blocked |
| 环境失败但原因明确 | Blocked |
| 自动验证通过但功能没验 | Done with Risk |
| 自动验证 + 功能验证都通过 | Done |
| Done 但无证据 | Invalid State |

核心规则：

```text
没有验证，不允许 Done。
没有证据，不许自信。
验证失败，不允许假装完成。
```

## 13. 停止门禁

以下情况必须停止并问人：

- 密钥、账号、OAuth、浏览器登录。
- 生产数据库、真实用户数据。
- 付费云资源、外部账户变更。
- 系统级安装、管理员权限、驱动。
- 不可逆删除、覆盖、迁移、force push、reset、历史重写。
- 技术栈替换、大版本框架迁移。
- 当前方向与 `TARGET.md` 或 `DIRECTION.md` 冲突。
- 连续失败达到预算。
- 上下文超预算且无法安全压缩。

## 14. Debug 和问题解决规则

CMS 把 PDCA、Five Whys、DMAIC、OODA、Definition of Done 等方法压缩成 6 条 Agent 工作纪律：

1. Problem Before Action  
   未定义问题，不开始行动。

2. Evidence Before Confidence  
   没有证据，不许自信。

3. Verify Before Done  
   没有验证，不许 Done。

4. Root Cause Before Fix  
   失败后先找根因，不乱改。

5. Continue Until Gate  
   默认继续到 Done / Done with Risk / Blocked / 预算耗尽。

6. Escalate When Unsafe  
   遇到权限、密钥、生产、不可逆操作必须问人。

## 15. AI Coding Production System

CMS 借鉴 TPS、TQC、Six Sigma、ISO 9001、ISO 22000、FSSC 22000、HACCP、FSMA、GFSI、8D/Five Whys 等管理体系。

目标不是建立管理学资料库，而是抽取控制机制。

```text
AI Coding Production System
  = Direction Alignment
  + Standard Work
  + Built-in Quality
  + Abnormal Stop
  + Root Cause Debugging
  + Real Evidence
  + Independent Audit
  + Continuous Improvement
```

核心映射：

| 生产体系机制 | CMS 机制 |
| --- | --- |
| Hoshin Kanri | `DIRECTION.md -> TARGET.md -> ACCEPTANCE.md` |
| Standard Work | `EXECUTION_CONTRACT.md` 和固定 loop |
| Jidoka / Andon | 异常即停止 |
| Poka-Yoke | 不测试就无法 Done |
| Gemba Walk | 以真实代码、日志、测试、截图为准 |
| HACCP / CCP | 关键控制点和失败门禁 |
| Six Sigma / DMAIC | 数据驱动 debug 和根因分析 |
| FSSC / ISO | 记录、审核、追溯、持续改进 |

## 16. 食品安全体系映射

食品安全体系对 CMS 很有价值，因为它处理低容错、高风险、多变量和突发异常。

食品安全控制链：

```text
PRP / prerequisites
  -> Hazard analysis
    -> Critical control points
      -> Monitoring
        -> Correction / corrective action
          -> Verification
            -> Records
              -> Audit
                -> Continuous improvement
```

Agent Loop 映射：

```text
Development prerequisites
  -> Agent failure mode analysis
    -> Test / build / security / acceptance gates
      -> Loop evidence
        -> Fix or root-cause corrective action
          -> Automatic and functional verification
            -> LOOP_RUNS.jsonl and EVALUATION.md
              -> Evaluator / checker / CI audit
                -> Template and skill improvement
```

Built-in Quality Rule：

```text
Every coding loop must include defined control points, monitoring evidence, corrective action for failures, and verification records.
An agent may not continue or claim Done when a critical control point is failed or unverified.
```

中文：

```text
每个 coding loop 必须包含控制点、监控证据、失败纠正和验证记录。
关键控制点失败或未验证时，Agent 不允许继续假装完成，也不允许声明 Done。
```

## 17. Checker

Checker 是 CMS 从软协议走向半硬控制的第一步。

最小 checker 应检查：

- `TARGET.md` 是否存在。
- `ACCEPTANCE.md` 是否存在。
- `NEXT_ACTIONS.md` 是否只有一个下一步。
- `EVALUATION.md` 最新状态是否合法。
- `LOOP_RUNS.jsonl` 是否为合法 JSONL。
- 是否触发 `STOP_RULES.md`。
- 是否允许继续下一轮。
- Done 是否有足够证据。

输出固定：

```text
Continue
Done
Done with Risk
Blocked
Invalid State
```

## 18. Runner

Runner 是 CMS 的调度器。

Runner 不负责写代码，负责：

- 调用 Agent。
- 控制 loop 次数。
- 读取 checker 结果。
- 判断是否继续。
- 处理超时、连续失败、Blocked。
- 记录运行日志。

Runner 只应在 checker 返回 `Continue` 且预算未耗尽时启动下一轮。

## 19. MCP

MCP 是未来工具化方向，但不应第一步就做。

建议路径：

```text
Skill 规则稳定
-> templates 稳定
-> checker 稳定
-> runner 稳定
-> 再封装 MCP
```

最小 MCP tools：

| Tool | 作用 |
| --- | --- |
| `read_loop_state` | 读取最小状态 |
| `validate_loop_state` | 检查状态完整性 |
| `append_loop_run` | 追加 JSONL 记录 |
| `evaluate_stop_rules` | 判断是否必须停止 |
| `get_next_action` | 返回下一轮动作 |

## 20. 渐进路线图

建议落地顺序：

1. 更新 `agent-loop-engineering` 顶层规则。
2. 增加 `templates/`。
3. 增加 `agent-loop-check`。
4. 增加 local runner。
5. 稳定后再做 MCP。
6. 产品级项目再考虑 dashboard / CI audit / multi-agent platform。

下一批最值得做的文件：

```text
skills/agent-loop-engineering/templates/
  EXECUTION_CONTRACT.md
  DIRECTION.md
  TARGET.md
  ACCEPTANCE.md
  EVALUATION.md
  LOOP_CONFIG.md
  STOP_RULES.md
  NEXT_ACTIONS.md
  RUBRIC.md
  QUALITY_VISION.md
```

## 21. 需要其他 Agent 审阅的问题

请其他 Agent 重点审阅：

1. CMS 是否过度工程化？
2. 小任务 / 中任务 / 大项目 / 产品级项目分级是否合理？
3. `Docs/` 文件分层是否仍然过多？
4. 是否应该先做 templates，还是先做 checker？
5. `Invalid State` 是否应作为正式状态？
6. Evaluator 与 Developer 的上下文隔离是否足够明确？
7. Production System 映射是否实用，还是仍偏理论？
8. MCP 是否应该延后到 checker / runner 稳定之后？
9. CMS 是否应作为独立 Skill，还是继续作为 `agent-loop-engineering` 的方法论层？
10. 是否有更好的最小可行版本？

## 22. 最小可行 CMS

如果要做 MVP，不做完整系统，最小版本应是：

```text
Core Docs:
  TARGET.md
  ACCEPTANCE.md
  EVALUATION.md

Skill Rules:
  默认完成语义
  Verify Before Done
  Stop Rules

Checker:
  validate target
  validate acceptance
  validate Done evidence
  validate next state
```

MVP 的目标：

> 先防止 Agent 无验证宣布完成，再谈长程自动化。

## 23. 当前判断

CMS 是有价值的，但必须保持克制。

它不应该变成：

- 管理学百科。
- 超大文档系统。
- 每个小任务都要填 15 个文件。
- 为了控制而控制。

它应该变成：

- 小任务轻治理。
- 中任务有独立评估。
- 大项目有阶段目标和记录。
- 产品级项目有 Runner、Rubric、审计和追溯。

最终目标：

> 把 AI Coding 从“靠 Agent 自觉完成”升级为“由管理系统驱动完成”。
