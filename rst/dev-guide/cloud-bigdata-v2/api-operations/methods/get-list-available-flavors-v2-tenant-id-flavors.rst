.. _get-list-available-flavors-v2-tenant-id-flavors:

List available flavors
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/flavors

This operation lists all available flavors, including the drive size and amount of RAM.



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
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.

Response
""""""""""""""""

**Example List available flavors: JSON response**


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
   




