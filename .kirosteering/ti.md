---
inclusion: manual
---

# TI — Local AI Second Opinion

Use `ask_local_ai` whenever the task involves technology, software development, infrastructure or DevOps.

The local Qwen2.5-Coder 14B is a SECOND OPINION. Kiro remains responsible for the final analysis, decisions and implementation.

## Workflow

1. Understand the request and inspect relevant context.
2. Build a concise technical question for the local AI.
3. Call `ask_local_ai`.
4. Include only relevant context: code, logs, versions, architecture, constraints and expected/actual behavior.
5. Critically evaluate the response.
6. Compare it with your own analysis.
7. Discard incorrect, speculative or irrelevant findings.
8. Provide the final practical answer.

## Priorities

Correctness, security, reliability, maintainability, performance, simplicity and operational impact.

Do not invent APIs, configuration options, errors or features. Clearly separate facts, assumptions and hypotheses.

The local AI must not directly modify project files.

For current or version-specific facts, verify official documentation or current sources when appropriate.
