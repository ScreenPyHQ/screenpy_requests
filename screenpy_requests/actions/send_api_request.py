"""Send an API request."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from screenpy import aside, beat
from screenpy.narration import AIRY

from ..abilities import MakeAPIRequests

if TYPE_CHECKING:
    from screenpy import Actor


class SendAPIRequest:
    """Send an API request.

    You can use this Action class directly if you wish, but the
    Send{METHOD}Request Actions are easier to read.

    Abilities Required:
        :class:`~screenpy_requests.abilities.MakeAPIRequests`

    Examples::

        the_actor.attempts_to(SendAPIRequest("GET", "http://www.example.com"))

        the_actor.attempts_to(
            SendAPIRequest("POST", "http://www.example.com").with_(
                data={"screenplay": "Citizen Kane"}
            )
        )
    """

    def with_(self, **kwargs: Any) -> SendAPIRequest:  # noqa: ANN401
        """Set additional kwargs to send through to the session's request.

        Args:
            kwargs: keyword arguments that correspond to |request|'s API.
        """
        self.kwargs = kwargs
        return self

    def which_should_be_kept_secret(self) -> SendAPIRequest:
        """Indicate the extra data should not be written to the log."""
        self.secret = True
        return self

    secretly = which_should_be_kept_secret

    def describe(self) -> str:
        """Describe the Action in present tense."""
        return f"Send a {self.method} request to {self.url}"

    @beat("{} sends a {method} request to {url}")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to send an API request to the stored URL."""
        if self.kwargs and not self.secret:
            aside(f"... along with the following: {self.kwargs}", gravitas=AIRY)

        the_actor.uses_ability_to(MakeAPIRequests).to_send(
            self.method, self.url, **self.kwargs
        )

    def __init__(self, method: str, url: str) -> None:
        self.method = method.upper()
        self.url = url
        self.kwargs = {}
        self.secret = False
