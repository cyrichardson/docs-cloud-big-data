=============================================================================
List Available Flavors -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List Available Flavors
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_available_flavors_v1.0_tenant_id_flavors.rst#request>`__
`Response <GET_list_available_flavors_v1.0_tenant_id_flavors.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/flavors

Lists all available flavors, including the drive size and amount of RAM.



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





**Example List Available Flavors: JSON request**


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
            {
                "disk": 3200,
                "id": "onmetal-io1",
                "links": [
                    {
                        "href": "https://iad.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/onmetal-io1",
                        "rel": "self"
                    },
                    {
                        "href": "https://iad.bigdata.api.rackspacecloud.com/1234/flavors/onmetal-io1",
                        "rel": "bookmark"
                    }
                ],
                "name": "OnMetal IO v1",
                "ram": 131072,
                "vcpus": 40
            }
        ]
    }
    

