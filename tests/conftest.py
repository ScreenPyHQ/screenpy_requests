from __future__ import annotations

from unittest import mock

import pytest
from screenpy import AnActor

from screenpy_requests.abilities import MakeAPIRequests


@pytest.fixture(scope="function")
def APITester() -> AnActor:
    """Provide an Actor with mocked API testing abilities."""
    MakeAPIRequests_Mocked = mock.Mock(spec=MakeAPIRequests)
    MakeAPIRequests_Mocked.session = mock.Mock()

    return AnActor.named("APITester").who_can(MakeAPIRequests_Mocked)
