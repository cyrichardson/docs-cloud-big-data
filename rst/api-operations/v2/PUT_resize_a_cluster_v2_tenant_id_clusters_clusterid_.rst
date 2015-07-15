=============================================================================
Resize A Cluster -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Resize A Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_resize_a_cluster_v2_tenant_id_clusters_clusterid_.rst#request>`__
`Response <PUT_resize_a_cluster_v2_tenant_id_clusters_clusterid_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/clusters/{clusterId}

Resizes the specified cluster.

This operation resizes the cluster specified by ``clusterId``.

The 400 error code might indicate the presence of unacceptable parameters or malformed data.

The 409 error code might indicate an invalid state.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{clusterId}               |xsd:string               |The cluster ID.          |
+--------------------------+-------------------------+-------------------------+








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
^^^^^^^^^^^^^^^^^^





**Example Resize A Cluster: JSON request**


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
    

