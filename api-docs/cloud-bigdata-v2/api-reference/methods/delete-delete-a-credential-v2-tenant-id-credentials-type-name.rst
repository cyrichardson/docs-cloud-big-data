.. _delete-a-credential-v2:

Delete a credential
~~~~~~~~~~~~~~~~~~~

.. code::

    DELETE /v2/{tenant_id}/credentials/{type}/{name}

This operation deletes the specified credential.

You can delete only credentials that are not used by any active clusters.

The ``HTTP 409`` error code might indicate an invalid state.

This table shows the possible response codes for this operation:

+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |No Content               |The server has fulfilled |
|                          |                         |the request and does not |
|                          |                         |need to return a         |
|                          |                         |response body.           |
+--------------------------+-------------------------+-------------------------+
|404                       |Not Found                |The back-end services    |
|                          |                         |did not find anything    |
|                          |                         |matching the request URI.|
+--------------------------+-------------------------+-------------------------+
|409                       |Conflict                 |The requested resource   |
|                          |                         |cannot currently be      |
|                          |                         |operated on.             |
+--------------------------+-------------------------+-------------------------+


Request
-------

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{type}                    |String                   |Specify type of          |
|                          |                         |credential. Supported    |
|                          |                         |options are ``ssh_keys`` |
|                          |                         |and ``cloud_files``. The |
|                          |                         |GET calls also support   |
|                          |                         |``types`` and            |
|                          |                         |``connectors``.          |
+--------------------------+-------------------------+-------------------------+
|{name}                    |String                   |Name or identifier for a |
|                          |                         |credential.              |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.


Response
--------

This operation does not return a response body.




