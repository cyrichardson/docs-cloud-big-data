
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
Delete A Credential -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Delete A Credential
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <delete-delete-a-credential-v2-tenant-id-credentials-type-name.html#request>`__
`Response <delete-delete-a-credential-v2-tenant-id-credentials-type-name.html#response>`__

.. code::

    DELETE /v2/{tenant_id}/credentials/{type}/{name}

Deletes the specified credential.

You can delete only credentials that are not used by any active clusters.

The 409 error code might indicate an invalid 				state.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
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
|{type}                    |xsd:string               |Specify type of          |
|                          |                         |credential. Supported    |
|                          |                         |options are ``ssh_keys`` |
|                          |                         |and ``cloud_files``. The |
|                          |                         |GET calls also support   |
|                          |                         |``types`` and            |
|                          |                         |``connectors``.          |
+--------------------------+-------------------------+-------------------------+
|{name}                    |xsd:string               |Name or identifier for a |
|                          |                         |credential.              |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




