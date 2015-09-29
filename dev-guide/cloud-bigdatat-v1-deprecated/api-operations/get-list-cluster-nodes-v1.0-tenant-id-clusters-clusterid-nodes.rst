
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-list-cluster-nodes-v1.0-tenant-id-clusters-clusterid-nodes:

List cluster nodes
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/clusters/{clusterId}/nodes

This operation lists all nodes for a specified 				cluster.

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





This operation does not accept a request body.




**Example List cluster nodes: JSON request**


.. code::

   GET https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/ac111111-2d86-4597-8010-cbe787bbbc41/nodes
   Accept: application/json 
   X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
   Content-Type: application/json              





Response
""""""""""""""""










**Example List cluster nodes: JSON response**


.. code::

   {
      "nodes":[
         {
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
                  "name":"namenode"
               },
               {
                  "name":"jobtracker"
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
         },
         {
            "id":"aaa",
            "role":"GATEWAY",
            "name":"GATEWAY-1",
            "postInitScriptStatus":null,
            "status":"ACTIVE",
            "addresses":{
               "public":[
                  {
                     "addr":"168.x.x.4",
                     "version":4
                  }
               ],
               "private":[
                  {
                     "addr":"10.x.x.4",
                     "version":4
                  }
               ]
            },
            "services":[
               {
                  "name":"pig"
               },
               {
                  "name":"hive"
               },
               {
                  "name":"ssh",
                  "uri":"ssh://user@168.x.x.4"
               },
               {
                  "name":"status",
                  "uri":"http://10.x.x.4"
               },
               {
                  "name":"hdfs-scp",
                  "uri":"scp://user@168.x.x.4:9022"
               }
            ],
            "links":[
               {
                  "rel":"self",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
               },
               {
                  "rel":"bookmark",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
               }
            ]
         },
         {
            "id":"bbb",
            "role":"DATANODE",
            "name":"DATANODE-1",
            "postInitScriptStatus":null,
            "status":"ACTIVE",
            "addresses":{
               "public":[
                  {
                     "addr":"168.x.x.5",
                     "version":4
                  }
               ],
               "private":[
                  {
                     "addr":"10.x.x.5",
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
                  "uri":"ssh://user@168.x.x.5"
               }
            ],
            "links":[
               {
                  "rel":"self",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/bbb"
               },
               {
                  "rel":"bookmark",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/bbb"
               }
            ]
         },
         {
            "id":"ccc",
            "role":"DATANODE",
            "name":"DATANODE-2",
            "postInitScriptStatus":null,
            "status":"ACTIVE",
            "addresses":{
               "public":[
                  {
                     "addr":"168.x.x.6",
                     "version":4
                  }
               ],
               "private":[
                  {
                     "addr":"10.x.x.6",
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
                  "uri":"ssh://user@168.x.x.6"
               }
            ],
            "links":[
               {
                  "rel":"self",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/ccc"
               },
               {
                  "rel":"bookmark",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/ccc"
               }
            ]
         }
      ]
   }




