# Agent Loop Engineering Knowledge Notes

记录时间：2026-06-10

这份笔记沉淀从构建 `agent-loop-engineering` Skill 到讨论 AI Coding Harness、MCP、专家 Agent、长程自动化和问题解决方法后的核心认知。目标是以后快速恢复思路，而不是重复阅读完整对话。

## 1. 核心目标

`agent-loop-engineering` 的目标不是让 Agent “更会写代码”，而是让 Agent 在编码工作中：

- 不跑偏。
- 不只做一步就结束。
- 不靠聊天记忆维持状态。
- 不在没有证据时宣布完成。
- 能在长程任务中持续推进、验证、修复、复盘。
- 遇到权限、密钥、生产数据、不可逆操作和方向冲突时停止问人。

一句话：

> Agent 不应该默认做下一步，而应该默认做到可验收状态。

## 2. Skill 的真实性质

Markdown Skill 本身不是硬约束，而是软约束协议。

| 层级 | 强度 | 例子 |
| --- | ---: | --- |
| Markdown / Skill / Prompt | 软约束 | 告诉 Agent 每轮更新 `Docs/STATUS.md` |
| Template / Checker / Runner | 中硬约束 | 没写 `EVALUATION.md` 就不能进入下一轮 |
| Tool permission / sandbox / CI / approval | 硬约束 | 没批准不能访问密钥、不能生产迁移、不能 force push |

因此，`agent-loop-engineering` 当前最重要的价值是“工作协议”。下一步要让它更强，应从写更多 reference 转向模板、检查器和 Runner。

## 3. 不要继续无限加 Reference

讨论中形成的关键判断：

- 每个想法都写成 reference 会造成重复和上下文膨胀。
- 现在已经有足够方法论，继续堆文档收益下降。
- 真正应该加强的是：目标门禁、执行合同、验收门禁、状态检查和自动继续机制。

方向应从：

```text
多写说明
```

转向：

```text
少讲道理
多设门禁
少写 reference
多写模板
少依赖 Agent 自觉
多用 checker 检查
```

## 4. 像管理新人一样管理 Agent

AI Agent 很像能力强但职业习惯不足的新人：

- 会写代码。
- 会查问题。
- 会修 bug。
- 但默认不一定会主动复核。
- 默认容易只做用户说的“一步”。
- 默认会在满足表层要求后停止。
- 默认可能把“动作完成”误认为“目标完成”。

因此不能只说：

```text
修复这个 bug。
```

而要把默认语义改成：

```text
复现问题。
定位根因。
修复。
验证。
如果验证失败，继续定位。
记录结果。
确认没有副作用。
最后再汇报 Done / Done with Risk / Blocked。
```

## 5. 默认完成语义

未来 Skill 顶层应明确：

```text
Unless the user explicitly asks for analysis only, a coding request means:
implement, verify, debug failures, re-verify, and stop only at Done, Done with Risk, Blocked, or budget exhausted.
```

中文：

```text
除非用户明确只要求分析，否则编程任务默认包含实现、验证、失败修复、再验证和完成判定。
```

这条规则用于解决“Agent 只做一步、不主动继续”的问题。

## 6. Plan 模式为什么不够

Plan 模式解决的是：

```text
我要怎么做？
```

但真正完成编码任务还需要：

```text
我做了吗？
做完了吗？
验证了吗？
失败后继续了吗？
什么时候停止？
```

因此 Plan 只能作为第一阶段，不能替代执行闭环。

真正需要的是：

```text
Plan -> Action -> Verify -> Debug -> Re-verify -> Evaluate -> Continue / Stop
```

## 7. 目标不清楚时的处理

大项目不可能第一天就知道最终所有细节，因此不能要求用户一开始写出完整终局目标。

更合理的分层：

```text
North Star / Direction 大方向
  -> Phase Goal 阶段目标
    -> Sprint Goal 当前小目标
      -> Acceptance Criteria 本轮验收
```

核心原则：

> 大方向可以软，当前阶段必须硬。

建议引入或模板化：

- `Docs/DIRECTION.md`：大方向，允许演化。
- `Docs/TARGET.md`：当前阶段目标。
- `Docs/ACCEPTANCE.md`：当前阶段验收标准。
- `Docs/DECISIONS.md`：方向调整和关键决策。

## 8. 小项目和大项目的判断

不要用“1-2 天”这种人类日历时间判断项目大小。AI Coding 应同时看三种成本：

