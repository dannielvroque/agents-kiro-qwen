---
inclusion: manual
---

# Incident / Production Troubleshooting — Local AI Second Opinion

Use `ask_local_ai` for production incidents, outages and difficult troubleshooting.

The local AI should work from evidence rather than guessing.

Provide, when available:

- Symptoms
- Timeline
- Recent changes
- Logs
- Metrics
- Alerts
- Error messages
- Infrastructure state
- Affected services
- Scope of impact

Ask the local AI to return:

1. Most likely hypotheses
2. Evidence supporting each
3. Evidence against each
4. Additional diagnostics
5. Safe mitigation options
6. Risks of each mitigation
7. Root-cause investigation steps
8. Follow-up/prevention ideas

Do not treat a hypothesis as confirmed until evidence supports it.

During production incidents, prefer reversible and low-risk actions.

Do not restart, delete, scale down, destroy or modify production resources without explicit authorization and validation.
