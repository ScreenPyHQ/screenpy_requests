"""
Exceptions used by screenpy_requests, which extend ScreenPy.
"""

from screenpy.exceptions import AbilityError


class RequestError(AbilityError):
    """MakeAPIRequests encountered an error."""
