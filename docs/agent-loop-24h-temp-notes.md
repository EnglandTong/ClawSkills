# Agent Loop Engineering 24h Temp Notes

记录时间：2026-06-10

用途：暂存近 24 小时围绕 `agent-loop-engineering`、AI Coding Harness、MCP、专家 Agent、生产管理体系和下一步路线的核心讨论。此文件用于压缩上下文，后续可再整理进正式知识库或 Skill 更新计划。

## 1. 已完成的仓库工作

- 新增独立 Skill：`skills/agent-loop-engineering/`。
- Skill 已改名为 `Agent Loop Engineering`，slug 为 `agent-loop-engineering`。
- `skill-card.md` 已从发布包中排除，因为该文件由 ClawHub 自动生成。
- 已生成发布 ZIP：
  - `dist/agent-loop-engineering-1.0.0.zip`
- 已推送到 GitHub：
  - `EnglandTong/ClawSkills`

已新增或更新的关键 reference：

- `references/automation-runner.md`
- `references/harness-engineering.md`
- `references/ai-coding-production-system.md`
- 原有 loop 协议、完成门禁、上下文预算、环境升级、runner adapters 等仍保留。

已新增知识库笔记：

- `docs/agent-loop-engineering-knowledge.md`

## 2. Skill 的性质判断

Markdown Skill 本身不是硬约束，而是软约束协议。

真正的控制强度分层：

| 层级 | 强度 | 例子 |
| --- | ---: | --- |
| Skill / Markdown / Prompt | 软约束 | 告诉 Agent 应该怎么做 |
| Templates / Checker / Runner | 中硬约束 | 没有验证记录就不能进入下一轮 |
| MCP / CI / 权限 / Sandbox / Approval | 硬约束 | 不能访问密钥、不能生产迁移、不能越权执行 |

核心判断：

> 不要只让 Agent 知道规则，要让系统检查它有没有真的遵守规则。

## 3. 当前 Skill 的有效性

`agent-loop-engineering` 对 AI 编程有效，尤其能帮助：

- 目标保存。
- 上下文恢复。
- 多 Agent 接力。
- 防止假完成。
- 明确停止规则。
- 减少目标漂移。

但它目前仍主要是协议层，还不是完整执行系统。

要变硬，需要：

```text
Skill 顶层规则
-> Templates
-> Checker
-> Runner
-> MCP tools
```

## 4. 不再继续无节制增加 Reference

已经形成共识：

- 不能每有一个想法就新增一个 reference。
- 过多 reference 会重复、膨胀、增加上下文负担。
- 后续重点应转向模板、检查器、Runner、MCP，而不是继续写方法论。

例外：

- 只允许新增高度压缩、总框架型 reference。
- 已新增的 `ai-coding-production-system.md` 属于总框架，整合 TPS、TQC、Six Sigma、ISO、HACCP、FSSC 等体系。

## 5. Agent 像初入职场新人

核心类比：

AI Agent 很像能力强但职业习惯不足的新人。

它会：

- 写代码。
- 查错误。
- 修 bug。
- 找问题。

但默认不一定会：

- 主动复核。
- 追根因。
- 继续做到验收。
- 不测试不交付。
- 发现方向偏移就停下来。

因此不能只对 Agent 说“做这个”，而要给：

- 工作合同。
- 完成标准。
- 复核要求。
- 升级规则。
- 停止门禁。

核心句子：

> Agent 不应该默认做下一步，而应该默认做到可验收状态。

## 6. 默认完成语义

未来应写入 Skill 顶层：

```text
Unless the user explicitly asks for analysis only, a coding request means:
understand the target, implement, verify, debug failures, re-verify, evaluate, and stop only at Done, Done with Risk, Blocked, or budget exhausted.
```

中文：

```text
除非用户明确只要求分析，否则编程任务默认包含理解目标、实现、验证、失败修复、再验证和完成判定。
Agent 只能在 Done、Done with Risk、Blocked 或预算耗尽时停止。
```

这条用于解决：

- 只做一步就结束。
- 改完不验证。
- 失败后等用户反馈。
- 口头宣布完成。

## 7. Plan 模式不够

Plan 模式解决的是：

```text
我要怎么做？
```

但完成任务还需要：

```text
我做了吗？
做完了吗？
验证了吗？
失败后继续了吗？
什么时候停止？
```

真正需要的是：

```text
Plan -> Action -> Verify -> Debug -> Re-verify -> Evaluate -> Continue / Stop
```

Plan 不能替代执行、验证、debug 和完成门禁。

## 8. 目标管理：大方向可以软，当前阶段必须硬

大项目不可能一开始就知道最终完整目标。

目标应分层：

```text
Direction / North Star
  -> Phase Target
    -> Sprint Goal
      -> Acceptance Criteria
```

核心原则：

> 大方向可以软，当前阶段必须硬。

建议模板：

- `DIRECTION.md`
- `TARGET.md`
- `ACCEPTANCE.md`
- `DECISIONS.md`

## 9. 项目类型分类

后续按这个分类决定启用哪些工具和流程：

| 项目类型 | 人类工程量 | AI loop | Agent 角色 |
| --- | ---: | ---: | --- |
| 小任务 | 0.5-2 人天 | 1-3 loops | 1 个 Agent |
| 中任务 | 3-10 人天 | 3-8 loops | Developer + Evaluator |
| 大项目 | 2 周以上 | 8+ loops | Planner + Developer + Evaluator |
| 产品级项目 | 1 月以上 | 多阶段 loops | 多 Agent + Runner + Rubric |

启用规则：

