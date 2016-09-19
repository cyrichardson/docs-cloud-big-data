.. _delete-delete-a-cluster-v2:

Delete a cluster
~~~~~~~~~~~~~~~~

.. code::

    DELETE /v2/{tenant_id}/clusters/{clusterId}

This operation deletes the specified cluster.

The ``HTTP 400`` error code might indicate missing or invalid parameters.

The ``HTTP 409`` error code might indicate an invalid state.


This table shows the possible response codes for this operation:

+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |No Content               |The server has fulfilled |
|                          |                         |the request and does not |
|                          |                         |need to return a request |
|                          |                         |body.                    |
+--------------------------+-------------------------+-------------------------+
|400                       |Bad Request              |The user-provided        |
|                          |                         |request contained an     |
|                          |                         |error.                   |
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
|{clusterId}               |String                   |The cluster ID.          |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.

Response
--------

This operation does not return a response body.




