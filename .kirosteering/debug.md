---
inclusion: manual
---

# Local Debugging

Use `ask_local_ai` to investigate the bug described by the user.

First understand the relevant code and reproduce the context.

Send the relevant code, error messages, stack traces and important context
to the local Qwen2.5-Coder 14B.

Ask the local AI to identify:

- likely root cause
- possible secondary causes
- incorrect assumptions
- edge cases
- recommended debugging steps
- possible fix

Do not modify files until the user explicitly asks for a fix.

After receiving the response, the primary Kiro agent must validate the findings.