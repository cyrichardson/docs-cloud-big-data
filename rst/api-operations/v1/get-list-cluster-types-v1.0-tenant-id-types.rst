
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
List Cluster Types -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List Cluster Types
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <get-list-cluster-types-v1.0-tenant-id-types.html#request>`__
`Response <get-list-cluster-types-v1.0-tenant-id-types.html#response>`__

.. code::

    GET /v1.0/{tenant_id}/types

Lists cluster types.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^





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
        

