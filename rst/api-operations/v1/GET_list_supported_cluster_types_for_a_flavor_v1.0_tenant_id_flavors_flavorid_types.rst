=============================================================================
List Supported Cluster Types For A Flavor -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List Supported Cluster Types For A Flavor
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_supported_cluster_types_for_a_flavor_v1.0_tenant_id_flavors_flavorid_types.rst#request>`__
`Response <GET_list_supported_cluster_types_for_a_flavor_v1.0_tenant_id_flavors_flavorid_types.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/flavors/{flavorId}/types

Lists the supported cluster types for a specified flavor.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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
|{flavorId}                |xsd:string               |Specifies the flavor ID. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Supported Cluster Types For A Flavor: JSON request**


.. code::

    {
        "types": [
            {
                "id": "HADOOP_HDP1_3",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP1_3",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP1_3",
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
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP2_1",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP2_1",
                        "rel": "bookmark"
                    }
                ],
                "name": "Hadoop (HDP 2.1)",
                "version": "2.1"
            }
        ]
    }

