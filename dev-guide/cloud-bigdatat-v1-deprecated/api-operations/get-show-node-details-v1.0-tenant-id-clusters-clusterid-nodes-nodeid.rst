
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-show-node-details-v1.0-tenant-id-clusters-clusterid-nodes-nodeid:

Show node details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/clusters/{clusterId}/nodes/{nodeId}

This operation shows details for a specified node 				in a specified cluster.

Valid values for the request body parameter ``postInitScriptStatus`` are ``FAILED``, ``PENDING``, ``DELIVERED``, ``RUNNING``, ``SUCCEEDED``, and ``None``.

Valid values for the node status are in.



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
|{nodeId}                  |String                   |Specifies the node ID.   |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




**Example Show node details: JSON request**


.. code::

   GET https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/ac111111-2d86-4597-8010-cbe787bbbc41/nodes/000
   Accept: application/json 
   X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
   Content-Type: application/json               





Response
""""""""""""""""










**Example Show node details: JSON response**


.. code::

   {
      "node":{
         "id":"000",
         "created":"2012-12-27T10:10:10Z",
         "role":"NAMENODE",
         "name":"NAMENODE-1",
         "postInitScriptStatus":null,
         "status":"ACTIVE",
         "addresses":{
            "public":[
               {
                  "addr":"168.x.x.3",
                  "version":4
               }
            ],
            "private":[
               {
                  "addr":"10.x.x.3",
                  "version":4
               }
            ]
         },
         "services":[
            {
               "name":"datanode"
            },
            {
               "name":"tasktracker"
            },
            {
               "name":"ssh",
               "uri":"ssh://user@168.x.x.3"
            }
         ],
         "links":[
            {
               "rel":"self",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
            },
            {
               "rel":"bookmark",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
            }
         ]
      }
   }
   
           




