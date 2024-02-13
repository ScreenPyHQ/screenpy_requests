"""Investigate the headers of the last API response received."""

from typing import MutableMapping

from screenpy import Actor
from screenpy.exceptions import UnableToAnswer
from screenpy.pacing import beat

from ..abilities import MakeAPIRequests


class HeadersOfTheLastResponse:
    """Ask about the headers of the last API response received.

    Abilities Required:
        :class:`~screenpy_requests.abilities.MakeAPIRequests`

    Examples::

        the_actor.should(
            See.the(HeadersOfTheLastResponse(), ContainsKey("Content-Type"))
        )
    """

    def describe(self) -> str:
        """Describe the Question.."""
        return "The headers of the last response."

    @beat("{} examines the headers of the last response they received.")
    def answered_by(self, the_actor: Actor) -> MutableMapping[str, str]:
        """Direct the Actor to investigate the headers of the last response."""
        responses = the_actor.ability_to(MakeAPIRequests).responses
        if len(responses) < 1:
            msg = f"{the_actor} has not yet received any API responses."
            raise UnableToAnswer(msg)
        return responses[-1].headers
