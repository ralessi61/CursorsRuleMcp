import asyncio
from unittest.mock import patch

import pytest

from src.utils import divide, fetch_user


def test_divide() -> None:
    assert divide(10, 4) == 2.5


def test_divide_by_zero() -> None:
    with pytest.raises(ValueError):
        divide(1, 0)


def test_fetch_user_mocked() -> None:
    # No network: replace the blocking call with a fake
    with patch("src.utils._get_user_sync", return_value={"id": 1, "name": "Ada"}):
        assert asyncio.run(fetch_user(1)) == {"id": 1, "name": "Ada"}
