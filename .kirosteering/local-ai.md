---
inclusion: manual
---

# Local AI

Use the `ask_local_ai` MCP tool to ask the local Ollama AI
(Qwen2.5-Coder 14B) for a second opinion.

The local AI is an auxiliary reviewer, not the primary agent.

Always:
- Read the relevant project files first.
- Send the relevant code and context to `ask_local_ai`.
- Clearly identify that the response came from the local AI.
- Do not modify files unless the user explicitly asks.
- Treat the local AI response as a second opinion and verify important findings yourself.