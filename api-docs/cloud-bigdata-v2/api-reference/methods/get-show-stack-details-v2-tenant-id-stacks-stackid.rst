.. _get-show-stack-details-v2-tenant-id-stacks-stackid:

Show stack details
~~~~~~~~~~~~~~~~~~

.. code::

    GET /v2/{tenant_id}/stacks/{stackId}

This operation shows details for the specified 	stack.


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
-------

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{stackId}                 |String                   |The stack ID.            |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.

Response
--------

**Example Show stack details: JSON response**


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





