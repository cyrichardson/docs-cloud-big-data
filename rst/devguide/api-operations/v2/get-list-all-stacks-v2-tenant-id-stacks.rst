
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

List All Stacks
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/stacks

This operation lists all stacks, includingglobal stacks and user-created stacks.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
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





This operation does not accept a request body.




Response
""""""""""""""""


This operation does not accept a response body.




**Example List All Stacks: JSON response**


.. code::

    {
        "stacks": [
            {
                "distro": "HDP2.2",
                "id": "HDP2.2_Hadoop",
                "name": "Core Hadoop",
                "description": "Core Hadoop Stack with Hive",
                "services": [
                    {
                        "modes": ["HA"],
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
            },
            {
                "distro": "HDP2.2",
                "id": "HDP2.2_HBase",
                "name": "HBase",
                "description": "Core Hadoop Stack with HBase",
                "services": [
                    {
                        "modes": ["HA"],
                        "name": "HDFS"
                    },
                    {
                        "name": "Yarn"
                    },
                    {
                        "name": "HBase"
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
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks/HDP2.2_HBase",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/stacks/HDP2.2_HBase",
                        "rel": "bookmark"
                    }
                ],
            }
        ],
        "links": [
            {
                "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks?limit=2&marker=HDP2.2_HBase",
                "rel": "next"
            },
        ]
    }
    

