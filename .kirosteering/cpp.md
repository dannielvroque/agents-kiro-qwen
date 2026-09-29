---
inclusion: manual
---

# C++ — Local AI Second Opinion

Use `ask_local_ai` for advanced C++ analysis.

Prioritize:

- Memory leaks
- Use-after-free
- Double-free
- Dangling references/pointers
- Undefined behavior
- Buffer overflows
- Ownership
- RAII
- Smart pointers
- Object lifetime
- Exception safety
- Thread safety
- Race conditions
- Deadlocks
- Data races
- STL usage
- Move semantics
- Copy semantics
- ABI concerns
- Performance
- Error handling

Distinguish real correctness problems from style preferences.

Prefer modern, maintainable C++ when compatible with the project's compiler, standard and constraints.

Do not recommend micro-optimizations without evidence of a meaningful bottleneck.
