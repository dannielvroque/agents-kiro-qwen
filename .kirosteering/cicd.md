---
inclusion: manual
---

# CI/CD — Local AI Second Opinion

Use `ask_local_ai` for CI/CD pipelines and deployment automation.

Relevant systems include:

- GitHub Actions
- GitLab CI
- Jenkins
- Docker builds
- Terraform pipelines
- Kubernetes deployments
- AWS deployments

Analyze:

- Pipeline correctness
- Dependency ordering
- Caching
- Artifacts
- Secrets
- Permissions
- Environment separation
- Reproducibility
- Rollback
- Failure handling
- Parallelism
- Build time
- Deployment safety

Prefer small, deterministic and observable pipelines.

Never expose credentials or secrets in logs.

When proposing changes, explain how the pipeline behaves on success and failure.