| 估算维度 | 作用 |
| --- | --- |
| 人类工程师工作量 | 判断真实复杂度和商业成本 |
| AI loop 数 | 判断自动化执行成本 |
| Agent 角色数 | 判断是否需要 Planner / Developer / Evaluator 分工 |

建议分类：

| 类型 | 人类工程量 | AI loop | Agent 角色 |
| --- | ---: | ---: | --- |
| 小任务 | 0.5-2 人天 | 1-3 loops | 1 个 Agent |
| 中任务 | 3-10 人天 | 3-8 loops | Developer + Evaluator |
| 大项目 | 2 周以上 | 8+ loops | Planner + Developer + Evaluator |
| 产品级项目 | 1 月以上 | 多阶段 loops | 多 Agent + Runner + Rubric |

## 9. Problem Solving 方法的抽象

PDCA、Five Whys、DMAIC、OODA、Scrum Definition of Done、Retrospective、Cynefin 等方法不应全部直接塞进 Skill，而应抽象成 Agent 工作纪律。

| 方法 | 对 Agent 的启发 |
| --- | --- |
| PDCA / PDSA | 每轮不能只 Do，必须 Check 和 Act |
| Five Whys | 测试失败不能只修表面错误，要追根因 |
| DMAIC | 复杂问题要 Define、Measure、Analyze、Improve、Control |
| OODA | 不确定环境先观察真实运行结果，再决定 |
| Definition of Done | 没有共同 Done 标准，Agent 会过早宣布完成 |
| Retrospective | 长程任务要记录可复用经验 |
| Cynefin | 小任务直接做，大项目实验和阶段化 |

## 10. 六条 Agent 工作纪律

最适合写进核心规则或执行合同：

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

## 11. 完成门禁

Agent 不能自由宣布完成。

| 状态 | 允许吗 |
| --- | --- |
| 代码改了但没测试 | 不允许 Done |
| 测试失败但没修 | 不允许 Done |
| 环境失败但没说明 | Blocked |
| 自动验证通过但功能没验 | Done with Risk |
| 自动验证 + 功能验证都通过 | Done |

关键规则：

```text
没有验证，不允许 Done。
验证失败，不允许结束。
没有解释失败原因，不允许交付。
```

## 12. 专家 Agent 的本质

“你是十年 QA 专家”不是打开模型里的 QA 模块，也不会临时修改模型参数。

它的作用是上下文软偏置：

- 更容易激活 QA、测试、验收、风险、证据、边界条件等生成模式。
- 让回答更像训练数据中的资深 QA 行为。
- 但不能保证它真的严格执行。

更强写法不是身份词，而是行为合同：

```text
你是资深 QA Evaluator。
你必须根据验收标准逐条评估。
每条 Pass / Fail 必须提供证据。
没有证据只能标记 Unknown。
不接受 Developer 自述作为通过证据。
最后只能输出 Pass / Fail / Blocked。
```

公式：

```text
角色 + 任务 + 输入边界 + 输出格式 + 判断标准 + 证据要求 + 禁止行为
```

比单独说“你是专家”更可靠。

## 13. MCP 的角色

MCP 是工具服务器协议，不是 Agent 管理者。

它负责：

```text
Agent -> 调用工具
MCP Server -> 执行工具 / API / 本地能力
MCP Server -> 返回结构化结果
Agent -> 根据结果继续推理
```

MCP 有统一协议，但每个工具要通过 schema 自我描述：

- 工具名。
- description。
- input schema。
- required 参数。
- 返回结果。

对 `agent-loop-engineering` 的启发：

| Markdown 规则 | 可工具化为 MCP Tool |
| --- | --- |
| 检查 `Docs/TARGET.md` | `validate_target()` |
| 判断是否能继续 | `check_loop_state()` |
| 追加运行记录 | `append_loop_run()` |
| 判断停止门禁 | `evaluate_stop_rules()` |
| 读取最新日志 | `read_recent_loop_runs()` |

## 14. 长程运行的偏差风险

10 小时、多轮压缩、多 Agent 接力后，常见风险：

- 目标漂移。
- 验收标准变形。
- 上下文污染。
- 历史压缩丢关键约束。
- 自我确认偏差。
- 低收益循环。

收紧方式：

