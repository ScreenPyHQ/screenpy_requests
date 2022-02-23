from unittest import mock

import pytest

from screenpy_requests.abilities import MakeAPIRequests
from screenpy_requests.exceptions import RequestError


class TestMakeAPIRequests:
    def test_can_be_instantiated(self):
        mar1 = MakeAPIRequests()
        mar2 = MakeAPIRequests.using(None)

        assert isinstance(mar1, MakeAPIRequests)
        assert isinstance(mar2, MakeAPIRequests)

    def test_unexpected_http_method(self):
        mar = MakeAPIRequests()

        with pytest.raises(RequestError):
            mar.send("TEST_METHOD", "url")

    @pytest.mark.parametrize(
        "method", ["delete", "get", "head", "options", "patch", "post", "put"]
    )
    def test_http_method_calls_correct_session_method(self, method):
        mocked_session = mock.Mock()
        mar = MakeAPIRequests.using(mocked_session)

        mar.send(method, "url")

        getattr(mocked_session, method).assert_called_once()
