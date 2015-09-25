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
|stack.node_groups.components.\  |*(Required)*          |Component name. For   |
|**name**                        |                      |example: Namenode     |
+--------------------------------+----------------------+----------------------+

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
""""""""""""""""










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
                       }
                   ],
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
                       }
                   ],
                   "count": 1,
                   "flavor_id": "hadoop1-7",
                   "id": "master1",
                   "resource_limits": {
                       "min_count": 1,
                       "max_count": 1,
                       "min_ram": 2048
                   }
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
                   "id": "master2",
                   "resource_limits": {
                       "min_count": 1,
                       "max_count": 1,
                       "min_ram": 4096
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
                           "name": "PigClient"
                       }
                   ],
                   "count": 1,
                   "flavor_id": "hadoop1-4",
                   "id": "hive",
                   "resource_limits": {
                       "min_count": 1,
                       "max_count": 1,
                       "min_ram": 2048
                   }
               }
           ]
       }
   }
   




