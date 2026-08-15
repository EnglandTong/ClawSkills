# Agent Loop / CMS 2.1.1

## Agent Loop Engineering 2.1.1

- Isolates high-output exploration, logs, validation, and independent QA in bounded workers.
- Limits normal concurrency to three workers and preserves one coordinating writer.
- Sends authority fingerprints and required excerpts instead of full governance history.
- Requires structured summary-and-evidence returns without hidden reasoning or full command output.
- Adds portable session-cost controls and a Claude Code adapter without hard-coding volatile prices or limits.
- Validates parallel-agent limits while retaining `contract_version: "2.0"` and `record_version: "2.1"` compatibility.

## CMS Project Governance 2.1.1

- Authorizes isolated workers only for separable, high-output work.
- Keeps small or tightly coupled work in the main execution loop.
- Enforces disjoint parallel Work Orders, single-writer governance, compact authority sharing, and independent final QA.

