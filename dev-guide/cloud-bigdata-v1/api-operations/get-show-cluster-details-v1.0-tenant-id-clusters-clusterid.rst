
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-show-cluster-details-v1.0-tenant-id-clusters-clusterid:

Show cluster details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/clusters/{clusterId}

This oepration shows details for a specified 				cluster.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|404                       |Not Found                |The back-end services    |
|                          |                         |did not find anything    |
|                          |                         |matching the request URI.|
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




**Example Show cluster details: JSON request**


.. code::

   GET https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/ac111111-2d86-4597-8010-cbe787bbbc41
   Accept: application/json 
   X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
   Content-Type: application/json  





Response
""""""""""""""""










**Example Show cluster details: JSON response**


.. code::

   Status: 200 OK
   Date: Mon, 06 Aug 2012 21:54:21 GMT
   Content-Type: application/json
   Content-Length: 110


.. code::

   {
      "cluster":{
         "id":"db478fc1-2d86-4597-8010-cbe787bbbc41",
         "created":"2012-12-27T10:10:10Z",
         "updated":"2012-12-27T10:20:10Z",
         "name":"slice",
         "clusterType":"HADOOP_HDP2_1",
         "flavorId":"hadoop1-7",
         "nodeCount":5,
         "postInitScriptStatus":"SUCCEEDED",
         "progress":1.0,
         "status":"ACTIVE",
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




