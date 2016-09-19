.. _get-list-all-credentials-v2:

List all credentials
~~~~~~~~~~~~~~~~~~~~

.. code::

    GET /v2/{tenant_id}/credentials

This operations lists all user credentials.



This table shows the possible response codes for this operation:

+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+


Request
-------

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.

Response
--------

**Example List all credentials: JSON response**


.. code::

   {
       "credentials": {
           "cloud_files": [
               {
                   "username": "cfuser"
               }
           ],
           "ssh_keys": [
               {
                   "key_name": "cbdkey"
               }
           ]
       }
   }