- 不相信聊天记忆。
- 每轮重新读取项目文件里的目标合同。
- 用 `TARGET.md`、`ACCEPTANCE.md`、`RUBRIC.md`、`STOP_RULES.md`、`EVALUATION.md` 作为锚。
- 让 Runner / Checker 检查是否允许继续。

## 15. Harness Engineering 的正确位置

`agent-loop-engineering` 目前是协议层。

```text
agent-loop-engineering = 协议
Docs/ = 状态数据库
templates/ = 稳定格式
checker = 协议审计
runner = 自动调度
MCP = 工具化接口
evaluator = 独立判断
```

只有 Skill Markdown 不足以做到 OpenClaw / Hermes 类自动化系统。  
要达到类似效果，需要外层执行器和检查器。

## 16. 下一步最有价值的改进

不要继续优先写 reference。

优先级建议：

| 优先级 | 动作 | 目的 |
| --- | --- | --- |
| P0 | 增加 `templates/` | 固定 `Docs/` 状态文件格式 |
| P0 | 增加 `EXECUTION_CONTRACT.md` | 明确默认完成语义和工作纪律 |
| P1 | 增加 `agent-loop-check` | 检查是否允许继续 / Done / Blocked |
| P1 | 增加 `RUBRIC.md` 和 `QUALITY_VISION.md` 模板 | 支撑主观质量和 UI/UX 验收 |
| P2 | 增加本地 Runner | 自动触发下一轮 |
| P2 | 做最小 MCP Server | 把状态读取、停止判断、日志写入工具化 |
| P3 | 做可视化面板 | 查看长程运行状态和得分变化 |

## 17. 最小 Checker 应检查什么

`agent-loop-check` 最小能力：

- `Docs/TARGET.md` 是否存在。
- `Docs/ACCEPTANCE.md` 是否存在。
- `Docs/NEXT_ACTIONS.md` 是否只有一个下一步。
- `Docs/EVALUATION.md` 最新状态是否合法。
- `Docs/LOOP_RUNS.jsonl` 是否合法 JSONL。
- 是否触发 `STOP_RULES.md`。
- 是否允许继续下一轮。

输出固定：

```text
Continue
Done
Done with Risk
Blocked
Invalid State
```

## 18. 最小 MCP Tool 集

如果进入 MCP 化，不要一开始做大。最小工具集：

| Tool | 作用 |
| --- | --- |
| `read_loop_state` | 读取最小状态 |
| `validate_loop_state` | 检查状态完整性 |
| `append_loop_run` | 追加 JSONL 记录 |
| `evaluate_stop_rules` | 判断是否必须停止 |
| `get_next_action` | 返回下一轮动作 |

## 19. 最终判断

当前 `agent-loop-engineering` 是有效的。

它已经能帮助 Agent：

- 保存目标。
- 控制上下文。
- 明确停止规则。
- 减少假完成。
- 支持多 Agent 接力。

但它还不够硬。

下一阶段要从：

```text
知识型 Skill
```

升级为：

```text
管理型 Skill + 模板 + 检查器 + Runner / MCP
```

最重要的方向：

> 不要只让 Agent “知道该怎么做”，要让系统检查它“有没有真的这么做”。

## 20. IMA 生产管理笔记补充

后续 IMA 笔记进一步确认：TPS、TQC、FSSC 22000 以及生产管理方法论，与 AI 编程管理 / Agent Loop Engineering 是同一类问题。

相关 IMA 笔记：

| IMA note_id | 标题 | 价值 |
| --- | --- | --- |
| `7470298035138559` | 随身笔记：TPS、TQC、FSSC 22000 对 AI 编程管理的启发 | 确认 AI 编程需要生产管理式的流程、标准、检查、异常处理、门禁和持续改善 |
| `7470303445780059` | 随身笔记：生产管理方法论大全——管人、管工作、管生产 | 建立从管人、管过程、管系统、管质量到 AI Agent 管理的完整方法地图 |
| `7470311574341202` | 随身笔记：生产管理方法论大全（续篇）——战略部署、防错、快速切换与创新方法 | 补充战略、防错、效率、创新、现场管理方法，形成 26 种方法全集 |

核心结论：

> 稳定、高质量、可复制的生产，不是靠人或 Agent 自觉，而是靠流程、标准、门禁、异常处理、审核和持续改善。

这与 AI Agent 的问题完全对应：

