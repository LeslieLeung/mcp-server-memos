# mcp-server-memos

A [MCP(Model Context Protocol)](https://modelcontextprotocol.io) server for [Memos](https://github.com/usememos/memos).

## Tools

- `search_memos`: Search memos with keyword.
- `create_memo`: Create a new memo.

## Usage

```
{
    "mcpServers": [
        "memos": {
            "command": "uvx",
            "args": [
                "mcp-server-memos"
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