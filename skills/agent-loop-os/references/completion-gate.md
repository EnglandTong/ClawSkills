# Completion Gate

Use this before declaring a loop or task complete.

## Completion States

### Done

Use `Done` only when:

- Every must-pass success criterion in `Docs/ACCEPTANCE.md` is satisfied.
- The implementation remains inside `Docs/TARGET.md` scope.
- Automatic verification passed, such as tests, typecheck, build, lint, or syntax checks.
- Functional verification passed, such as a manual flow, sample input/output, screenshot, API call, or acceptance scenario.
- Remaining risks are minor and do not affect the stated target.

### Done with Risk

Use `Done with Risk` when:

- The core goal appears satisfied.
- At least one important check, environment path, edge case, or manual confirmation is missing.
- The missing evidence is clearly recorded.
- The next human or agent can reproduce what was verified and what remains uncertain.

### Blocked

Use `Blocked` when:

- Completion cannot be judged from available evidence.
- A required permission, credential, account, environment, production resource, or human decision is missing.
- A hard stop rule is triggered.
- The loop cannot safely continue within budget.

### Continue

Use `Continue` when:

- The target is clear.
- No hard stop is triggered.
- Budget remains.
- One concrete next action exists.

## Evidence Classes

Prefer at least two evidence classes for `Done`:

- Automatic verification: tests, typecheck, build, lint, syntax validation.
- Functional verification: sample run, UI flow, API request, screenshot, fixture, acceptance scenario.
- Code review evidence: diff review, risk review, dead-code/security review.
- Documentation/handoff evidence: updated usage notes, status, evaluation, or handoff.

`Done` requires automatic verification plus functional verification unless the project explicitly has no runnable artifact. If no runnable artifact exists, record why and use review/documentation evidence instead.

## Functional Verification By Project Type

- Frontend app: render the changed page or component, exercise the main interaction, and capture screenshot or browser evidence when possible.
- API service: run a request against the changed endpoint or a representative integration test.
- CLI: run `--help` plus one core command with sample input.
- Library or SDK: import the package and call the changed public function in a test or small sample.
- Data pipeline: run a dry-run, sample transform, fixture-based job, or query preview.
- Infrastructure/config: run plan, validate, dry-run, or static policy check.
- Documentation-only or skill-only project: run structural validation and review the rendered or linked documentation paths.

## No Runnable Artifact

A project has no runnable artifact only when it is purely documentation, prompt/skill text, policy, configuration guidance, or static reference material. Record this in `Docs/EVALUATION.md` and replace functional verification with review/documentation evidence.

## Evaluation Template

```markdown
## Completion Gate

- State: Done / Done with Risk / Blocked / Continue
- Target alignment:
- Success criteria:
- Non-goals preserved:
- Automatic verification:
- Functional verification:
- Risks:
- Missing evidence:
- Next action:
```
