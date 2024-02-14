from __future__ import annotations

import logging
from typing import TYPE_CHECKING, cast
from unittest import mock

import pytest

from screenpy_requests.abilities import MakeAPIRequests
from screenpy_requests.actions import (
    AddHeader,
    AddHeaders,
    SendAPIRequest,
    SendDELETERequest,
    SendGETRequest,
    SendHEADRequest,
    SendOPTIONSRequest,
    SendPATCHRequest,
    SendPOSTRequest,
    SendPUTRequest,
    SetHeaders,
    generate_send_method_class,
)

if TYPE_CHECKING:
    from screenpy import Actor

    from screenpy_requests.actions import APIMethodAction


class TestAddHeader:
    def test_can_be_instantiated(self) -> None:
        ah1 = AddHeader(a="a")
        ah2 = AddHeaders(a="a")

        assert isinstance(ah1, AddHeader)
        assert isinstance(ah2, AddHeader)

    def test_can_be_secret(self) -> None:
        assert AddHeader(a="a").secretly().secret

    def test_remembers_headers(self) -> None:
        assert AddHeader(a="a").headers == {"a": "a"}

    def test_possible_arguments(self) -> None:
        """can handle dict, pairs, and kwargs"""
        ah1 = AddHeader({"a": "1"})
        ah2 = AddHeader("a", "1")
        ah3 = AddHeader(a="1")
        ah4 = AddHeader({"a": "1"}, b="2")

        assert ah1.headers == {"a": "1"}
        assert ah2.headers == {"a": "1"}
        assert ah3.headers == {"a": "1"}
        assert ah4.headers == {"a": "1", "b": "2"}

    def test_raises_on_odd_arguments(self) -> None:
        test_msg = "AddHeader received an odd-number of key-value pairs."
        with pytest.raises(ValueError, match=test_msg):
            AddHeader("a", "1", "b")

    def test_raises_on_non_iterable_arguments(self) -> None:
        test_msg = "dictionary update sequence element #0 has length 1; 2 is required"
        with pytest.raises(ValueError, match=test_msg):
            AddHeader("a")

    def test_perform_add_header(self, APITester: Actor) -> None:
        test_headers = {"test": "header", "another": "one"}
        session = APITester.ability_to(MakeAPIRequests).session
        session.headers = {}

        AddHeader(**test_headers).perform_as(APITester)

        assert session.headers == test_headers

    def test_logs_headers(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        test_headers = {"foo": "bar", "spam": "eggs"}

        with caplog.at_level(logging.DEBUG):
            AddHeader(**test_headers).perform_as(APITester)

        assert "foo, spam" in caplog.text
        assert str(test_headers) in caplog.text

    def test_hides_secret_headers(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        test_headers = {"foo": "bar", "spam": "eggs"}

        with caplog.at_level(logging.DEBUG):
            AddHeader(**test_headers).secretly().perform_as(APITester)

        assert "some headers" in caplog.text
        assert "foo, spam" not in caplog.text
        assert str(test_headers) not in caplog.text


def test_generate_send_method_class_docstring() -> None:
    """Generated class and method's docstring both contain method name."""
    test_method = "TESTYTEST"

    SendTESTMethod = generate_send_method_class(test_method)

    assert SendTESTMethod.__doc__ is not None
    assert SendTESTMethod.to.__doc__ is not None
    assert test_method in SendTESTMethod.__doc__
    assert test_method in SendTESTMethod.to.__doc__


@pytest.mark.parametrize(
    "request_class",
    [
        SendDELETERequest,
        SendGETRequest,
        SendHEADRequest,
        SendOPTIONSRequest,
        SendPATCHRequest,
        SendPOSTRequest,
        SendPUTRequest,
    ],
)
def test_can_be_instantiated(request_class: type[APIMethodAction]) -> None:
    """Send{METHOD}Request instantiation gives back SendAPIRequest"""
    sr1 = request_class.to("url")
    sr2 = request_class.to("url").with_(some="kwarg")

    assert isinstance(sr1, SendAPIRequest)
    assert isinstance(sr2, SendAPIRequest)


class TestSendAPIRequest:
    def test_can_be_instantiated(self) -> None:
        sar1 = SendAPIRequest("GET", "test")
        sar2 = SendAPIRequest("GET", "test").with_(some="kwarg")

        assert isinstance(sar1, SendAPIRequest)
        assert isinstance(sar2, SendAPIRequest)

    def test_stores_kwargs(self) -> None:
        """kwargs are stored to send in the request later"""
        test_kwargs = {"test": "kwarg"}

        assert SendAPIRequest("GET", "test").with_(**test_kwargs).kwargs == test_kwargs

    def test_can_be_secret(self) -> None:
        assert SendAPIRequest("GET", "test").with_(test="kwarg").secretly().secret

    def test_parameters_passed_along(self, APITester: Actor) -> None:
        """Args and kwargs given to SendAPIRequest are passed to ``to_send``"""
        method = "GET"
        url = "TEST_URL"
        kwargs = {"test": "kwargs"}

        SendAPIRequest(method, url).with_(**kwargs).perform_as(APITester)

        mocked_mar = cast(mock.Mock, APITester.ability_to(MakeAPIRequests))
        mocked_mar.to_send.assert_called_once_with(method, url, **kwargs)

    def test_parameters_logged(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        kwargs = {"test": "kwargs", "data": "foo"}

        with caplog.at_level(logging.DEBUG):
            SendAPIRequest("GET", "TEST_URL").with_(**kwargs).perform_as(APITester)

        assert str(kwargs) in caplog.text

    def test_parameters_not_logged_if_secret(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        kwargs = {"test": "kwargs", "data": "foo"}

        with caplog.at_level(logging.DEBUG):
            SendAPIRequest("GET", "TEST_URL").with_(**kwargs).secretly().perform_as(
                APITester
            )

        assert str(kwargs) not in caplog.text


class TestSetHeaders:
    def test_can_be_instantiated(self) -> None:
        sh1 = SetHeaders(a="a")
        sh2 = SetHeaders.to(b="b")

        assert isinstance(sh1, SetHeaders)
        assert isinstance(sh2, SetHeaders)

    def test_can_be_secret(self) -> None:
        assert SetHeaders(a="1").secretly().secret

    def test_remembers_headers(self) -> None:
        assert SetHeaders(a="a").headers == {"a": "a"}

    def test_possible_arguments(self) -> None:
        """can handle dict, pairs, and kwargs"""
        sh1 = SetHeaders({"a": "1"})
        sh2 = SetHeaders("a", "1")
        sh3 = SetHeaders(a="1")
        sh4 = SetHeaders({"a": "1"}, b="2")

        assert sh1.headers == {"a": "1"}
        assert sh2.headers == {"a": "1"}
        assert sh3.headers == {"a": "1"}
        assert sh4.headers == {"a": "1", "b": "2"}

    def test_raises_on_odd_arguments(self) -> None:
        test_msg = "SetHeader received an odd-number of key-value pairs."
        with pytest.raises(ValueError, match=test_msg):
            SetHeaders("a", "1", "b")

    def test_raises_on_non_iterable_arguments(self) -> None:
        test_msg = "dictionary update sequence element #0 has length 1; 2 is required"
        with pytest.raises(ValueError, match=test_msg):
            SetHeaders("a")

    def test_sets_headers(self, APITester: Actor) -> None:
        test_headers = {"test": "header", "another": "one"}
        session = APITester.ability_to(MakeAPIRequests).session
        session.headers = {"foo": "bar"}

        SetHeaders(**test_headers).perform_as(APITester)

        assert session.headers == test_headers

    def test_logs_headers(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        test_headers = {"foo": "bar", "spam": "eggs"}

        with caplog.at_level(logging.DEBUG):
            SetHeaders(**test_headers).perform_as(APITester)

        assert "foo, spam" in caplog.text
        assert str(test_headers) in caplog.text

    def test_hides_secret_headers(
        self, APITester: Actor, caplog: pytest.LogCaptureFixture
    ) -> None:
        test_headers = {"foo": "bar", "spam": "eggs"}

        with caplog.at_level(logging.DEBUG):
            SetHeaders(**test_headers).secretly().perform_as(APITester)

        assert "some headers" in caplog.text
        assert "foo, spam" not in caplog.text
        assert str(test_headers) not in caplog.text
