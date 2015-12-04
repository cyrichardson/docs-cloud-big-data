
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-view-profile-information-v1.0-tenant-id-profile:

View profile information
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/profile

This operation returns profile details for the 				current user.



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










**Example View profile information: JSON response**


.. code::

   {
      "profile":{
         "username":"john.doe",
         "user_id":"12346",
         "tenant_id":"123456",
         "sshkeys":[
            {
               "name":"t@test"
            }
         ],
         "cloudCredentials":{
   
         },
         "links":[
            {
               "rel":"self",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/123456/profile"
            },
            {
               "rel":"bookmark",
               "href":"https://dfw.bigdata.api.rackspacecloud.com/123456/profile"
            }
         ]
      }
   }
   




