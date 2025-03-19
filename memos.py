import requests
from typing import List, Dict, Any


class MemosException(Exception):
    """Custom exception for Memos API errors"""

    pass


class Memos:
    def __init__(self, memos_url, memos_api_key):
        """
        Initialize a Memos client.

        Args:
            memos_url: The URL of the Memos API
            memos_api_key: API key for authentication
        """
        self.memos_url = memos_url
        self.memos_api_key = memos_api_key
        self.headers = {
            "Authorization": f"Bearer {self.memos_api_key}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

    def get_user_id(self) -> str:
        """
        Get the user ID of the authenticated user by checking auth status.

        Returns:
            str: The user ID of the authenticated user

        Raises:
            MemosException: If there is an error retrieving the user ID
        """
        try:
            # Use the auth/status endpoint to get current user info
            response = requests.post(
                f"{self.memos_url}/api/v1/auth/status", headers=self.headers
            )
            response.raise_for_status()

            # Extract the user ID from the response
            user_data = response.json()
            user_id = user_data.get("name")

            if not user_id:
                raise MemosException("Could not retrieve user ID from auth status")

            return user_id
        except requests.RequestException as e:
            raise MemosException(f"Error getting user ID: {e}")

    def search_memos(self, query: str) -> List[Dict[str, Any]]:
        """
        Search memos using the Memos API.

        Args:
            query: Search query string

        Returns:
            A list of memo objects matching the query

        Raises:
            MemosException: If there is an error searching memos
        """
        # Get the user ID first
        user_id = self.get_user_id()

        params = {
            "filter": f'content.contains("{query}")',  # Search by content
            "pageSize": 20,  # Limit results
        }

        try:
            response = requests.get(
                f"{self.memos_url}/api/v1/{user_id}/memos",
                headers=self.headers,
                params=params,
            )
            response.raise_for_status()

            if response.status_code == 200:
                return response.json().get("memos", [])
            else:
                raise MemosException(f"Error searching memos: {response.status_code}")
        except requests.RequestException as e:
            raise MemosException(f"Error searching memos: {e}")

    def create_memo(self, content: str, tags: List[str] = []) -> Dict[str, Any]:
        """
        Create a new memo using the Memos API.

        Args:
            content: Content of the memo
            tags: List of tags for the memo

        Returns:
            The created memo object

        Raises:
            MemosException: If there is an error creating the memo
        """
        # Format content to include tags
        formatted_content = content
        if tags:
            # Append tags to the end of content
            formatted_content += "\n\n" + " ".join(tags)

        # Prepare payload
        payload = {
            "content": formatted_content,
            "visibility": "PRIVATE",  # Default to private memos
        }

        try:
            response = requests.post(
                f"{self.memos_url}/api/v1/memos", headers=self.headers, json=payload
            )
            response.raise_for_status()

            if response.status_code in [200, 201]:
                return response.json()
            else:
                raise MemosException(f"Error creating memo: {response.status_code}")
        except requests.RequestException as e:
            raise MemosException(f"Error creating memo: {e}")
