.. _create-cluster:

Creating a cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

When you use the Cloud Big Data service, you can create a :ref:`cluster<clusters-def>` 
of virtual and OnMetal servers to host your Hadoop instance.

You can create a stack or use one of the preconfigured stacks. 

Following is the operation template:

.. code::

     POST /v2/{tenant_id}/clusters
    
 
cURL example
^^^^^^^^^^^^^^

Use the cURL request shown in the following example to create a server cluster on the 
Cloud Big Data service.  The example shows the cURL request, request body, and the 
corresponding response body.
 
**Example: Create cluster cURL request**

.. code::  

    curl -i -X POST $API_ENDPOINT/clusters -d \
    -H "X-Auth-Token: $AUTH_TOKEN" \
    -H "Accept: application/json" \
    -H "Content-type: application/json"

 
**JSON request body**

.. code::  

    {
        "cluster": {
            "name": "test",
            "username": "cbduser",
            "ssh_keys": ["cbdkey"],
            "stack_id": "HDP2.1_Hadoop",
            "node_groups": [
                {
                    "count": 10,
                    "flavor_id": "hadoop1-7",
                    "id": "slave"
                }
            ],
            "connectors": [
                {
                    "type": "cloud_files",
                    "credential": {
                        "name": "cfuser"
                    }
                }
            ],
            "scripts": [
                {
                    "id": "c5033423-97ff-4215-9552-19d425e1f9dd"
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
            "username": "cbduser",
            "ssh_keys": ["cbdkey"],
            "status": "BUILDING",
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
            "updated": "",
            "connectors": [
                {
                    "type": "cloud_files",
                    "credential": {
                        "name": "cfuser"
                    }
                }
            ],
            "scripts": [
                {
                    "id": "c5033423-97ff-4215-9552-19d425e1f9dd",
                    "name": "Mongo Connector",
                    "status": "PENDING"
                }
            ]
        }
    }



Client example
^^^^^^^^^^^^^^^^^

Using the client, create a cluster using the ``clusters create`` lava client command
as shown in the following example.

 
**Create a cluster by using the lava client**

.. code::  

    $ lava clusters create test KAFKA_HDP2_2 --node-groups='slave(flavor_id=hadoop1-7, count=3)' \
    --ssh-key cbdkey --username cbduser
    +----------------------------------------------------+
    |                      Cluster                       |
    +-------------+--------------------------------------+
    | ID          | c5444b98-f4b4-aaaa-bbbb-b6e9d3313da1 |
    | Name        |                                 test |
    | Status      |                             BUILDING |
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
    |   slave   | hadoop1-7 |     3 |     [{name=Datanode},      |
    |           |           |       |    {name=KafkaBroker},     |
    |           |           |       |  {name=ZookeeperClient}]   |
    | zookeeper | hadoop1-2 |     3 |  [{name=ZookeeperServer},  |
    |           |           |       |  {name=ZookeeperClient}]   |
    +-----------+-----------+-------+----------------------------+
