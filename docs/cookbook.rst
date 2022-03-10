=========================
ScreenPy Requests Recipes
=========================

Setting An Authorization Header
===============================

During your API tests,
you will likely need
to log in.
You can set your authorization header
like so::

    from screenpy import AnActor
    from screenpy_requests.abilities import MakeAPIRequests
    from screenpy_requests.actions import AddHeader, SendPOSTRequest
    from screenpy_requests.questions import BodyOfTheLastResponse

    # from example test data files
    from .secrets import USERNAME, PASSWORD
    from .urls import LOGIN_URL


    Apu = AnActor.who_can(MakeAPIRequests())
    Apu.attempts_to(
        SendPOSTRequest.to(LOGIN_URL).with_(auth=(USERNAME, PASSWORD)),
    )

    bearer_token = BodyOfTheLastResponse.answered_by(Apu)["token"]

    Apu.attempts_to(AddHeader(Authorization=f"Bearer {bearer_token}"))
