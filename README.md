ScreenPy Requests
=================

[![Build Status](../../actions/workflows/tests.yml/badge.svg)](../../actions/workflows/tests.yml)
[![Build Status](../../actions/workflows/lint.yml/badge.svg)](../../actions/workflows/lint.yml)

[![Supported Versions](https://img.shields.io/pypi/pyversions/screenpy_requests.svg)](https://pypi.org/project/screenpy_requests)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

```
TITLE CARD:
                               "ScreenPy Requests"
TITLE DISAPPEARS.
                                                                      FADE IN:
INT. DOCUMENTATION - MIDDAY

AUDIENCE enters from a hidden door built into a bookcase, blinking their eyes
as they adjust to the relative darkness. Dimly lit shelves hold gizmos and
gadgets which give off a secretive air. NARRATOR continues.

                              NARRATOR (V.O.)
            ... these gathered curios enable your ScreenPy
            Actors to make API requests using the Requests
            library.

                              AUDIENCE
            These things look like they weren't meant to be seen.
            Will it be OK to expose them like this?

                              NARRATOR (V.O.)
            You could consider the "front end" to be an End User,
            of sorts. Then your Actors are simply a stand-in for
            your front end application.

                              AUDIENCE
            In that case, anything could be an End User, if I
            need them to be.

                              NARRATOR (V.O.)
            Now you're getting it. Come this way, there are more...

                                                                      FADE OUT
```


Installation
------------
    pip install screenpy_requests

or

    pip install screenpy[requests]


Documentation
-------------
Please check out the [Read The Docs documentation](https://screenpy-requests-docs.readthedocs.io/en/latest/) for the latest information about this module!

You can also read the [ScreenPy Docs](https://screenpy-docs.readthedocs.io/en/latest/) for more information about ScreenPy in general.


Contributing
------------
You want to contribute? Great! Here are the things you should do before submitting your PR:

1. Fork the repo and git clone your fork.
1. `dev` install the project package:
    1. `pip install -e .[dev]`
    1. Optional (poetry users):
        1. `poetry install --extras dev`
1. Run `pre-commit install` once.
1. Run `tox` to perform tests frequently.
1. Create pull-request from your branch.

That's it! :)
