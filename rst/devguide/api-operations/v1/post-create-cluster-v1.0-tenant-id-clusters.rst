
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Create Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /v1.0/{tenant_id}/clusters

Creates a cluster.

.. note::
   You must create your profile before you create 					a cluster.
   
   

The ``postInitScript`` request parameter 				specifies a URL that downloads a script that runs 				after the cluster is created. The status of the run is 				shown in the ``postInitScriptStatus`` 				response parameter.

Possible values for ``postInitScriptStatus`` are ``FAILED``, ``PENDING``, ``DELIVERED``, ``RUNNING``, ``SUCCEEDED``, and ``None``.

The ``progress`` response parameter is 				calculated based on the number of nodes in the cluster 				and their progress through configuration. Currently, 				the calculation is as follows but is subject to 				change:



*  BUILDING: progress = 0.5 * 						configuring_count / 					len(self.nodes)
*  CONFIGURING/RESIZING: progress = 0.5 + 						(0.5 * active_count / 					len(self.nodes))
*  ACTIVE: progress = 					1.0


The 400 error code might indicate any of the 				following issues:



*  The 						response body is 						invalid.
*  You 						need to create a user 					profile.
*  The node 						count is 						invalid.
*  The 						flavor is 						invalid.
*  The 						data is 				malformed.


The 413 error code might indicate that the resource 				limit is exceeded.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |Bad Request              |The user-provided        |
|                          |                         |request contained an     |
|                          |                         |error.                   |
+--------------------------+-------------------------+-------------------------+
|413                       |Request Entity Too Large |The resource quota was   |
|                          |                         |exceeded.                |
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





This operation does not accept a request body.




**Example Create Cluster: JSON request**


.. code::

    {
       "cluster":{
          "name":"slice",
          "clusterType":"HADOOP_HDP2_1",
          "flavorId":"hadoop1-7",
          "nodeCount":5,
          "postInitScript":"http://example.com/configure_cluster.sh"
       }
    }


Response
""""""""""""""""


This operation does not accept a response body.




**Example Create Cluster: JSON response**


.. code::

    {
       "cluster":{
          "id":"db478fc1-2d86-4597-8010-cbe787bbbc41",
          "created":"2012-12-27T10:10:10Z",
          "updated":"",
          "name":"slice",
          "clusterType":"HADOOP_HDP2_1",
          "flavorId":"hadoop1-7",
          "nodeCount":5,
          "postInitScriptStatus":"PENDING",
          "progress":0.0,
          "status":"BUILDING",
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