| 项目类型 | 必用 | 按需 |
| --- | --- | --- |
| 小任务 | `TARGET.md`、`ACCEPTANCE.md`、`EVALUATION.md` | `STOP_RULES.md` |
| 中任务 | 小任务全部 + Evaluator + 简版 `RUBRIC.md` | `QUALITY_VISION.md` |
| 大项目 | 中任务全部 + `DIRECTION.md`、阶段目标、`DECISIONS.md` | Runner |
| 产品级项目 | 大项目全部 + Runner + Rubric + Production System | MCP / dashboard / CI audit |

关键门禁：

- 小任务：目标清楚即可做，但必须验证。
- 中任务：不能只由 Developer 自评。
- 大项目：不能只写最终大目标，必须拆当前阶段目标。
- 产品级：不能靠聊天推进，必须靠 `Docs/`、Runner、Rubric 和审计。

## 10. 专家 Agent 的本质

“你是十年 QA 专家”不会打开模型中的某个固定模块，也不会修改参数。

它的作用是上下文软偏置：

- 更倾向 QA、测试、验收、风险、证据、边界条件。
- 更像训练数据中的资深 QA 输出模式。
- 但不保证真正严格执行。

更强写法：

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

## 11. MCP 的定位

MCP 是工具服务器协议，不是 Agent 管理者。

基本结构：

```text
Agent -> 调用工具
MCP Server -> 执行工具 / API / 本地能力
MCP Server -> 返回结构化结果
Agent -> 根据结果继续推理
```

MCP 有统一协议，但每个工具通过 schema 描述：

- name。
- description。
- inputSchema。
- required 参数。
- result。

对 `agent-loop-engineering` 的未来映射：

| Markdown 规则 | MCP Tool |
| --- | --- |
| 检查目标 | `validate_target()` |
| 判断状态 | `check_loop_state()` |
| 写入日志 | `append_loop_run()` |
| 判断停止 | `evaluate_stop_rules()` |
| 获取下一步 | `get_next_action()` |

## 12. Problem Solving 方法的抽象

PDCA、Five Whys、DMAIC、OODA、Definition of Done、Retrospective、Cynefin 等不应原样塞进 Skill。

抽象为 6 条 Agent 工作纪律：

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

## 13. 生产管理体系的启发

已讨论并记录：

- TPS
- TQC / TQM
- Six Sigma
- ISO 9001
- ISO 22000
- FSSC 22000
- HACCP / Codex
- FSMA
- GFSI
- 8D / Five Whys
- 食品生产管理体系

核心判断：

> 稳定、高质量、可复制的生产，不靠人或 Agent 自觉，而靠流程、标准、门禁、异常处理、审核和持续改善。

## 14. AI Coding Production System

已经新增：

- `references/ai-coding-production-system.md`

它把管理体系压缩为：

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

10 条控制规则：

| 规则 | 来源 |
| --- | --- |
| Direction Alignment | Hoshin Kanri / ISO 9001 |
| Standard Work | TPS / TQC |
| Built-in Quality | Jidoka / TQC |
| Just-in-Time Context | TPS JIT |
| Hazard Analysis | HACCP / ISO 22000 |
| Critical Control Points | HACCP / FSMA |
| Data-Driven Verification | Six Sigma / ISO |
| Root Cause Corrective Action | DMAIC / 8D / Five Whys |
| Traceability Records | ISO 22000 / FSSC |
| Continuous Improvement | Kaizen / PDCA / ISO |

## 15. 食品安全体系映射

食品安全体系非常适合借鉴，因为它处理的是：

- 低容错。
- 高风险。
- 多变量。
- 突发异常。
- 强追溯。
- 强审核。
- 持续改进。

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

核心规则：

```text
每个 coding loop 必须包含控制点、监控证据、失败纠正和验证记录。
关键控制点失败或未验证时，Agent 不允许继续假装完成，也不允许声明 Done。
```

## 16. 下一步路线

不要马上做 MCP。

推荐顺序：

```text
1. 更新 Skill 顶层规则
2. 增加 templates/
3. 增加 agent-loop-check
4. 增加 local runner
5. 稳定后再做 MCP
```

最重要的下一步：

```text
templates/
  EXECUTION_CONTRACT.md
  DIRECTION.md
  TARGET.md
  ACCEPTANCE.md
  LOOP_CONFIG.md
  STOP_RULES.md
  NEXT_ACTIONS.md
  EVALUATION.md
  RUBRIC.md
  QUALITY_VISION.md
```

之后做：

```text
scripts/agent-loop-check.ps1
```

检查：

- 是否有目标。
- 是否有验收标准。
- 是否有唯一下一步。
- 最新状态是否合法。
- `LOOP_RUNS.jsonl` 是否合法。
- 是否触发停止规则。
- 是否允许继续。

输出：

```text
Continue
Done
Done with Risk
Blocked
Invalid State
```

## 17. 当前最重要的未落地改动

应优先进入下一次 Skill 更新：

1. 在 `SKILL.md` 顶层加入默认完成语义。
2. 在 `SKILL.md` 顶层加入任务分类入口。
3. 增加 `templates/`。
4. 增加最小 checker 设计。
5. 后续再做 runner / MCP。

不要继续优先新增 reference。

## 18. 当前核心口号

可以作为后续 Skill 的顶层思想：

```text
大方向可以软，当前阶段必须硬。
Agent 可以自由写代码，但不能自由宣布完成。
没有验证，不允许 Done。
没有证据，不许自信。
异常即停止，失败要追根因。
不是让 Agent 做下一步，而是让 Agent 做到可验收状态。
```
