.. _get-show-resource-limits-v2:

Show resource limits
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/limits

This operation shows the absolute resource limits for the user, including the 
remaining node count, available RAM, and remaining disk space.

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
       "limits": {
           "absolute": {
               "disk": {
                   "limit": 100000,
                   "remaining": 28882
               },
               "node_count": {
                   "limit": 100,
                   "remaining": 50
               },
               "ram": {
                   "limit": 50000,
                   "remaining": 34567
               },
               "vcpus": {
                   "limit": 50,
                   "remaining": 25
               }
           },
       }
   }
   




