
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Resize A Cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    PUT /v2/{tenant_id}/clusters/{clusterId}

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
|{clusterId}               |xsd:string               |The cluster ID.          |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




**Example Resize A Cluster: JSON request**


.. code::

    {
        "cluster": {
            "node_groups": [
                {
                    "count": 15,
                    "id": "slave"
                }
            ]
        }
    }


Response
""""""""""""""""


This operation does not accept a response body.




**Example Resize A Cluster: JSON response**


.. code::

    {
        "cluster": {
            "created": "2014-06-14T10:10:10Z",
            "id": "aaa-bbbb-cccc",
            "name": "test",
            "status": "UPDATING",
            "progress": "5",
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
            "stack_id": "HDP2.1_Hadoop",
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
                    "count": 15,
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
            "updated": "2014-06-25T10:10:10Z"
        }
    }
    

