# memos-mcp-server
[![smithery badge](https://smithery.ai/badge/@LeslieLeung/mcp-server-memos)](https://smithery.ai/server/@LeslieLeung/mcp-server-memos)

A [MCP(Model Context Protocol)](https://modelcontextprotocol.io) server for [Memos](https://github.com/usememos/memos).

## Tools

- `search_memos`: Search memos with keyword.
- `create_memo`: Create a new memo.

## Usage

### Installing via Smithery

To install mcp-server-memos for Claude Desktop automatically via [Smithery](https://smithery.ai/server/@LeslieLeung/mcp-server-memos):

```bash
npx -y @smithery/cli install @LeslieLeung/mcp-server-memos --client claude
```

```
{
    "mcpServers": [
        "memos": {
            "command": "uvx",
            "args": [
                "memos-mcp-server"
            ],
            "env": {
                "MEMOS_URL": "https://memos.example.com",
                "MEMOS_API_KEY": "your_api_key",
                "DEFAULT_TAG": "#mcp"
            }
        }
    ]
}
```
