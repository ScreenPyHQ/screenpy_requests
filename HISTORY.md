Release History
===============

4.0.2 (2023-01-25)
------------------

### Improvements

- All `Send*Request` Actions can now be referred to as their HTTP Action, e.g. `SendGETRequest` can now just be `Get`.
- All Questions can now be referred without `-OfTheLastResponse`, e.g. `BodyOfTheLastResponse` can now just be `Body`.
- All parts of ScreenPy Requests can now be imported from the root (i.e. from screenpy_requests import MakeAPIRequests, SendGETRequest, ...)


4.0.1 (2022-02-22)
------------------

In honor of 2sday, how about 2 deploys?

### Bugfixes

- Fix some issues with dependencies (hopefully), so installing via `screenpy[requests]` works.


4.0.0 (2022-02-22)
------------------

2day is 2sday, by the way. Also I pushed this up at 22:22!

### Timeline

- Broke off from ScreenPy's core library, https://github.com/ScreenPyHQ/screenpy!
