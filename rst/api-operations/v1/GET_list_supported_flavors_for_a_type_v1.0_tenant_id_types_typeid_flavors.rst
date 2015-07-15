=============================================================================
List Supported Flavors For A Type -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List Supported Flavors For A Type
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_supported_flavors_for_a_type_v1.0_tenant_id_types_typeid_flavors.rst#request>`__
`Response <GET_list_supported_flavors_for_a_type_v1.0_tenant_id_types_typeid_flavors.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/types/{typeId}/flavors

Lists the supported flavors for a specified cluster type.



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
|{typeId}                  |xsd:string               |Specifies the type ID.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Supported Flavors For A Type: JSON request**


.. code::

    {
        "flavors": [
            {
                "disk": 2500,
                "id": "hadoop1-15",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-15",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-15",
                        "rel": "bookmark"
                    }
                ],
                "name": "Medium Hadoop Instance",
                "ram": 15360,
                "vcpus": 4
            },
            {
                "disk": 5000,
                "id": "hadoop1-30",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-30",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-30",
                        "rel": "bookmark"
                    }
                ],
                "name": "Large Hadoop Instance",
                "ram": 30720,
                "vcpus": 8
            },
            {
                "disk": 10000,
                "id": "hadoop1-60",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-60",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-60",
                        "rel": "bookmark"
                    }
                ],
                "name": "XLarge Hadoop Instance",
                "ram": 61440,
                "vcpus": 16
            },
            {
                "disk": 1250,
                "id": "hadoop1-7",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-7",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-7",
                        "rel": "bookmark"
                    }
                ],
                "name": "Small Hadoop Instance",
                "ram": 7680,
                "vcpus": 2
            }
        ]
    }
    

