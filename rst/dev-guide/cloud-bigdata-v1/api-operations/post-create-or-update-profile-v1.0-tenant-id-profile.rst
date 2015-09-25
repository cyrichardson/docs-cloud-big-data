
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _post-create-or-update-profile-v1.0-tenant-id-profile:

Create or update profile
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    POST /v1.0/{tenant_id}/profile

This operation creates a profile or updates the 				information in an existing profile.

Cloud Big Data provisions each server in the cluster 				with the ``username`` and ``password`` that are part of the 				profile. You can ssh into the nodes with those 				credentials. These credentials are required in the 				request (as shown in the example "Create or update 				profile request:JSON").

The ``cloudCredentials.username`` and ``cloudCredentials.apikey`` are stored in 				the cluster configuration so that Hadoop can read or 				write objects stored in Cloud Files. These credentials 				are optional. If they are not supplied, the cluster 				does not have access to Cloud Files, but otherwise 				operates normally.

.. note::
   You must create your profile before you create 					a cluster.
   
   

The 400 error code might indicate malformed data or 				unacceptable parameters.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|400                       |Bad Request              |The user-provided        |
|                          |                         |request contained an     |
|                          |                         |error.                   |
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




**Example Create or update profile: JSON request**


.. code::

   {
      "profile":{
         "username":"john.doe",
         "password":"j0Hnd03",
         "sshkeys":[
            {
               "name":"t@test",
               "publicKey":"ssh-rsa ....."
            }
         ],
         "cloudCredentials":{
            "username":"jdoe",
            "apikey":"df23gkh34h52gkdgfakgf"
         }
      }
   }





Response
""""""""""""""""










**Example Create or update profile: JSON response**


.. code::

   {
      "profile":{
         "username":"john.doe",
         "userId":"12346",
         "tenantId":"123456",
         "sshkeys":[
            {
               "name":"t@test",
               "publicKey":"ssh-rsa ....."
            }
         ],
         "cloudCredentials":{
            "username":"jdoe"
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




