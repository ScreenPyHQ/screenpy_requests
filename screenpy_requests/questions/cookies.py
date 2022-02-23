"""
Investigate the cookies on the Actor's web or API session.
"""

from screenpy import Actor
from screenpy.pacing import beat

from ..abilities import MakeAPIRequests


class Cookies:
    """Ask about the cookies on the Actor's API session.

    Abilities Required:
        |MakeAPIRequests|

    Examples::

        the_actor.should(
            See.the(CookiesOnTheAPISession(), ContainTheEntry(type="snickerdoodle"))
        )
    """

    def describe(self) -> str:
        """Describe the Question.."""
        return "The session's cookies."

    @beat("{} inspects their API session's cookies.")
    def answered_by(self, the_actor: Actor) -> dict:
        """Direct the Actor to investigate their API session's cookies."""
        cookies = the_actor.uses_ability_to(MakeAPIRequests).session.cookies
        return cookies.get_dict()
