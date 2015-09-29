
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-show-resource-limits-v1.0-tenant-id-limits:

Show resource limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/limits

This operation shows the absolute resource limits, 				such as remaining node count, available RAM, and 				remaining disk space, for the user.



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










**Example Show resource limits: JSON response**


.. code::

   {
      "limits":{
         "absolute":{
            "disk":{
               "limit":5120,
               "remaining":5120
            },
            "nodeCount":{
               "limit":5,
               "remaining":5
            },
            "ram":{
               "limit":40960,
               "remaining":40960
            },
            "vcpus":{
               "limit":10,
               "remaining":10
            }
         },
         "links":[
            {
               "href":"http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/limits",
               "rel":"self"
            },
            {
               "href":"http://dfw.bigdata.api.rackspacecloud.com/1234/limits",
               "rel":"bookmark"
            }
         ]
      }
   }
           




