### Recommended setup

- [Codebase Memory MCP](https://github.com/DeusData/codebase-memory-mcp)
- [Karpathy Guidelines skill](https://github.com/multica-ai/andrej-karpathy-skills/blob/main/skills/karpathy-guidelines/SKILL.md)
- [Ponytail plugin](https://github.com/dietrichgebert/ponytail)
- [Google developer documentation style skill](https://github.com/aaarrti/codex-skills/blob/main/skills/google-developer-documentation-style/SKILL.md)

### Guidelines

- This project is for private use. Do not add backward-compatibility layers or
  fallbacks.
- For Python scripts, do not add a shebang or `from __future__` imports.
- Write Python tests with `pytest`, not `unittest`.
- Implement work in small, incremental changes.
- When a task changes multiple files, fan out sub-agents to parallelize the
  work.

### Documentation

Use the Google developer documentation style skill when writing or editing
project documentation.