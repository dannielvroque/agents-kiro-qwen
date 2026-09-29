---
inclusion: manual
---

# Linux — Local AI Second Opinion

Use `ask_local_ai` for Linux administration, troubleshooting and scripting.

Analyze:

- Processes
- Services/systemd
- Permissions
- Users/groups
- Filesystems
- Disk usage
- Memory
- CPU
- Networking
- DNS
- Ports
- Logs
- SSH
- Shell scripts
- Package management
- Containers
- Resource limits

For incidents, prefer evidence from commands such as:

- ps
- top
- free
- df
- du
- ss
- ip
- journalctl
- systemctl
- dmesg
- curl

Do not suggest destructive commands without explaining their impact.

When commands may vary by distribution/version, identify the assumption.
