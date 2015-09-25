
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _delete-delete-cluster-v1.0-tenant-id-clusters-clusterid:

Delete cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    DELETE /v1.0/{tenant_id}/clusters/{clusterId}

This operation deletes the cluster that is specified 				by ``clusterId``.

The 400 error code might indicate missing or invalid 				parameters.

The 409 error code might indicate an invalid 				state.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |No Content               |The server has fulfilled |
|                          |                         |the request and does not |
|                          |                         |need to return a         |
|                          |                         |response body.           |
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
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{clusterId}               |String                   |Specifies the cluster ID.|
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




**Example Delete cluster: JSON request**


.. code::

   DELETE https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41
   Accept: application/json 
   X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
   Content-Type: application/json





Response
""""""""""""""""










**Example Delete cluster: JSON response**


.. code::

   Status: 202 Accepted
   Date: Mon, 06 Aug 2012 21:54:21 GMT
   Content-Type: application/json


.. code::

   {
      "cluster":{
         "id":"db478fc1-2d86-4597-8010-cbe787bbbc41",
         "created":"2012-12-27T10:10:10Z",
         "updated":"2012-12-27T20:14:10Z",
         "name":"slice",
         "clusterType":"HADOOP_HDP2_1",
         "flavorId":"hadoop1-7",
         "nodeCount":5,
         "postInitScriptStatus":null,
         "status":"DELETING",
         "links":[
            {
               "rel":"self",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41"
            },
            {
               "rel":"bookmark",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41"
            }
         ]
      }
   }      