- Agent 会写代码，但不一定会主动复核。
- Agent 会修 bug，但不一定追根因。
- Agent 会执行一步，但不一定做到可验收。
- Agent 会说完成，但不一定有证据。
- Agent 能运行很久，但可能目标漂移。

生产管理体系的价值，就是把这些“靠自觉”的行为变成系统规则。

## 21. AI Coding Production System

这些生产管理方法最终可以收敛成一套更适合 AI Coding 的方法论：

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

对应执行链路：

```text
目标标准化
-> 执行最小增量
-> 异常即停止
-> 质量内建
-> 独立验证
-> 持续改善
-> 可审计交付
```

这条线比继续扩写 reference 更有价值。它可以成为 `agent-loop-engineering` 下一阶段的核心框架。

## 22. 生产管理方法到 Agent Loop 的核心映射

不应把 26 种方法全部塞进 Skill。应抽出最有工程约束力的 7 类机制。

| 生产管理机制 | AI Agent 机制 | 进入 Skill 的方式 |
| --- | --- | --- |
| Hoshin Kanri 方针管理 | `DIRECTION.md -> TARGET.md -> ACCEPTANCE.md` 三层对齐 | 目标门禁和模板 |
| Standard Work 标准作业 | 每轮固定流程：读目标、实现、验证、记录、评估 | `EXECUTION_CONTRACT.md` |
| Jidoka / Andon 异常即停止 | 测试失败、构建失败、环境异常时不能假装完成 | Stop gate + checker |
| Poka-Yoke 防错 | 不测试就无法 Done，状态不完整就无法继续 | checker / MCP tool |
| Gemba Walk 现场 | 不看 Agent 自述，看真实代码、日志、测试、截图 | evidence policy |
| PDCA / DMAIC / Toyota Kata | 小实验、看结果、追根因、再调整 | debug loop |
| TQC / FSSC 22000 | 前提条件、风险分析、关键控制点、独立审核 | quality system |

这些机制可以覆盖大多数 AI Coding 跑偏问题，同时避免把 Skill 变成生产管理百科。

## 23. 最值得进入 Skill 顶层的 7 条规则

下一轮 Skill 更新建议只强化这些顶层规则：

1. Direction Alignment
   大方向可以演化，但当前阶段目标和验收标准必须明确。

2. Standard Work
   每个 coding loop 都必须按固定顺序执行，不允许只做一步。

3. Built-in Quality
   验证嵌入每轮执行，不能最后才想起测试。

4. Abnormal Stop
   测试失败、构建失败、权限缺失、环境异常、目标冲突时必须暴露问题并停止或进入修复循环。

5. Root Cause Before Repeated Fix
   连续失败时必须写根因，不允许随机改。

6. Gemba Evidence
   以真实代码、测试、日志、浏览器截图、DOM、API 响应为准，不以 Agent 自述为准。

7. Independent Audit
   复杂任务必须由 Evaluator / Checker / CI 独立判断是否完成。

## 24. 对下一阶段实现的影响

下一步不应继续新增大量 reference，而应做：

| 优先级 | 动作 | 对应生产管理思想 |
| --- | --- | --- |
| P0 | `templates/EXECUTION_CONTRACT.md` | Standard Work |
| P0 | `templates/DIRECTION.md`、`TARGET.md`、`ACCEPTANCE.md` | Hoshin Kanri |
| P0 | `templates/EVALUATION.md` | TQC / Independent Audit |
| P1 | `agent-loop-check` | Poka-Yoke / Andon |
| P1 | 停止门禁和状态合法性检查 | Jidoka |
| P1 | 失败根因字段 | DMAIC / Five Whys |
| P2 | Runner 自动循环 | PDCA / Toyota Kata |
| P2 | MCP 工具化 | FSSC-style auditable control system |

核心路线：

```text
Skill 顶层规则
-> Templates 固化标准作业
-> Checker 防止违规状态
-> Runner 自动循环
-> MCP 工具化状态和门禁
```

## 25. 最重要的新判断

`agent-loop-engineering` 不应该只是一个 Prompt Skill。

它可以演化成：

```text
AI Coding Production System 的协议层
```

也就是把生产管理中的：

- 标准作业。
- 异常停止。
- 防错。
- 现场证据。
- 关键控制点。
- 独立审核。
- 持续改善。

迁移到 AI 编程。

最终目标不是让 Agent “更听话”，而是让 AI 编程像生产系统一样：

```text
可控制
可验证
可追溯
可复盘
可持续改善
```
