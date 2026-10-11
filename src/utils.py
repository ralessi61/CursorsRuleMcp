"""Small utility functions used to demo Cursor Rules."""
import asyncio
import json
import urllib.error
import urllib.request
from typing import TypedDict


class User(TypedDict):
    id: int
    name: str


def divide(a: float, b: float) -> float:
    """Divide a by b; raise ValueError when b is zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def _get_user_sync(user_id: int) -> User:
    """Blocking HTTP call (stdlib only)."""
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        with urllib.request.urlopen(url, timeout=10) as res:
            data = json.load(res)
    except urllib.error.HTTPError as exc:
        raise LookupError(f"User {user_id} not found") from exc
    return {"id": data["id"], "name": data["name"]}


async def fetch_user(user_id: int) -> User:
    """Fetch a user without blocking the event loop."""
    return await asyncio.to_thread(_get_user_sync, user_id)
