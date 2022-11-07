==================
Additional Actions
==================

These are the additional Actions added by ScreenPy Requests.

.. module:: screenpy_requests.actions

AddHeader
---------

**Aliases**: AddHeaders

.. autoclass:: AddHeader
    :members:

SendAPIRequest
--------------

This Action is a bit special.
For code DRYness' sake,
all of the ``Send{METHOD}Request`` Actions
use this Action;
but for readability's sake,
you will want to use
the appropriate ``Send{METHOD}Request`` Action
listed below.

.. autoclass:: SendAPIRequest
    :members:

SendDELETERequest
^^^^^^^^^^^^^^^^^

**Aliases**: Delete

.. autoclass:: SendDELETERequest
    :members:

SendGETRequest
^^^^^^^^^^^^^^

**Aliases**: Get

.. autoclass:: SendGETRequest
    :members:

SendHEADRequest
^^^^^^^^^^^^^^^

**Aliases**: Head

.. autoclass:: SendHEADRequest
    :members:

SendOPTIONSRequest
^^^^^^^^^^^^^^^^^^

**Aliases**: Options

.. autoclass:: SendOPTIONSRequest
    :members:

SendPATCHRequest
^^^^^^^^^^^^^^^^

**Aliases**: Patch

.. autoclass:: SendPATCHRequest
    :members:

SendPOSTRequest
^^^^^^^^^^^^^^^

**Aliases**: Post

.. autoclass:: SendPOSTRequest
    :members:

SendPUTRequest
^^^^^^^^^^^^^^

**Aliases**: Put

.. autoclass:: SendPUTRequest
    :members:

SetHeaders
----------

.. autoclass:: SetHeaders
    :members:

