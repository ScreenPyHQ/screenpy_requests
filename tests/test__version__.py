from __future__ import annotations

from datetime import datetime

from screenpy_requests import __version__


def test_metadata() -> None:
    assert __version__.__title__ == "screenpy_requests"
    assert __version__.__license__ == "MIT"
    assert __version__.__author__ == "Perry Goy"


def test_copyright_year() -> None:
    current = datetime.now().year
    assert f"{current}" in __version__.__copyright__