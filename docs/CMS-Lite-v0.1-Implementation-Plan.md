# CMS Lite v0.1 Implementation Plan

状态：Draft, Step 5 updated  
日期：2026-06-10  
用途：根据多个 Agent 对 CMS 文档的审阅意见，做减法、整理共识，并定义下一步最小可执行实现路线。

## 1. Review Consensus

不同 Agent 的反馈高度一致：

| 判断 | 结论 |
| --- | --- |
| CMS 方向 | 成立，值得继续 |
| 核心类比 | “能力强但缺少工作纪律的新人”准确 |
| 最大价值 | 防止假完成、目标漂移、无证据自信、不追根因 |
| 最大风险 | 方法论膨胀、文件过多、实现路径过度工程化 |
| 当前状态 | 仍是软协议和文档体系 |
| 下一步 | 不再证明理论，转向 templates + checker |
| MCP | 延后，等 checker / runner 稳定后再工具化 |

最重要的外部反馈：

> CMS 最大的问题不是想法错，而是目前方法论远超实现。下一步要证明它真的能管住 Agent。

## 2. Subtraction Decisions

### 2.1 Keep

保留这些核心：

- Agent 是“知识丰富、执行快、但工作纪律不足的新人员工”。
- 默认完成语义。
- Verify Before Done。
- Evidence Before Confidence。
- Stop Rules。
- Continue / Done / Done with Risk / Blocked / Invalid State。
- 项目分级。
- 渐进式治理。
- Checker 优先。

### 2.2 Reduce

压缩这些内容：

| 原内容 | 减法处理 |
| --- | --- |
| TPS / TQC / Six Sigma / ISO / HACCP 等大段映射 | 保留为背景 reference，不进入 MVP 主流程 |
| 多 Agent 完整角色体系 | 中任务以上再启用 |
| 15+ 个 `Docs/` 文件 | 测试阶段压到 4 个文件 |
| Runner / MCP / Dashboard | 延后 |
| Production System 术语 | 对外表达时转成“target / evidence / checker / stop rules” |

### 2.3 Stop Doing

暂时停止：

- 继续新增 reference。
- 继续扩写 CMS 理论文档。
- 先做 MCP。
- 先做 dashboard。
- 小任务默认启用完整 Docs。

## 3. CMS Lite v0.1 Goal

CMS Lite v0.1 只解决一个核心问题：

> 防止 AI Coding Agent 在目标不清、没有验证、没有证据或状态不可信时宣布完成或继续自动运行。

不是目标：

- 不做完整多 Agent 平台。
- 不做 MCP server。
- 不做 dashboard。
- 不做复杂质量评分。
- 不做所有生产管理方法论的落地。

## 4. Minimum File Set

CMS Lite v0.1 测试阶段使用 4 个必需文件：

```text
Docs/
  TARGET.md
  ACCEPTANCE.md
  LOOP_STATE.md
  LOOP_LOG.jsonl
```

`LOOP_LOG.jsonl` 在测试阶段是必需文件。它用于记录可观察的 decision/evidence trace，例如 scenario 判断、是否使用 `agent-loop-engineering`、创建或更新了哪些模板、读写了哪些文件、运行了哪些命令、收集了哪些证据、`agent-loop-check` 的结果。不要记录模型隐藏 chain-of-thought。

### 4.1 TARGET.md

用途：定义当前目标和边界。

最小结构：

```markdown
# Target

## Goal

## Non-Goals

## Current Scope
Small / Medium / Large / Product

## Human Decisions Required
```

### 4.2 ACCEPTANCE.md

用途：定义什么叫完成，必须可验证。

最小结构：

```markdown
# Acceptance

## Must Pass
- [ ] 

## Evidence Required
- Automatic:
- Functional:

## Failure Examples
- 
```

### 4.3 LOOP_STATE.md

用途：合并当前状态、验证证据、失败原因、下一步和停止状态，避免 MVP 阶段文件过多。

最小结构：

```markdown
# Loop State

## Status
Continue / Done / Done with Risk / Blocked / Invalid State

## Last Action

## Evidence
- Command:
- Result:
- Functional check:
- Logs / screenshots / files:

## Failed Checks

## Root Cause

## Next Action
Only one next action allowed.

## Stop Rule Triggered
Yes / No
Reason:
```

## 5. State Rules

允许状态：

| State | Meaning | User-facing |
| --- | --- | --- |
| Continue | 仍有明确下一步，且未触发停止门禁 | Yes |
| Done | 验收满足，有足够证据 | Yes |
| Done with Risk | 核心完成，但有明确风险或未验证边界 | Yes |
| Blocked | 需要人提供信息、权限、环境或决策 | Yes |
| Invalid State | 状态文件不可信，不能继续自动运行 | No, internal checker state |

