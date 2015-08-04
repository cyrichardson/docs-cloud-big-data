
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

List Cluster Types
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/types

THis operation lists cluster types.



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





**Example List Cluster Types: JSON response**


.. code::

    {
        "types": [
            {
                "id": "HADOOP_HDP1_3",
                "links": [
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP1_3",
                        "rel": "self"
                    },
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP1_3",
                        "rel": "bookmark"
                    }
                ],
                "name": "Hadoop (HDP 1.3)",
                "version": "1.3"
            },
            {
                "id": "HADOOP_HDP2_1",
                "links": [
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP2_1",
                        "rel": "self"
                    },
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP2_1",
                        "rel": "bookmark"
                    }
                ],
                "name": "Hadoop (HDP 2.1)",
                "version": "2.1"
            },
            {
                "id": "SPARK_HDP2_1",
                "links": [
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/SPARK_HDP2_1",
                        "rel": "self"
                    },
                    {
                        "href": "http://dfw.bigdata.api.rackspacecloud.com/1234/types/SPARK_HDP2_1",
                        "rel": "bookmark"
                    }
                ],
                "name": "Spark Technical Preview (HDP 2.1)",
                "version": "2.1"
            }
        ]
    }
        


