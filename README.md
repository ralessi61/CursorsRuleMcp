# Cursor Rules + MCP sample (Python)

## Try it
1. Open this folder in Cursor and set up Python:
   `python -m venv .venv && source .venv/bin/activate && pip install -e ".[dev]"`, then run `pytest`.
2. Rules: ask the chat "write tests for src/utils.py". The `tests.mdc` rule makes it use pytest with error cases.
3. MCP: set `GITHUB_PERSONAL_ACCESS_TOKEN` in your environment, then check Cursor Settings > MCP to see `github` and `postgres` enabled.
   Ask: "Summarise open issues labelled bug in <owner>/<repo>".
4. The postgres server needs a local database at `postgresql://localhost/mydb` (edit the URL in `.cursor/mcp.json`).

Note: the `github` and `postgres` MCP servers are launched with `npx`, so Node.js must be installed
just to start them. The project code itself is pure Python. A custom MCP server written in Python is in
`examples/mcp-server-python`.

## Files
- `src/utils.py` - sample code (`divide`, async `fetch_user`)
- `tests/test_utils.py` - pytest tests
- `pyproject.toml` - project metadata and dev dependencies
- `.cursor/rules/style.mdc` - always-on style rule
- `.cursor/rules/tests.mdc` - applies only to test files (`tests/**/*.py`, `**/test_*.py`)
- `.cursor/rules/database.mdc` - rule that tells the AI when to use the postgres MCP tool
- `.cursor/mcp.json` - MCP server config
- `docs/` and `examples/` - extended Italian docs and examples

## Note: temporary GitHub token
This repo was pushed using a temporary fine-grained GitHub personal access token
(scoped to this repository only, Contents: read and write, short expiry).
The token is intentionally NOT stored in this repo. Revoke it at
https://github.com/settings/personal-access-tokens once it is no longer needed.
Never commit tokens; for MCP use the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.
