# Cursor Rules + MCP sample

## Try it
1. Open this folder in Cursor and run `npm install`.
2. Rules: ask the chat "write tests for src/utils.ts". The `tests.mdc` rule makes it use Vitest with error cases.
3. MCP: set `GITHUB_PERSONAL_ACCESS_TOKEN` in your environment, then check Cursor Settings > MCP to see `github` and `postgres` enabled.
   Ask: "Summarise open issues labelled bug in <owner>/<repo>".
4. The postgres server needs a local database at `postgresql://localhost/mydb` (edit the URL in `.cursor/mcp.json`).

## Files
- `.cursor/rules/style.mdc` - always-on style rule
- `.cursor/rules/tests.mdc` - applies only to `*.test.ts`
- `.cursor/rules/database.mdc` - rule that tells the AI when to use the postgres MCP tool
- `.cursor/mcp.json` - MCP server config

## Note: temporary GitHub token
This repo was pushed using a temporary fine-grained GitHub personal access token
(scoped to this repository only, Contents: read and write, short expiry).
The token is intentionally NOT stored in this repo. Revoke it at
https://github.com/settings/personal-access-tokens once it is no longer needed.
Never commit tokens; for MCP use the `GITHUB_PERSONAL_ACCESS_TOKEN` environment variable.
