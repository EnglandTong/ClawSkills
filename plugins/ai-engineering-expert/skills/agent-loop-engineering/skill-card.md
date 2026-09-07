## Description: <br>
Execute an authorized software goal through low-context, bounded-autonomous AI coding loops with persistent state, proactive repair, automatic and functional evidence, layered stage review, independent final acceptance, safe workspace boundaries, and resumable handoffs. Stops on repeated failure signatures instead of retrying wider, and never downgrades a missing artifact into a pass. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[englandtong](https://clawhub.ai/user/englandtong) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators with a clear target and acceptance criteria use this skill to implement, debug, verify, and continue work autonomously across context loss, keeping one authoritative loop state and one writer per surface. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A loop could keep retrying a failing change and burn tokens or widen unintended scope. <br>
Mitigation: Stop on a repeated failure signature, cap repair attempts, and require an itemized dry run plus explicit Owner approval for destructive or migration operations. <br>
Risk: A stage could be marked done without its required artifact, producing false completion. <br>
Mitigation: Evidence downgrade is banned; a stage missing its required artifact is recorded as cannot-confirm, never as pass. <br>
Risk: Sensitive operational data could reach loop records or cloud services. <br>
Mitigation: Personal contact data, counterparty names, and contract or inspection details are never written into loop state; cloud upload requires explicit confirmation. <br>


## Reference(s): <br>
- [Agent Loop Engineering ClawHub listing](https://clawhub.ai/englandtong/agent-loop-engineering) <br>
- [Quickstart](QUICKSTART.md) <br>
- [Execution Loop](references/en/execution-loop.md) <br>
- [Evidence And Completion](references/en/evidence-and-completion.md) <br>
- [Safety And Context](references/en/safety-and-context.md) <br>
- [Anti-Patterns](references/en/anti-patterns.md) <br>
- [Migration Guide](references/en/migration.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, structured records] <br>
**Output Format:** [Markdown plus loop-state and evidence files under the project Docs/ directory] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local loop-state, stage-evidence, and work-order files when the user asks the agent to run or resume an autonomous loop.] <br>

## Skill Version(s): <br>
2.2.0 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
