.. _post-create-a-stack-v2:

Create a stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /v2/{tenant_id}/stacks

This operation creates a new stack. You can create a new stack and start from scratch or 
use one of the preconfigured global stacks.
   

.. note::
   This functionality is not yet implemented.
      

The 400 error code might indicate any of the following issues:

-  The response body is invalid.
-  A stack with the name already exists.

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
|413                       |Request Entity Too Large |The resource quota was   |
|                          |                         |exceeded.                |
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

This table shows the body parameters for the request:

+--------------------------------+----------------------+----------------------+
|Name                            |Type                  |Description           |
+================================+======================+======================+
|**stack**                       |*(Required)*          |Stack information.    |
+--------------------------------+----------------------+----------------------+
|stack.\ **distro**              |*(Required)*          |Identifier for a      |
|                                |                      |particular            |
|                                |                      |distribution. For     |
|                                |                      |example: HDP2.1       |
+--------------------------------+----------------------+----------------------+
|stack.\ **name**                |*(Required)*          |Descriptive name for  |
|                                |                      |the stack. For        |
|                                |                      |example: HDP_Core     |
+--------------------------------+----------------------+----------------------+
|stack.\ **description**         |*(Optional)*          |Description for the   |
|                                |                      |stack.                |
+--------------------------------+----------------------+----------------------+
|stack.\ **services**            |*(Required)*          |List of services and  |
|                                |                      |corresponding         |
|                                |                      |components.           |
|stack.services.\ **name**       |*(Required)*          |Name of a particular  |
|                                |                      |service. For example: |
|                                |                      |HDFS                  |
+--------------------------------+----------------------+----------------------+
|stack.services.\ **modes**      |*(Optional)*          |List of modes to      |
|                                |                      |create for a          |
|                                |                      |particular service.   |
|                                |                      |(Certain services can |
|                                |                      |operate in different  |
|                                |                      |modes.)               |
+--------------------------------+----------------------+----------------------+
|stack.\ **node_groups**         |*(Optional)*          |Definition of the     |
|                                |                      |layout of services    |
|                                |                      |into grouped cluster  |
|                                |                      |nodes.                |
+--------------------------------+----------------------+----------------------+
|stack.node_groups.\ **id**      |*(Required)*          |A node group ID or    |
|                                |                      |name.                 |
+--------------------------------+----------------------+----------------------+
|stack.node_groups.\             |*(Required)*          |List of components to |
|**components**                  |                      |run within the node   |
|                                |                      |group.                |
+--------------------------------+----------------------+----------------------+
|stack.node_groups.components.\  |*(Required)*          |Component name. For   |
|**name**                        |                      |example: Namenode     |
+--------------------------------+----------------------+----------------------+
|stack.node_groups.\ **count**   |*(Optional)*          |Number of instances   |
|                                |                      |of the node group.    |
+--------------------------------+----------------------+----------------------+
|stack.node_groups.\             |*(Optional)*          |Flavor ID for the     |
|**flavor_id**                   |                      |node group.           |
+--------------------------------+----------------------+----------------------+


**Example Create a stack: JSON request**


