.. _request-and-response-types:

==========================
Request and response types
==========================

The |apiservice| supports JSON data serialization formats.

The request format is specified by using the ``Content-Type`` header and is
required for operations that have a request body.

The response format can be specified in requests either by using the
``Accept`` header or by adding ``.json`` extension to the request URI. Note
that JSON is the default format for data serialization.

.. list-table:: **JSON response formats**
   :widths: 10 20 10 10
   :header-rows: 1

   * - Format
     - Accept header
     - Query extension
     - Default
   * - JSON
     - application/json
     - .json
     - Yes
