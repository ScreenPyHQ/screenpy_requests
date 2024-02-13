from __future__ import annotations

from json.decoder import JSONDecodeError
from typing import TYPE_CHECKING
from unittest import mock

import pytest
from requests.cookies import RequestsCookieJar
from screenpy.exceptions import UnableToAnswer

from screenpy_requests.abilities import MakeAPIRequests
from screenpy_requests.questions import (
    BodyOfTheLastResponse,
    Cookies,
    HeadersOfTheLastResponse,
    StatusCodeOfTheLastResponse,
)

if TYPE_CHECKING:
    from screenpy import Actor


class TestBodyOfTheLastResponse:
    def test_can_be_instantiated(self) -> None:
        botlr = BodyOfTheLastResponse()

        assert isinstance(botlr, BodyOfTheLastResponse)

    def test_raises_error_if_no_responses(self, APITester: Actor) -> None:
        botlr = BodyOfTheLastResponse()
        APITester.ability_to(MakeAPIRequests).responses = []

        with pytest.raises(UnableToAnswer):
            botlr.answered_by(APITester)

    def test_handles_non_json(self, APITester: Actor) -> None:
        """Non-JSON bodies are returned as text."""
        botlr = BodyOfTheLastResponse()
        test_body = "And stop calling me Shirley."
        mock_response = mock.Mock()
        mock_response.json.side_effect = JSONDecodeError(
            "Surely, it's not JSON", test_body, 1
        )
        mock_response.text = test_body
        APITester.ability_to(MakeAPIRequests).responses = [mock_response]

        answer = botlr.answered_by(APITester)

        assert answer == test_body

    def test_ask_for_body_of_the_last_response(self, APITester: Actor) -> None:
        """BodyOfTheLastResponse and ContainsTheEntry tests the JSON body"""
        test_json = {"play": "Hamlet"}
        fake_response = mock.Mock()
        fake_response.json.return_value = test_json
        mocked_mar = APITester.ability_to(MakeAPIRequests)
        mocked_mar.responses = [fake_response]

        assert BodyOfTheLastResponse().answered_by(APITester) == test_json

    def test_stores_index_path(self):
        botlr = BodyOfTheLastResponse()["shuffled"]["off"][10]["mortal"]["coils"]

        assert botlr.body_parts == ["shuffled", "off", 10, "mortal", "coils"]

    def test_digs_into_json(self, APITester):
        test_json = {"plays": [{"name": "Hamlet"}]}
        fake_response = mock.Mock()
        fake_response.json.return_value = test_json
        mocked_mar = APITester.ability_to(MakeAPIRequests)
        mocked_mar.responses = [fake_response]

        botlr = BodyOfTheLastResponse()["plays"][0]["name"]

        assert botlr.answered_by(APITester) == "Hamlet"

    def test_slices_text(self, APITester):
        test_text = "My favorite play is Hamlet."
        fake_response = mock.Mock()
        fake_response.json.return_value = test_text
        mocked_mar = APITester.ability_to(MakeAPIRequests)
        mocked_mar.responses = [fake_response]

        assert BodyOfTheLastResponse()[-7:-1].answered_by(APITester) == "Hamlet"



class TestCookies:
    def test_can_be_instantiated(self) -> None:
        c = Cookies()

        assert isinstance(c, Cookies)

    def test_ask_for_cookies(self, APITester: Actor) -> None:
        test_name = "cookie_type"
        test_value = "madeleine"
        test_jar = RequestsCookieJar()
        test_jar.set(test_name, test_value)
        APITester.ability_to(MakeAPIRequests).session.cookies = test_jar

        assert Cookies().answered_by(APITester)[test_name] == test_value


class TestHeadersOfTheLastResponse:
    def test_can_be_instantiated(self) -> None:
        hotlr = HeadersOfTheLastResponse()

        assert isinstance(hotlr, HeadersOfTheLastResponse)

    def test_raises_error_if_no_responses(self, APITester: Actor) -> None:
        hotlr = HeadersOfTheLastResponse()
        APITester.ability_to(MakeAPIRequests).responses = []

        with pytest.raises(UnableToAnswer):
            hotlr.answered_by(APITester)

    def test_ask_for_headers_of_the_last_response(self, APITester: Actor) -> None:
        """HeadersOfTheLastResponse returns a dict"""
        test_headers = {"Content-Type": "application/json"}
        mock_response = mock.Mock()
        mock_response.headers = test_headers
        APITester.ability_to(MakeAPIRequests).responses = [mock_response]

        HeadersOfTheLastResponse().answered_by(APITester) == test_headers


class TestStatusCodeOfTheLastResponse:
    def test_can_be_instantiated(self) -> None:
        scotlr = StatusCodeOfTheLastResponse()

        assert isinstance(scotlr, StatusCodeOfTheLastResponse)

    def test_raises_error_if_no_responses(self, APITester: Actor) -> None:
        scotlr = StatusCodeOfTheLastResponse()
        APITester.ability_to(MakeAPIRequests).responses = []

        with pytest.raises(UnableToAnswer):
            scotlr.answered_by(APITester)

    def test_ask_for_status_code_of_the_last_response(self, APITester: Actor) -> None:
        test_status_code = 1337
        mock_response = mock.Mock()
        mock_response.status_code = test_status_code
        APITester.ability_to(MakeAPIRequests).responses = [mock_response]

        StatusCodeOfTheLastResponse().answered_by(APITester) == test_status_code
