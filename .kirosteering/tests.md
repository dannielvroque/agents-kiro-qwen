---
inclusion: manual
---

# Local Test Assistant

Use `ask_local_ai` to analyze the relevant code and propose tests.

Ask the local Qwen2.5-Coder 14B to identify:

- missing unit tests
- edge cases
- invalid inputs
- boundary conditions
- error paths
- concurrency cases
- regression tests

If the user asks to generate tests, provide the relevant existing code
and testing framework context to the local AI.

The primary Kiro agent remains responsible for implementing and validating
the tests.