"""Add headers to an Actor's API session."""

from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, cast

from screenpy import aside, beat
from screenpy.narration import AIRY

from ..abilities import MakeAPIRequests

if TYPE_CHECKING:
    from screenpy import Actor


class AddHeader:
    """Add one or more headers to the Actor's API session.

    Abilities Required:
        :class:`~screenpy_requests.abilities.MakeAPIRequests`

    Examples::

        the_actor.attempts_to(AddHeader(Authorization=TOKEN_AUTH_STRING))

        the_actor.attempts_to(
            AddHeader(Authorization=TOKEN_AUTH_STRING).which_should_be_kept_secret()
        )

        the_actor.attempts_to(AddHeader({"Authorization": TOKEN_AUTH_STRING}))

        the_actor.attempts_to(AddHeader("Authorization", TOKEN_AUTH_STRING))

        the_actor.attempts_to(
            AddHeaders(
                (
                    ("Authorization", TOKEN_AUTH_STRING),
                    ("ContentType", "application/JSON"),
                )
            )
        )
    """

    def which_should_be_kept_secret(self) -> AddHeader:
        """Indicate the added headers should not be written to the log."""
        self.secret = True
        self.headers_to_log = "some"
        return self

    secretly = which_should_be_kept_secret

    def describe(self) -> str:
        """Describe the Action in present tense."""
        return f"Add {self.headers_to_log} headers."

    @beat("{} adds {headers_to_log} headers to their session.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to add the given headers to their session."""
        if not self.secret:
            aside(f"... the headers are: {self.headers}", gravitas=AIRY)
        session = the_actor.ability_to(MakeAPIRequests).session
        session.headers.update(self.headers)

    def __init__(self, *header_pairs: str | Iterable, **header_kwargs: str) -> None:
        self.headers = {}
        if len(header_pairs) == 1:
            self.headers = dict(cast(Iterable, header_pairs[0]))
        elif header_pairs and len(header_pairs) % 2 == 0:
            self.headers = dict(zip(header_pairs[0::2], header_pairs[1::2]))
        elif header_pairs:
            msg = "AddHeader received an odd-number of key-value pairs."
            raise ValueError(msg)

        if header_kwargs:
            self.headers.update(header_kwargs)

        self.secret = False
        self.headers_to_log = ", ".join(self.headers)
