=============================================================================
List Available Flavors -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List Available Flavors
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_available_flavors_v2_tenant_id_flavors.rst#request>`__
`Response <GET_list_available_flavors_v2_tenant_id_flavors.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/flavors

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
                "disk": 10000,
                "id": "hadoop1-60",
                "name": "XLarge Hadoop Instance",
                "ram": 61440,
                "vcpus": 16,
                "class": "hadoop1"
            },
            {
                "disk": 1250,
                "id": "hadoop1-7",
                "name": "Small Hadoop Instance",
                "ram": 8192,
                "vcpus": 2,
                "class": "hadoop1"
            },
            {
                "disk": 3200,
                "id": "onmetal-io1",
                "name": "OnMetal IO 1",
                "ram": 122880,
                "vcpus": 40,
                "class": "onmetal"
            }
        ],
        "links": [
            {
                "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/flavors?limit=2&amp;marker=hadoop1-7",
                "rel": "next"
            }
        ]
    }
    

