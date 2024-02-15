"""Questions an Actor might ask about API requests they've made."""

from .body_of_the_last_response import BodyOfTheLastResponse
from .cookies import Cookies
from .headers_of_the_last_response import HeadersOfTheLastResponse
from .status_code_of_the_last_response import StatusCodeOfTheLastResponse

# Natural-language-enabling syntactic sugar
TheBody = Body = TheBodyOfTheLastResponse = BodyOfTheLastResponse
TheCookies = Cookies
TheHeaders = Headers = TheHeadersOfTheLastResponse = HeadersOfTheLastResponse
TheStatusCodeOfTheLastResponse = StatusCodeOfTheLastResponse
TheStatusCode = StatusCode = StatusCodeOfTheLastResponse

__all__ = [
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
]
