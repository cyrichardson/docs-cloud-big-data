=============================================================================
List Cluster Types -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List Cluster Types
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_cluster_types_v1.0_tenant_id_types.rst#request>`__
`Response <GET_list_cluster_types_v1.0_tenant_id_types.rst#response>`__

.. code-block:: javascript

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





**Example List Cluster Types: JSON request**


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
        

