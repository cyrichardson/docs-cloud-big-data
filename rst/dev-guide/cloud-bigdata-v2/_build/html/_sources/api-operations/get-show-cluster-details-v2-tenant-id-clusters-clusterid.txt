
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Show Cluster Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/clusters/{clusterId}

This operation shows details for the specified 				cluster.



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
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{clusterId}               |xsd:string               |The cluster ID.          |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""





**Example Show Cluster Details: JSON response**


.. code::

    {
        "cluster": {
            "created": "2014-06-14T10:10:10Z",
            "id": "aaa-bbbb-cccc",
            "name": "test",
            "status": "ACTIVE",
            "stack_id": "HDP2.1_Hadoop",
            "links": [
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc",
                    "rel": "self"
                },
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc",
                    "rel": "bookmark"
                }
            ],
            "node_groups": [
                {
                    "components": [
                        {
                            "name": "Namenode"
                        },
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "YarnTimelineServer"
                        },
                        {
                            "name": "JobHistoryServer"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "master"
                },
                {
                    "components": [
                        {
                            "name": "Namenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "standby-namenode"
                },
                {
                    "components": [
                        {
                            "name": "JournalNode"
                        }
                    ],
                    "count": 3,
                    "flavor_id": "hadoop1-1",
                    "id": "journalnodes"
                },
                {
                    "components": [
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "NodeManager"
                        }
                    ],
                    "count": 10,
                    "flavor_id": "hadoop1-7",
                    "id": "slave",
                },
                {
                    "components": [
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        },
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "PigClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-2",
                    "id": "gateway"
                }
            ],
            "updated": ""
        }
    }
    


