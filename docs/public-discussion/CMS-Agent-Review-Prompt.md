# CMS Agent Review Prompt

Use this prompt when asking another AI Agent to review CMS.

```text
Please review the attached AI Coding Management System (CMS) materials neutrally.

Context:
- CMS is not claimed as an invention or finished standard.
- It is a research direction based on practical experience in purchasing, new product development, food production, quality control, SOP, risk prevention, abnormal handling, review, and action planning.
- The core idea is to manage AI coding agents as fast, knowledgeable, but inexperienced workers.
- The current MVP is CMS Lite v0.1.

Please focus on subtraction and implementation:

1. What should be removed or simplified?
2. Is CMS Lite v0.1 still too heavy?
3. Are these four files reasonable for testing?
   - TARGET.md
   - ACCEPTANCE.md
   - LOOP_STATE.md
   - LOOP_LOG.jsonl
4. Is the checker scope reasonable?
5. Is Invalid State useful as checker-only status?
6. What risks exist if the checker is deterministic only?
7. What should not be implemented yet?
8. Should MCP wait until checker and runner are stable?
9. What is the smallest test that could prove CMS Lite useful?
10. What is the smallest test that could disprove it?

Please avoid generic praise. Lead with risks, flaws, overengineering concerns, and concrete implementation suggestions.
```