.. code::

   {
       "stack": {
           "distro": "HDP2.3",
           "name": "HDP2.3_Hadoop",
           "description": "Core Hadoop Stack with Hive",
           "services": [
               {
                   "name": "HDFS",
                   "modes": ["Secondary"]
               },
               {
                   "name": "YARN"
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
   


Response
""""""""""""""""


.. code::

   {
        "stack": {
            "created": "2016-02-19T15:36:10+00:00",
            "description": "Core Hadoop Stack with Hive",
            "distro": "HDP2.3",
            "id": "d1a2b3cb-5423-4b91-a804-02970b05159a",
            "is_deletable": true,
            "links": [
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/123456/stacks/d1a2b3cb-5423-4b91-a804-02970b05159a",
                    "rel": "self"
                },
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/123456/stacks/d1a2b3cb-5423-4b91-a804-02970b05159a",
                    "rel": "bookmark"
                }
            ],
            "name": "HDP2.3_Hadoop",
            "node_groups": [
                {
                    "components": [
                        {
                            "name": "AmbariServer"
                        },
                        {
                            "name": "AmbariMetricsCollector"
                        },
                        {
                            "name": "ZookeeperServer"
                        },
                        {
                            "name": "ZookeeperClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-4",
                    "id": "ambari",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 1520
                    }
                },
                {
                    "components": [
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        },
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        },
                        {
                            "name": "Namenode"
                        },
                        {
                            "name": "MRHistoryServer"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "master0",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 6645
                    }
                },
                {
                    "components": [
                        {
                            "name": "SecondaryNamenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-2",
                    "id": "master1",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 1126
                    }
                },
                {
                    "components": [
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "MRClient"
                        },
                        {
                            "name": "PigClient"
                        },
                        {
                            "name": "HdfsScp"
                        },
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "NodeManager"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "slave0",
                    "resource_limits": {
                        "max_count": 999,
                        "min_count": 1,
                        "min_ram": 5237
                    }
                }
            ],
            "services": [
                {
                    "components": [
                        {
                            "name": "SecondaryNamenode"
                        },
                        {
                            "name": "HdfsScp"
                        },
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "Namenode"
                        }
                    ],
                    "modes": [
                        "Secondary"
                    ],
                    "name": "HDFS",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        },
                        {
                            "name": "NodeManager"
                        }
                    ],
                    "modes": [],
                    "name": "YARN",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "MRClient"
                        },
                        {
                            "name": "MRHistoryServer"
                        }
                    ],
                    "modes": [],
                    "name": "MapReduce",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        }
                    ],
                    "modes": [],
                    "name": "Hive",
                    "version": "1.2.1"
                },
                {
                    "components": [
                        {
                            "name": "PigClient"
                        }
                    ],
                    "modes": [],
                    "name": "Pig",
                    "version": "0.15.0"
                }
            ]
        }
    }



**Example JSON request with node_groups**


.. code::

   {
        "stack": {
            "description": "Core Hadoop Stack with Hive",
            "distro": "HDP2.3",
            "name": "HDP2.3_Hadoop",
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
                            "name": "HiveAPI"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        },
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        },
                        {
                            "name": "MRHistoryServer"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "master0"
                },
                {
                    "components": [
                        {
                            "name": "SecondaryNamenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-4",
                    "id": "master1"
                },
                {
                    "components": [
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "HdfsScp"
                        },
                        {
                            "name": "NodeManager"
                        },
                        {
                            "name": "MRClient"
                        },
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "PigClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "slave0"
                }
            ],
            "services": [
                {
                    "name": "HDFS"
                },
                {
                    "name": "YARN"
                },
                {
                    "name": "Hive"
                },
                {
                    "name": "MapReduce"
                },
                {
                    "name": "Pig"
                }
            ]
        }
    }


**Example JSON response**


.. code::

   {
        "stack": {
            "created": "2016-02-19T04:21:03+00:00",
            "description": "Core Hadoop Stack with Hive",
            "distro": "HDP2.3",
            "id": "d1a2b3cb-5423-4b91-a804-02970b05159a",
            "is_deletable": true,
            "links": [
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/123456/stacks/d1a2b3cb-5423-4b91-a804-02970b05159a",
                    "rel": "self"
                },
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/123456/stacks/d1a2b3cb-5423-4b91-a804-02970b05159a",
                    "rel": "bookmark"
                }
            ],
            "name": "HDP2.3_Hadoop",
            "node_groups": [
                {
                    "components": [
                        {
                            "name": "AmbariServer"
                        },
                        {
                            "name": "AmbariMetricsCollector"
                        },
                        {
                            "name": "ZookeeperServer"
                        },
                        {
                            "name": "ZookeeperClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-4",
                    "id": "ambari",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 1520
                    }
                },
                {
                    "components": [
                        {
                            "name": "Namenode"
                        },
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        },
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        },
                        {
                            "name": "MRHistoryServer"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "master0",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 6645
                    }
                },
                {
                    "components": [
                        {
                            "name": "SecondaryNamenode"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-4",
                    "id": "master1",
                    "resource_limits": {
                        "max_count": 1,
                        "min_count": 1,
                        "min_ram": 1126
                    }
                },
                {
                    "components": [
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "HdfsScp"
                        },
                        {
                            "name": "NodeManager"
                        },
                        {
                            "name": "MRClient"
                        },
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "PigClient"
                        }
                    ],
                    "count": 1,
                    "flavor_id": "hadoop1-7",
                    "id": "slave0",
                    "resource_limits": {
                        "max_count": 999,
                        "min_count": 1,
                        "min_ram": 5237
                    }
                }
            ],
            "services": [
                {
                    "components": [
                        {
                            "name": "SecondaryNamenode"
                        },
                        {
                            "name": "HdfsScp"
                        },
                        {
                            "name": "Datanode"
                        },
                        {
                            "name": "Namenode"
                        }
                    ],
                    "modes": [
                        "Secondary"
                    ],
                    "name": "HDFS",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        },
                        {
                            "name": "NodeManager"
                        }
                    ],
                    "modes": [],
                    "name": "YARN",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "MRClient"
                        },
                        {
                            "name": "MRHistoryServer"
                        }
                    ],
                    "modes": [],
                    "name": "MapReduce",
                    "version": "2.7.1"
                },
                {
                    "components": [
                        {
                            "name": "HiveClient"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        }
                    ],
                    "modes": [],
                    "name": "Hive",
                    "version": "1.2.1"
                },
                {
                    "components": [
                        {
                            "name": "PigClient"
                        }
                    ],
                    "modes": [],
                    "name": "Pig",
                    "version": "0.15.0"
                }
            ]
        }
    }
