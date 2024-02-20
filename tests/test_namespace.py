from __future__ import annotations

import screenpy_requests


def test_screenpy_requests() -> None:
    expected = (
        "AddHeader",
        "AddHeaders",
        "Body",
        "BodyOfTheLastResponse",
        "Cookies",
        "Delete",
        "Get",
        "Head",
        "Headers",
        "HeadersOfTheLastResponse",
        "MakeAPIRequests",
        "Options",
        "Patch",
        "Post",
        "Put",
        "SendDELETERequest",
        "SendGETRequest",
        "SendHEADRequest",
        "SendOPTIONSRequest",
        "SendPATCHRequest",
        "SendPOSTRequest",
        "SendPUTRequest",
        "SetHeaders",
        "StatusCode",
        "StatusCodeOfTheLastResponse",
        "TheBody",
        "TheBodyOfTheLastResponse",
        "TheCookies",
        "TheHeaders",
        "TheHeadersOfTheLastResponse",
        "TheStatusCode",
        "TheStatusCodeOfTheLastResponse",
    )

    assert sorted(screenpy_requests.__all__) == sorted(expected)
    return


def test_abilities() -> None:
    expected = ("MakeAPIRequests",)
    assert sorted(screenpy_requests.abilities.__all__) == sorted(expected)


def test_actions() -> None:
    expected = (
        "AddHeader",
        "AddHeaders",
        "Delete",
        "Get",
        "Head",
        "Options",
        "Patch",
        "Post",
        "Put",
        "SendDELETERequest",
        "SendGETRequest",
        "SendHEADRequest",
        "SendOPTIONSRequest",
        "SendPATCHRequest",
        "SendPOSTRequest",
        "SendPUTRequest",
        "SetHeaders",
    )
    assert sorted(screenpy_requests.actions.__all__) == sorted(expected)


def test_questions() -> None:
    expected = (
        "Body",
        "BodyOfTheLastResponse",
        "Cookies",
        "Headers",
        "HeadersOfTheLastResponse",
        "StatusCode",
        "StatusCodeOfTheLastResponse",
        "TheBody",
        "TheBodyOfTheLastResponse",
        "TheCookies",
        "TheHeaders",
        "TheHeadersOfTheLastResponse",
        "TheStatusCode",
        "TheStatusCodeOfTheLastResponse",
    )
    assert sorted(screenpy_requests.questions.__all__) == sorted(expected)
