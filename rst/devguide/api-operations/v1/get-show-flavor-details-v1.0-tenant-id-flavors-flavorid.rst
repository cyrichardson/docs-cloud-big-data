
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Show Flavor Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/flavors/{flavorId}

Shows details for a specified 				flavor.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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
|{flavorId}                |xsd:string               |Specifies the flavor ID. |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""


This operation does not accept a response body.




**Example Show Flavor Details: JSON response**


.. code::

    {
       "flavor":{
          "disk":1250,
          "id":"hadoop1-7",
          "links":[
             {
                "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-7",
                "rel":"self"
             },
             {
                "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-7",
                "rel":"bookmark"
             }
          ],
          "name":"Small Hadoop Instance",
          "ram":7680,
          "vcpus":2
       }
    }
    