`Invalid State` 只给 checker / runner 使用，不作为正常交付状态。

## 5.1 Required Test Loop Log

`LOOP_LOG.jsonl` 用于测试者不确定当前任务属于哪种 scenario 时的逐个验证。测试阶段必须创建该文件，后续正式使用时可根据项目等级决定是否保留为必需项。

推荐 JSONL 字段：

```json
{
  "timestamp": "2026-06-10T00:00:00Z",
  "event": "loop_start | template_update | command_run | evidence_added | checker_run | loop_end",
  "agent": "agent-name",
  "scenario_guess": "Small | Medium | Large | Product | Unknown",
  "skill_used": "agent-loop-engineering",
  "templates_used": ["TARGET.md", "ACCEPTANCE.md", "LOOP_STATE.md"],
  "files_read": [],
  "files_written": [],
  "commands": [],
  "evidence": [],
  "checker_result": "Continue | Done | Done with Risk | Blocked | Invalid State | Not run",
  "code_size": {
    "size_class": "Small | Medium | Large | Product | Unknown",
    "code_files": 0,
    "code_lines": 0,
    "changed_files": "unknown"
  },
  "notes": "Short observable summary"
}
```

Checker v0.1 在测试阶段必须检查该文件存在且为合法 JSONL。

Checker v0.2 增加 strict evidence gate。测试 `Done` 时，`LOOP_LOG.jsonl` 应记录机器可读的 `verification_commands[]`，包括 `kind`、`command`、`exit_code`、`summary` 和 `verified_at`。`-Strict` 模式下，`Done` 至少需要一个成功的 `automatic` 验证和一个成功的 `functional` 验证。

## 6. Minimum Checker

第一版 checker 只做确定性检查，不做复杂 AI 判断。v0.2 仍保持确定性，但增加验证命令与 exit code 绑定。

建议名称：

```text
scripts/agent-loop-check.ps1
```

输入：

```text
Docs/TARGET.md
Docs/ACCEPTANCE.md
Docs/LOOP_STATE.md
Docs/LOOP_LOG.jsonl
```

输出：

```text
Continue
Done
Done with Risk
Blocked
Invalid State
```

### 6.1 Checker Rules

最小规则：

| Rule | Failed result |
| --- | --- |
| `TARGET.md` missing or empty | Invalid State |
| `ACCEPTANCE.md` missing or empty | Invalid State |
| `LOOP_STATE.md` missing or empty | Invalid State |
| `LOOP_LOG.jsonl` missing or empty in test mode | Invalid State |
| Status not in allowed enum | Invalid State |
| Status = Done but evidence section empty | Invalid State |
| Status = Done but failed checks not empty | Invalid State |
| Status = Continue but next action missing | Invalid State |
| Status = Continue but multiple next actions found | Invalid State |
| Status = Blocked but no reason | Invalid State |
| Stop rule triggered = Yes and status is Continue / Done | Invalid State |
| `LOOP_LOG.jsonl` is not valid JSONL | Invalid State |
| `LOOP_LOG.jsonl` record misses required fields | Invalid State |
| `LOOP_LOG.jsonl` record has invalid `scenario_guess` | Invalid State |

### 6.2 What Checker Should Not Do in v0.1

Do not make the checker judge:

- Whether the code is elegant.
- Whether the solution is optimal.
- Whether acceptance criteria are semantically perfect.
- Whether UI looks good.
- Whether architecture is ideal.

### 6.3 Checker v0.2 / Step 5 Evidence Gate

Add:

- `-Strict` parameter.
- JSON output fields: `checkerVersion`, `strict`, `warnings`, `log.successfulAutomatic`, and `log.successfulFunctional`.
- `Done -Strict` requires at least one successful automatic verification and one successful functional verification.
- `verification_commands[].exit_code` must be numeric.
- `verification_commands[].verified_at` or record-level `verified_at` must exist.
- `scenario_guess` and code size mismatch should produce a warning, not `Invalid State`.

Important boundary:

> checker `Done` means the `Docs/` state and evidence record satisfy the protocol. It does not prove product behavior, UI, architecture, or user experience is truly complete.
- Whether code size alone proves the scenario type.

Those require Evaluator / Rubric later. v0.1 checks state integrity and evidence presence only.

## 7. Skill Changes Needed

`agent-loop-engineering` should be updated with only three top-level additions:

