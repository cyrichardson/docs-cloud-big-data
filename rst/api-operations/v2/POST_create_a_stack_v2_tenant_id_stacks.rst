=============================================================================
Create A Stack -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Create A Stack
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <POST_create_a_stack_v2_tenant_id_stacks.rst#request>`__
`Response <POST_create_a_stack_v2_tenant_id_stacks.rst#response>`__

.. code-block:: javascript

    POST /v2/{tenant_id}/stacks

Creates a new stack. ***NOTE: This functionality is not yet implemented.***

This functionality is not yet implemented.

You can create a new stack and start from scratch or use one of the preconfigured global stacks.

The 400 error code might indicate any of the following issues:

The response body is invalid.

A stack with the name already exists.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Create a stack - first   |                         |
|                          |example: JSON response   |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|413                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|distro                    |*(Required)*             |Identifier for a         |
|                          |                         |particular distribution. |
|                          |                         |For example: HDP2.1      |
+--------------------------+-------------------------+-------------------------+
|name                      |*(Required)*             |Descriptive name for the |
|                          |                         |stack. For example:      |
|                          |                         |HDP_Core                 |
+--------------------------+-------------------------+-------------------------+
|description               |*(Required)*             |Description for the      |
|                          |                         |stack.                   |
+--------------------------+-------------------------+-------------------------+
|services                  |*(Required)*             |List of services and     |
|                          |                         |corresponding components.|
+--------------------------+-------------------------+-------------------------+
|node_groups               |*(Required)*             |Definition of the layout |
|                          |                         |of services into grouped |
|                          |                         |cluster nodes.           |
+--------------------------+-------------------------+-------------------------+
|name                      |*(Required)*             |Name of a particular     |
|                          |                         |service. For example:    |
|                          |                         |HDFS                     |
+--------------------------+-------------------------+-------------------------+
|modes                     |*(Required)*             |List of modes to create  |
|                          |                         |for a particular         |
|                          |                         |service. (Certain        |
|                          |                         |services can operate in  |
|                          |                         |different modes.)        |
+--------------------------+-------------------------+-------------------------+
|id                        |*(Required)*             |A node group ID or name. |
+--------------------------+-------------------------+-------------------------+
|components                |*(Required)*             |List of components to    |
|                          |                         |run within the node      |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|count                     |*(Required)*             |Number of instances of   |
|                          |                         |the node group.          |
+--------------------------+-------------------------+-------------------------+
|flavor_id                 |*(Required)*             |Flavor ID for the node   |
|                          |                         |group.                   |
+--------------------------+-------------------------+-------------------------+
|name                      |*(Required)*             |Component name. For      |
|                          |                         |example: Namenode        |
+--------------------------+-------------------------+-------------------------+





**Example Create a stack - first example: JSON request**


.. code::

    {
        "stack": {
            "distro": "HDP2.2",
            "name": "HDP2.2_Hadoop",
            "description": "Core Hadoop Stack with Hive",
            "services": [
                {
                    "name": "HDFS",
                    "modes": ["HA"]
                },
                {
                    "name": "Yarn"
                },
                {
                    "name": "MapReduce"
                },
                {
                    "name": "Hive"
                },
                {
                    "name": "Pig"
                }
            ]
        }
    }
    


**Example Create a stack - second example: JSON request**


.. code::

    {
        "stack": {
            "distro": "HDP2.2",
            "name": "HDP2.2_Hadoop",
            "description": "Core Hadoop Stack with Hive",
            "services": [
                {
                    "name": "HDFS"
                },
                {
                    "name": "Yarn"
                },
                {
                    "name": "MapReduce"
                },
                {
                    "name": "Hive"
                },
                {
                    "name": "Pig"
                }
            ],
            "node_groups": [
                {
                    "components": [
                        {
                            "name": "Namenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "master1"
                },
                {
                    "components": [
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
                    "flavor_id": "hadoop1-4",
                    "id": "master2"
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
                    "id": "slave"
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
                            "name": "PigClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-4",
                    "id": "hive"
                }
            ]
        }
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create a stack - first example: JSON response**


.. code::

    {
        "stack": {
            "id": "aaa-bbb-ccc",
            "created": "2014-06-14T10:10:10Z",
            "distro": "HDP2.2",
            "name": "HDP2.2_Hadoop",
            "description": "Core Hadoop Stack with Hive",
            "links": [
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks/HDP2.2_Hadoop",
                    "rel": "self"
                },
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/stacks/HDP2.2_Hadoop",
                    "rel": "bookmark"
                }
            ],
            "services": [
                {
                    "components": [
                        {
                            "name": "Namenode"
                        },
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "JournalNode"
                        }
                    ],
                    "modes": ["HA"],
                    "name": "HDFS",
                    "version": "2.6"
                },
                {
                    "components": [
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "NodeManager"
                        }
                    ],
                    "name": "Yarn",
                    "version": "2.6"
                },
                {
                    "components": [
                        {
                            "name": "JobHistoryServer"
                        },
                        {
                            "name": "MRClient"
                        }
                    ],
                    "name": "MapReduce",
                    "version": "2.6"
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
                            "name": "HiveAPI"
                        },
                        {
                            "name": "HiveClient"
                        }
                    ],
                    "name": "Hive",
                    "version": "0.14"
                },
                {
                    "components": [
                        {
                            "name": "PigClient"
                        }
                    ],
                    "name": "Pig",
                    "version": "0.14"
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
                    "id": "master",
                    "resource_limits": {
                        "min_count": 1,
                        "max_count": 1,
                        "min_ram": 6144
                    }
                },
                {
                    "components": [
                        {
                            "name": "Namenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "standby-namenode",
                    "resource_limits": {
                        "min_count": 1,
                        "max_count": 1,
                        "min_ram": 2048
                    }
                },
                {
                    "components": [
                        {
                            "name": "JournalNode"
                        }
                    ],
                    "count": 3,
                    "flavor_id": "hadoop1-1",
                    "id": "journalnodes",
                    "resource_limits": {
                        "min_count": 3,
                        "max_count": 99,
                        "min_ram": 1024
                    }
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
                    "id": "slave",
                    "resource_limits": {
                        "min_count": 1,
                        "max_count": 9999,
                        "min_ram": 6144
                    }
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
                    "id": "gateway",
                    "resource_limits": {
                        "min_count": 1,
                        "max_count": 1,
                        "min_ram": 2048
                    }
                }
            ]
        }
    }
    

