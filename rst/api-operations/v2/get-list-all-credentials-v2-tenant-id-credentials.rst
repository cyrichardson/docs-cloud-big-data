
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
List All Credentials -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List All Credentials
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <get-list-all-credentials-v2-tenant-id-credentials.html#request>`__
`Response <get-list-all-credentials-v2-tenant-id-credentials.html#response>`__

.. code::

    GET /v2/{tenant_id}/credentials

Lists all user credentials.



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





**Example List All Credentials: JSON response**


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
    

