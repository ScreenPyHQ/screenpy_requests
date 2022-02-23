"""
Questions an Actor might ask about API requests they've made.
"""

from .body_of_the_last_response import BodyOfTheLastResponse
from .cookies import Cookies
from .headers_of_the_last_response import HeadersOfTheLastResponse
from .status_code_of_the_last_response import StatusCodeOfTheLastResponse

# Natural-language-enabling syntactic sugar
TheBodyOfTheLastResponse = BodyOfTheLastResponse
TheCookies = Cookies
TheHeadersOfTheLastResponse = HeadersOfTheLastResponse
TheStatusCodeOfTheLastResponse = StatusCodeOfTheLastResponse


__all__ = [
    "BodyOfTheLastResponse",
    "Cookies",
    "HeadersOfTheLastResponse",
    "StatusCodeOfTheLastResponse",
    "TheBodyOfTheLastResponse",
    "TheCookies",
    "TheHeadersOfTheLastResponse",
    "TheStatusCodeOfTheLastResponse",
]
