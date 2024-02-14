"""Investigate the body of the last API response received by the Actor."""

from __future__ import annotations

from json.decoder import JSONDecodeError
from typing import TYPE_CHECKING, Union

from screenpy.exceptions import UnableToAnswer
from screenpy.pacing import beat

from ..abilities import MakeAPIRequests

if TYPE_CHECKING:
    from screenpy import Actor

    subscripts = Union[str, int, slice]


class BodyOfTheLastResponse:
    """Ask about the body of the last API response received by the Actor.

    If you are expecting a JSON response, this Question can be indexed to
    return only a section of that response. See the examples below.

    If you are expecting a text response, you can also slice the text.

    Abilities Required:
        :class:`~screenpy_requests.abilities.MakeAPIRequests`

    Examples::

        # JSON response
        the_actor.should(
            See.the(BodyOfTheLastResponse(), ContainsTheEntry(play="Hamlet"))
        )

        # JSON response, picked
        the_actor.should(
            See.the(
                BodyOfTheLastResponse()["users"][0]["first_name"],
                ReadsExactly("Monty")
            ),
        )

        # text response
        the_actor.should(
            See.the(BodyOfTheLastResponse(), ReadsExactly("To be, or not to be"))
        )

        # text response, sliced
        the_actor.should(
            See.the(BodyOfTheLastResponse()[6:12], ReadsExactly("Python"))
        )
    """

    body_parts: list[subscripts]

    def __getitem__(self, key: subscripts) -> BodyOfTheLastResponse:
        """Allows access to subscripts later in answered_by."""
        self.body_parts.append(key)
        return self

    def __init__(self) -> None:
        self.body_parts = []

    def describe(self) -> str:
        """Describe the Question.."""
        return "The body of the last response."

    @beat("{} examines the body of the last response they received.")
    def answered_by(self, the_actor: Actor) -> dict | str:
        """Direct the Actor to investigate the body of the last response."""
        responses = the_actor.ability_to(MakeAPIRequests).responses
        if len(responses) < 1:
            msg = f"{the_actor} has not yet received any API responses."
            raise UnableToAnswer(msg)
        try:
            response = responses[-1].json()
            for part in self.body_parts:
                response = response[part]
        except JSONDecodeError:
            response = responses[-1].text
            for part in self.body_parts:
                response = response[part]
        return response
