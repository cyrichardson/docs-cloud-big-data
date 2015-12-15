.. _view-node-details:

Viewing node details
~~~~~~~~~~~~~~~~~~~~~~

Use the view node details operation to get information about all server nodes 
in a specified cluster.


Following is the operation template:

.. code::

     GET /v2/{tenant_id}/clusters/{clusterId}/nodes
     
In the :ref:`cURL<node-details-curl-ex>` and :ref:`client<node-details-client-ex>`  
examples for the view node details operations, the cluster includes 
the following components:

-  One master node

-  Two slave nodes

Each server node has the following IP addresses:

-  A private IP address that is used for backend (Hadoop) data transfers

-  A public IP address that allows you to access the server over the
   public Internet

     
.. _node-details-curl-ex:
     
cURL example
^^^^^^^^^^^^^^

The following example shows the cURL request and corresponding response for listing all 
nodes in a cluster.

You can use SSH to connect to a node through the IP address. Supply your 
account username and the SSH key for the cluster in the connection request. 

.. note:: 
    Use the :ref:`Credentials <create-manage-credentials>` operations to get information 
    about SSH key credentials.

 
**List node details cURL request**

.. code::  

    $ curl -i -X GET $ENDPOINT/clusters/ac111111-2d86-4597-8010-cbe787bbbc41/nodes -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-Type: application/json"

 
**JSON response**

.. code::  

    {
        "nodes": [
            {
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-444",
                "name": "master-1",
                "node_group": "master",
                "status": "ACTIVE",
                "updated": "",
                "addresses": {
                    "public": [
                        {
                            "addr": "168.x.x.3",
                            "version": 4
                        }
                    ],
                    "private": [
                        {
                            "addr": "10.x.x.3",
                            "version": 4
                        }
                    ]
                },
                "flavor_id": "hadoop1-4",
                "components": [
                    {
                        "name": "Namenode",
                        "nice_name": "HDFS Namenode",
                        "uri": "http://master-1.local:50070"
                    },
                    {
                        "name": "ResourceManager",
                        "nice_name": "YARN Resource Manager",
                        "uri": "http://master-1.local:8088"
                    },
                    {
                        "name": "YarnTimelineServer",
                        "nice_name": "YARN Timeline History Server",
                        "uri": "http://master-1.local:8188"
                    },
                    {
                        "name": "JobHistoryServer",
                        "nice_name": "MapReduce History Server",
                        "uri": "http://master-1.local:19888"
                    }
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-444"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-444"
                    }
                ]
            },
            {
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-333",
                "name": "slave-1",
                "node_group": "slave",
                "status": "ACTIVE",
                "updated": "",
                "addresses": {
                    "public": [
                        {
                            "addr": "168.x.x.4",
                            "version": 4
                        }
                    ],
                    "private": [
                        {
                            "addr": "10.x.x.4",
                            "version": 4
                        }
                    ]
                },
                "flavor_id": "hadoop1-7",
                "components": [
                    {
                        "name": "Datanode",
                        "nice_name": "HDFS Datanode",
                        "uri": "http://slave-1.local:50075"
                    },
                    {
                        "name": "NodeManager",
                        "nice_name": "YARN Node Manager",
                        "uri": "http://slave-1.local:8042"
                    },
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-333"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-333"
                    }
                ]
            },
            {
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-555",
                "name": "slave-2",
                "node_group": "slave",
                "status": "ACTIVE",
                "updated": "",
                "addresses": {
                    "public": [
                        {
                            "addr": "168.x.x.5",
                            "version": 4
                        }
                    ],
                    "private": [
                        {
                            "addr": "10.x.x.5",
                            "version": 4
                        }
                    ]
                },
                "flavor_id": "hadoop1-7",
                "components": [
                    {
                        "name": "Datanode",
                        "nice_name": "HDFS Datanode",
                        "uri": "http://slave-2.local:50075"
                    },
                    {
                        "name": "NodeManager",
                        "nice_name": "YARN Node Manager",
                        "uri": "http://slave-2.local:8042"
                    },
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-555"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-555"
                    }
                ]
            }
        ],
        "links":[
            {
                "rel":"next",
                "href":"https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes?limit=3&marker=111-222-555"
            }
        ]
    }

    
.. _node-details-client-ex:
    
Client example
^^^^^^^^^^^^^^^^^

The following example shows the ``nodes list`` lava client command to get 
details about the server nodes in a specified cluster. 

**List server nodes by using the lava client**

.. code::  

    $ lava nodes list cc5444b98-f4b4-aaaa-bbbb-b6e9d3313da1
    +--------------------------------------+-------------+-----------+--------+----------------+----------------+--------------------------------+
    |                  ID                  |     Name    |    Role   | Status |   Public IP    |   Private IP   |           Components           |
    +--------------------------------------+-------------+-----------+--------+----------------+----------------+--------------------------------+
    | 057b24f1-6397-4c46-ba59-3649a32db23d |   master-1  |   master  | ACTIVE | 166.78.133.67  | 10.190.241.50  |   [{nice_name=HDFS Namenode,   |
    |                                      |             |           |        |                |                | name=Namenode, uri=http://mast |
    |                                      |             |           |        |                |                |       er-1.local:50070}]       |
    | 42bca320-9581-4321-b835-668216c3e3a9 |   slave-1   |   slave   | ACTIVE | 166.78.132.244 | 10.190.240.242 |   [{nice_name=HDFS Datanode,   |
    |                                      |             |           |        |                |                | name=Datanode, uri=http://slav |
    |                                      |             |           |        |                |                |       e-1.local:50075},        |
    |                                      |             |           |        |                |                |    {nice_name=Kafka Broker,    |
    |                                      |             |           |        |                |                |       name=KafkaBroker},       |
    |                                      |             |           |        |                |                |  {nice_name=Zookeeper Client,  |
    |                                      |             |           |        |                |                |     name=ZookeeperClient}]     |
    | 4818bc5c-82e1-4392-800e-0667519b0129 |   slave-2   |   slave   | ACTIVE | 166.78.132.249 | 10.190.240.246 |   [{nice_name=HDFS Datanode,   |
    |                                      |             |           |        |                |                | name=Datanode, uri=http://slav |
    |                                      |             |           |        |                |                |       e-2.local:50075},        |
    |                                      |             |           |        |                |                |    {nice_name=Kafka Broker,    |
    |                                      |             |           |        |                |                |       name=KafkaBroker},       |
    |                                      |             |           |        |                |                |  {nice_name=Zookeeper Client,  |
    |                                      |             |           |        |                |                |     name=ZookeeperClient}]     |
    +--------------------------------------+-------------+-----------+--------+----------------+----------------+--------------------------------+
