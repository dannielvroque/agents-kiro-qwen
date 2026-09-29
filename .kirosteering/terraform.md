---
inclusion: manual
---

# Terraform / IaC — Local AI Second Opinion

Use `ask_local_ai` for Terraform and Infrastructure-as-Code analysis.

Analyze:

- Provider configuration
- Resources
- Modules
- Variables and outputs
- Dependencies
- State management
- Remote backends
- Lock files
- Workspaces
- Provider aliases
- IAM
- Networking
- Naming
- Reusability
- Drift
- Plan/apply risks
- Security
- CI/CD integration

When debugging Terraform, distinguish:

- Configuration errors
- Provider errors
- State problems
- AWS/API errors
- Dependency issues
- Permission issues

Do not recommend `terraform destroy`, state deletion or state manipulation without clearly explaining the risk.

Prefer `terraform fmt`, `validate`, `plan` and targeted inspection before changes.

For provider/resource behavior that may have changed, verify current official documentation.
