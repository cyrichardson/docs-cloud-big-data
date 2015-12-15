.. _resize-clusters:

Resizing clusters
~~~~~~~~~~~~~~~~~~

You can increase or decrease the size of an existing cluster by using the resize operation.

Following is the operation template:

.. code::

     GET /v2/{tenant_id}/clusters/{clusterId}
     
In the following :ref:`cURL<resize-cluster-curl-example>` and 
:ref:`client<resize-cluster-client-example>` examples, the resize operations increases the 
size of the test cluster to add four slave nodes. 

In the resize operation parameters, you specify the total number nodes per node group 
that you want the cluster to have, not just the number of nodes to add or remove. 

After you complete the operations, you can use the :ref:`view nodes<view-node-details>` 
operation to confirm that the resize operation had the intended affect. 
    
.. _resize-cluster-curl-example:
    
cURL example
^^^^^^^^^^^^^^

The following examples show the resize cluster cURL request and corresponding response to 
add 4 slave nodes to a cluster.
 
**Resize cluster cURL request**

.. code::  

    $ curl -i -X PUT $ENDPOINT/clusters/$testClusterId -d \
        -H "Accept: application/json" \
        -H "X-Auth-Token:$AUTH_TOKEN" \
        -H "Content-Type: application/json"  

 
**JSON request body**

.. code::  

    {
        "cluster": {
            "node_groups": [
                {
                    "count": 4,
                    "id": "slave"
                }
            ]
        }
    }

 
**JSON response**

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
                    "count": 4,
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

    
.. _resize-cluster-client-example:
    
Client example
^^^^^^^^^^^^^^^^^

The following example shows the ``clusters resize`` client command to add 4 slave 
nodes to a cluster. 
 
**Resize a cluster by using the lava client**

.. code::  

    $ lava clusters resize c5444b98-f4b4-aaaa-bbbb-b6e9d3313da1 --node-groups='slave(flavor_id=hadoop1-7, count=4)'
    +----------------------------------------------------+
    |                      Cluster                       |
    +-------------+--------------------------------------+
    | ID          | c5444b98-f4b4-aaaa-bbbb-b6e9d3313da1 |
    | Name        |                                 test |
    | Status      |                             UPDATING |
    | Stack       |                         KAFKA_HDP2_2 |
    | Created     |            2015-05-30 06:10:37+00:00 |
    | CBD Version |                                    2 |
    | Username    |                              cbduser |
    | Progress    |                                 0.00 |
    +-------------+--------------------------------------+

    +------------------------------------------------------------+
    |                        Node Groups                         |
    +-----------+-----------+-------+----------------------------+
    |     ID    |   Flavor  | Count |         Components         |
    +-----------+-----------+-------+----------------------------+
    |   master  | hadoop1-4 |     1 |     [{name=Namenode}]      |
    | secondary | hadoop1-4 |     1 | [{name=SecondaryNamenode}] |
    |   slave   | hadoop1-7 |     4 |     [{name=Datanode},      |
    |           |           |       |    {name=KafkaBroker},     |
    |           |           |       |  {name=ZookeeperClient}]   |
    | zookeeper | hadoop1-2 |     3 |  [{name=ZookeeperServer},  |
    |           |           |       |  {name=ZookeeperClient}]   |
    +-----------+-----------+-------+----------------------------+

