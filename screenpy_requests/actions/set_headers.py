"""Set the headers on the Actor's API session."""

from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, cast

from screenpy import aside, beat
from screenpy.narration import AIRY

from ..abilities import MakeAPIRequests

if TYPE_CHECKING:
    from screenpy import Actor


class SetHeaders:
    """Set the headers of the Actor's API session to this specific set.

    Note this will remove all other headers on your session.

    Abilities Required:
        :class:`~screenpy_requests.abilities.MakeAPIRequests`

    Examples::

        the_actor.attempts_to(SetHeaders(Cookies="csrf_token=1234"))

        the_actor.attempst_to(SetHeaders.to(Cookies="csrf_token=1234"))

        the_actor.attempts_to(
            SetHeaders(Cookies="csrf_token=1234").which_should_be_kept_secret()
        )

        the_actor.attempts_to(SetHeaders({"Cookies": "csrf_token=1234"}))

        the_actor.attempts_to(SetHeaders("Cookies", "csrf_token=1234"))

        the_actor.attempts_to(
            SetHeaders(
                (
                    ("Cookies", "csrf_token=1234"),
                    ("ContentType", "application/JSON"),
                )
            )
        )
    """

    headers: dict

    @staticmethod
    def to(**kwargs: str) -> SetHeaders:
        """Specify the headers to set."""
        return SetHeaders(**kwargs)

    def which_should_be_kept_secret(self) -> SetHeaders:
        """Indicate these headers should not be written to the log."""
        self.secret = True
        self.headers_to_log = "some"
        return self

    secretly = which_should_be_kept_secret

    def describe(self) -> str:
        """Describe the Action in present tense."""
        return f"Set the{self.headers_to_log} headers of a session."

    @beat("{} sets {headers_to_log} headers of their session.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to set the headers for their API session."""
        if not self.secret:
            aside(f"... the headers are:\n{self.headers}", gravitas=AIRY)
        session = the_actor.ability_to(MakeAPIRequests).session
        session.headers.clear()
        session.headers.update(self.headers)

    def __init__(self, *header_pairs: str | Iterable, **header_kwargs: str) -> None:
        self.headers = {}
        if len(header_pairs) == 1:
            self.headers = dict(cast(Iterable, header_pairs[0]))
        elif header_pairs and len(header_pairs) % 2 == 0:
            self.headers = dict(zip(header_pairs[0::2], header_pairs[1::2]))
        elif header_pairs:
            msg = "SetHeader received an odd-number of key-value pairs."
            raise ValueError(msg)

        if header_kwargs:
            self.headers.update(header_kwargs)

        self.secret = False
        self.headers_to_log = ", ".join(self.headers)
