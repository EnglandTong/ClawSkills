# AI Coding Management System：把 AI Agent 当作“能力强但缺少工作纪律的新人员工”来管理

这不是一个“发明”，而是一个基于实践经验的研究方向。

我做了 20 年采购、新品研发和食品生产。长期经验告诉我：稳定的品质不能靠人自觉，必须靠目标、SOP、风险前置、检查、异常处理、review 和 action plan。

最近使用 AI Coding Agent 做开发时，我发现它们很像能力很强但缺少工作经验的新人员工：

- 知识很多，执行很快；
- 会写代码，也会找问题；
- 但不一定主动复核；
- 不一定追根因；
- 容易只做一步就停；
- 容易在没有验证时说 Done；
- 长程任务中容易目标漂移；
- 上下文压缩后容易忘记关键约束。

所以我开始思考：能否像管理生产和品质一样，管理 AI Coding Agent？

这个方向暂时叫：

> CMS: AI Coding Management System

CMS 的核心不是让 Agent “更听话”，而是让 AI Coding 过程变得可控制、可验证、可追溯、可复盘。

## 核心假设

AI Coding 的主要问题不是模型不会写代码，而是：

> Agent 缺少稳定的工作纪律和外部管理系统。

因此，CMS 尝试把这些机制引入 AI Coding：

- 目标合同；
- 验收标准；
- 证据优先；
- 无验证不允许 Done；
- 异常即停止；
- 失败要追根因；
- 状态记录；
- 独立检查；
- 持续改善。

## CMS Lite v0.1

为了避免过度工程化，第一版只做最小实验。

测试阶段使用 4 个文件：

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  LOOP_STATE.md
  LOOP_LOG.jsonl
```

再加一个确定性 checker：

```text
agent-loop-check.ps1
```

它不判断代码好不好，只检查 Agent 有没有满足最基本的工作纪律：

- 有没有目标；
- 有没有验收标准；
- 状态是否合法；
- Done 是否有证据；
- Continue 是否有唯一下一步；
- Blocked 是否有原因；
- 日志是否可解析；
- scenario 判断和代码规模是否可追踪。

## 要测试的问题

我准备先跑三个场景：

| Scenario | Goal |
| --- | --- |
| Small bug fix | CMS Lite 会不会太重 |
| Medium feature | evidence gate 是否减少假完成 |
| Long refactor | loop state 是否减少目标漂移 |

## 我希望大家讨论

这不是标准，也不是结论，而是一个开放研究方向。

我想听到反对意见：

- 这是不是过度工程化？
- 小任务是否应该完全不用 Docs？
- 4 个文件是否仍然太多？
- checker 应该检查到什么程度？
- 证据应该如何定义？
- Agent 是否真的需要像新人一样管理？
- 哪些场景会证明 CMS 无效？

如果你也在使用 Codex、Claude Code、OpenCode、Cursor、Cline、Aider、Gemini CLI 或其他 AI Coding 工具，欢迎用真实任务测试这个思路。

我的目标不是证明 CMS 一定正确，而是验证：

> 一个轻量的目标、验收、状态、日志和 checker，能否减少 AI Coding Agent 的假完成、目标漂移和无证据交付。

