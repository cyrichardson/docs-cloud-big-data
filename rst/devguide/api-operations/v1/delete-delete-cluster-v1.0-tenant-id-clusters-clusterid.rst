
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Delete Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    DELETE /v1.0/{tenant_id}/clusters/{clusterId}

Deletes a specified cluster.

The 400 error code might indicate missing or invalid 				parameters.

The 409 error code might indicate an invalid 				state.

This operation deletes the cluster that is specified 				by ``clusterId``.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
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
""""""""""""""""

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{clusterId}               |xsd:string               |Specifies the cluster ID.|
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




**Example Delete Cluster: JSON request**


.. code::

    DELETE https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41
    Accept: application/json 
    X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
    Content-Type: application/json


Response
""""""""""""""""


This operation does not accept a response body.




**Example Delete Cluster: JSON response**


.. code::

    Status: 202 Accepted
    Date: Mon, 06 Aug 2012 21:54:21 GMT
    Content-Type: application/json