1. Default completion semantics.
2. Task classification entry.
3. CMS Lite file strategy.

Do not add another long reference.

### 7.1 Default Completion Semantics

```text
Unless the user explicitly asks for analysis only, a coding request means:
understand the target, implement, verify, debug failures, re-verify, evaluate, and stop only at Done, Done with Risk, Blocked, or budget exhausted.
```

### 7.2 Task Classification

```text
Classify before choosing workflow:
- Small task: one Agent, 1-3 loops
- Medium task: Developer + Evaluator, 3-8 loops
- Large project: Planner + Developer + Evaluator, 8+ loops
- Product-level: multi-agent + runner + rubric
```

### 7.3 CMS Lite File Strategy

```text
For CMS Lite v0.1, start with:
- Docs/TARGET.md
- Docs/ACCEPTANCE.md
- Docs/LOOP_STATE.md

Only split LOOP_STATE.md into STATUS, NEXT_ACTIONS, PENDING, EVALUATION, and LOOP_RUNS.jsonl when the project grows beyond CMS Lite.
```

## 8. Step-by-Step Implementation

### Step 1: Freeze Theory

Decision:

- No more new references for now.
- Treat `CMS-Coding-Management-System.md` as review draft.
- Treat `CMS-Lite-v0.1-Implementation-Plan.md` as implementation source.

Exit condition:

- User approves CMS Lite v0.1 scope.

### Step 2: Add Templates

Add:

```text
skills/agent-loop-engineering/templates/TARGET.md
skills/agent-loop-engineering/templates/ACCEPTANCE.md
skills/agent-loop-engineering/templates/LOOP_STATE.md
```

Exit condition:

- Templates are short, practical, and match checker rules.

### Step 3: Update SKILL.md

Update:

- Add default completion semantics near top.
- Add task classification table.
- Add CMS Lite file strategy.
- Keep production-system references as optional, not required per loop.

Exit condition:

- Skill entry remains concise.
- No new long reference is required.

### Step 4: Build Checker v0.1

Add:

```text
skills/agent-loop-engineering/scripts/agent-loop-check.ps1
```

Checker should:

- Read a workspace path.
- Validate the four CMS Lite files.
- Validate the required test log `Docs/LOOP_LOG.jsonl`.
- Estimate rough code size from source file count, source line count, and git changed file count when available.
- Print one final state.
- Return nonzero exit code for `Invalid State`.

Run command:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File skills/agent-loop-engineering/scripts/agent-loop-check.ps1 -WorkspacePath <project>
```

Exit condition:

- Script can detect missing files, invalid status, invalid JSONL log, missing log fields, invalid scenario guess, rough code size, Done without evidence, Continue without next action, and Blocked without reason.

### Step 5: Run Three Test Scenarios

Use real tasks:

| Scenario | Goal |
| --- | --- |
| Small bug fix | Check whether CMS Lite is too heavy |
| Medium feature | Check whether evidence gate reduces false Done |
| Long refactor | Check whether loop state prevents target drift |

Exit condition:

- Record what worked and what was too heavy.
- Revise templates / checker only from evidence.

### Step 6: Decide Runner

Only after checker works:

- Design local runner.
- Runner starts next loop only if checker returns `Continue`.
- Runner stops on `Done`, `Done with Risk`, `Blocked`, or `Invalid State`.

Exit condition:

- Runner does not make quality decisions itself; it only enforces checker output and budget.

## 9. What to Change in Existing Docs

Later cleanup:

| File | Action |
| --- | --- |
| `CMS-Coding-Management-System.md` | Keep as architecture draft, but add pointer to CMS Lite plan |
| `agent-loop-24h-temp-notes.md` | Archive or delete after decisions are merged |
| `agent-loop-engineering-knowledge.md` | Keep as knowledge base, not execution spec |
| `ai-coding-production-system.md` | Keep optional reference, not per-loop input |

## 10. Current Best Next Action

The next actual implementation should be:

```text
Create CMS Lite v0.1 templates:
- TARGET.md
- ACCEPTANCE.md
- LOOP_STATE.md

Then implement agent-loop-check.ps1.
```

Do not implement Runner or MCP before the checker proves useful.

## 11. Success Criteria for CMS Lite v0.1

CMS Lite v0.1 succeeds if it reliably blocks these cases:

- Agent claims Done without evidence.
- Agent claims Done while failed checks exist.
- Agent continues without a single clear next action.
- Agent starts work without target or acceptance.
- Agent marks Blocked without explaining what human input is needed.
- State file is malformed or unparseable.

If it blocks those cases, CMS has moved from theory to practical control.
