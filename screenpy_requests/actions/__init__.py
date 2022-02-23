"""
Actions an Actor can perform using their Ability to MakeAPIRequests.
"""

from typing import Protocol, Type

from .add_header import AddHeader
from .send_api_request import SendAPIRequest
from .set_headers import SetHeaders


class APIMethodAction(Protocol):
    """Describes the available methods for a SendMETHODRequest Action."""

    @staticmethod
    def to(url: str) -> SendAPIRequest:
        """Set the URL this request will be sent to."""
        ...


def generate_send_method_class(method: str) -> Type[APIMethodAction]:
    """
    Generates a class for a specific HTTP method call.
    """

    class SendMETHODRequest:
        "Will be programmatically replaced."

        @staticmethod
        def to(url: str) -> SendAPIRequest:
            "Will be programmatically replaced."
            return SendAPIRequest(method, url)

    SendMETHODRequest.__doc__ = f"""Send a {method} request to a URL.

Abilities Required:
    |MakeAPIRequests|

Examples::

    the_actor.attempts_to(Send{method}Request.to("https://www.example.com")))

    the_actor.attempts_to(
        Send{method}Request.to("https://www.example.com").with_(auth=(USER, PASS)
    )
"""
    SendMETHODRequest.to.__doc__ = f"""Set the URL to send the {method} request to."""

    return SendMETHODRequest


#: Send a DELETE request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendDELETERequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendDELETERequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendDELETERequest = generate_send_method_class("DELETE")

#: Send a GET request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendGETRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendGETRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendGETRequest = generate_send_method_class("GET")

#: Send a HEAD request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendHEADRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendHEADRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendHEADRequest = generate_send_method_class("HEAD")

#: Send an OPTIONS request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendOPTIONSRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendOPTIONSRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendOPTIONSRequest = generate_send_method_class("OPTIONS")

#: Send a PATCH request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendPATCHRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendPATCHRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendPATCHRequest = generate_send_method_class("PATCH")

#: Send a POST request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendPOSTRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendPOSTRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendPOSTRequest = generate_send_method_class("POST")

#: Send a PUT request to a URL.
#:
#: Abilities Required:
#:     |MakeAPIRequests|
#:
#: Examples::
#:
#:     the_actor.attempts_to(SendPUTRequest.to("https://www.example.com")))
#:
#:     the_actor.attempts_to(
#:         SendPUTRequest.to("https://www.example.com").with_(auth=(USER, PASS))
#:     )
SendPUTRequest = generate_send_method_class("PUT")


# Natural-language-enabling syntactic sugar
AddHeaders = AddHeader


__all__ = [
    "AddHeader",
    "AddHeaders",
    "SendDELETERequest",
    "SendGETRequest",
    "SendHEADRequest",
    "SendOPTIONSRequest",
    "SendPATCHRequest",
    "SendPOSTRequest",
    "SendPUTRequest",
    "SetHeaders",
]
