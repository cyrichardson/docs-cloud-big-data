
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Resize Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /v1.0/{tenant_id}/clusters/{clusterId}/action

This operation resizes the cluster specified by ``clusterId``.

The 400 error code might indicate the presence of 				unacceptable parameters or malformed data.

The 409 error code might indicate an invalid 				state.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
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




**Example Resize Cluster: JSON request**


.. code::

    {
       "resize":{
          "nodeCount":10
       }
    }      


Response
""""""""""""""""





**Example Resize Cluster: JSON response**


.. code::

    {
       "cluster":{
          "id":"db478fc1-2d86-4597-8010-cbe787bbbc41",
          "created":"2012-12-27T10:10:10Z",
          "updated":"2012-12-27T16:20:10Z",
          "name":"slice",
          "clusterType":"HADOOP_HDP2_1",
          "flavorId":"hadoop1-7",
          "nodeCount":10,
          "postInitScriptStatus":"PENDING",
          "progress":0.5,
          "status":"UPDATING",
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
            


