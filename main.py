from typing import Any, List, Dict
import os
from mcp.server.fastmcp import FastMCP
from mcp.shared.exceptions import McpError
from mcp.types import (
    ErrorData,
    INTERNAL_ERROR,
)
from memos import Memos, MemosException

# Initialize FastMCP server
mcp = FastMCP("memos")

# Constants
MEMOS_URL = os.getenv("MEMOS_URL")
MEMOS_API_KEY = os.getenv("MEMOS_API_KEY")
DEFAULT_TAG = os.getenv("DEFAULT_TAG", "#MCP")  # Default to #MCP if not set

# Initialize Memos client
memos_client = Memos(MEMOS_URL, MEMOS_API_KEY)


@mcp.tool()
def search_memos(query: str) -> List[Dict[str, Any]]:
    """
    Search memos using the Memos API.

    Args:
        query: Search query string

    Returns:
        A list of memo objects matching the query
    """
    try:
        return memos_client.search_memos(query)
    except MemosException as e:
        # Map the Memos exception to an MCP error
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=str(e)))


@mcp.tool()
def create_memo(content: str, tags: List[str] = []) -> Dict[str, Any]:
    """
    Create a new memo with the Memos API.

    Args:
        content: Content of the memo
        tags: List of tags for the memo (will always include the default tag)

    Returns:
        The created memo object
    """
    # Make sure default tag is included
    tags_with_default = list(tags)
    if DEFAULT_TAG not in tags_with_default:
        tags_with_default.append(DEFAULT_TAG)

    try:
        return memos_client.create_memo(content, tags_with_default)
    except MemosException as e:
        # Map the Memos exception to an MCP error
        raise McpError(ErrorData(code=INTERNAL_ERROR, message=str(e)))


def main():
    # Initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
