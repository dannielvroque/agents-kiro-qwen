---
inclusion: manual
---

# Security — Local AI Second Opinion

Use `ask_local_ai` for security analysis.

Consider:

- Authentication
- Authorization
- Least privilege
- Secrets management
- Credentials
- Input validation
- Injection
- Command execution
- SSRF
- Path traversal
- Dependency vulnerabilities
- TLS
- Encryption
- Network exposure
- Logging sensitive information
- Container security
- Cloud IAM
- API security

Classify findings as:

- Critical
- High
- Medium
- Low
- Informational

Do not claim a vulnerability without evidence or a plausible attack path.

For security-sensitive changes, Kiro must validate the finding before implementation.

Never print, commit or expose credentials, tokens or private keys.
