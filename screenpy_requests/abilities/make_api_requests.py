"""Enable the Actor to make API requests and store the responses."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable

from requests import Session

from ..exceptions import RequestError

if TYPE_CHECKING:
    from requests import Response


class MakeAPIRequests:
    """Use Requests to enable sending API requests.

    Examples::

        Perry = AnActor.named("Perry").who_can(MakeAPIRequests())

        Perry = AnActor.named("Perry").who_can(
            MakeAPIRequests.using(session_instance)
        )
    """

    @staticmethod
    def using(session: Session) -> MakeAPIRequests:
        """Provide a |Requests| session for the Ability to use."""
        return MakeAPIRequests(session=session)

    def to_send(self, method: str, url: str, **kwargs: Any) -> None:  # noqa: ANN401
        """Send a request.

        This is a pass-through to the session's ``request`` method and has the
        same parameter signature. The response is stored in this Ability.

        Args:
            method: the HTTP method of the request - GET, POST, etc.
            url: the URL to which to send the request.
            kwargs: additional keyword arguments to pass through to |request|.
        """
        http_requests: dict[str, Callable] = {
            "DELETE": self.session.delete,
            "GET": self.session.get,
            "HEAD": self.session.head,
            "OPTIONS": self.session.options,
            "PATCH": self.session.patch,
            "POST": self.session.post,
            "PUT": self.session.put,
        }
        method = method.upper()

        if method not in http_requests:
            msg = f'"{method}" is not a valid HTTP method.'
            raise RequestError(msg)

        self.responses.append(http_requests[method](url, **kwargs))

    send = to_send

    def forget(self) -> None:
        """Clean up the Session instance stored in this Ability."""
        self.session.close()

    def __repr__(self) -> str:
        """Represents Making API Requests."""
        return "Make API Requests"

    __str__ = __repr__

    def __init__(self, session: Session | None = None) -> None:
        if session is None:
            session = Session()
        self.session = session
        self.responses: list[Response] = []
