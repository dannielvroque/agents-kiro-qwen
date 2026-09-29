---
inclusion: manual
---

# Local Code Review

Use `ask_local_ai` to perform a code review of the relevant code.

Ask the local Qwen2.5-Coder 14B to analyze:

1. Memory leaks
2. Undefined behavior
3. Race conditions
4. Thread-safety and concurrency
5. Performance problems
6. Error handling
7. Security problems
8. Maintainability
9. Code smells
10. Refactoring opportunities

Do not modify files.

Return the local AI findings clearly categorized by severity:

- Critical
- High
- Medium
- Low
- Informational

After receiving the local AI response, the primary Kiro agent should review
the findings and point out which findings are confirmed, uncertain, or incorrect.