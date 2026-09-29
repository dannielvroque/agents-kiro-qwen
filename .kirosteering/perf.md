---
inclusion: manual
---

# Local Performance Review

Use `ask_local_ai` to analyze the relevant code for performance.

Ask the local Qwen2.5-Coder 14B to investigate:

- unnecessary allocations
- copies
- memory usage
- algorithmic complexity
- unnecessary I/O
- locking and contention
- CPU-intensive operations
- inefficient data structures
- caching opportunities
- unnecessary network calls

Do not modify the code.

Clearly distinguish measured problems from theoretical optimization opportunities.