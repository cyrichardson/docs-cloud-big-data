
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

List Supported Flavors For A Type
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/types/{typeId}/flavors

This operation lists the supported flavors for a 				specified cluster type.



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
""""""""""""""""

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{typeId}                  |xsd:string               |Specifies the type ID.   |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""


This operation does not accept a response body.




**Example List Supported Flavors For A Type: JSON response**


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
    

