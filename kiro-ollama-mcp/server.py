import json
import urllib.request
from mcp.server.mcpserver import MCPServer

OLLAMA_URL = "http://localhost:11434"
DEFAULT_MODEL = "qwen2.5-coder:14b"
KEEP_ALIVE = "15m"

mcp = MCPServer("ollama-local")


def ollama_generate(model: str, prompt: str) -> str:
    payload = json.dumps({
        "model": model,
        "prompt": prompt,
        "stream": False,
        "keep_alive": KEEP_ALIVE
    }).encode("utf-8")

    request = urllib.request.Request(
        f"{OLLAMA_URL}/api/generate",
        data=payload,
        headers={
            "Content-Type": "application/json"
        },
        method="POST"
    )

    with urllib.request.urlopen(request, timeout=300) as response:
        data = json.loads(response.read().decode("utf-8"))

    return data.get("response", "")


@mcp.tool()
def ask_local_ai(prompt: str) -> str:
    """
    Ask the local Qwen2.5-Coder 14B for a second opinion.

    The local AI is specialized in software development,
    code review, debugging, performance and testing.

    It must prioritize real and relevant problems and
    avoid speculative or unnecessary recommendations.
    """

    enhanced_prompt = f"""
You are a senior software engineer performing a second-opinion
analysis for another AI coding agent.

Analyze the provided request/code carefully.

Priorities:
- Find real and relevant problems.
- Do not invent problems.
- Do not recommend premature optimization.
- Distinguish real bugs from style preferences.
- Consider the existing context before making recommendations.

For code analysis, consider:

1. Memory leaks and memory safety
2. Undefined behavior
3. Race conditions
4. Thread safety and concurrency
5. Performance
6. Error handling
7. Security
8. Maintainability
9. Code smells
10. Refactoring opportunities

For every relevant problem found, provide:

- Severity: Critical / High / Medium / Low / Informational
- Location
- Problem
- Why it matters
- Recommended solution

If a category has no relevant problems, explicitly say so.

Do not modify files.
Do not rewrite the entire code unless specifically requested.

USER REQUEST:
{prompt}
"""

    return ollama_generate(DEFAULT_MODEL, enhanced_prompt)


@mcp.tool()
def local_ai_status() -> str:
    """
    Check whether the local Ollama server is available
    and list installed models.
    """

    try:
        request = urllib.request.Request(
            f"{OLLAMA_URL}/api/tags",
            method="GET"
        )

        with urllib.request.urlopen(request, timeout=5) as response:
            data = json.loads(response.read().decode("utf-8"))

        models = [
            model.get("name")
            for model in data.get("models", [])
        ]

        return (
            "Ollama is running.\n"
            f"Default model: {DEFAULT_MODEL}\n"
            f"Keep alive: {KEEP_ALIVE}\n"
            f"Available models: {', '.join(models)}"
        )

    except Exception as error:
        return f"Ollama is not available: {error}"


if __name__ == "__main__":
    mcp.run()