=============================================================================
Update A Credential -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Update A Credential
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <PUT_update_a_credential_v2_tenant_id_credentials_type_name_.rst#request>`__
`Response <PUT_update_a_credential_v2_tenant_id_credentials_type_name_.rst#response>`__

.. code-block:: javascript

    PUT /v2/{tenant_id}/credentials/{type}/{name}

Updates the specified user credential.

The update marks clusters that already use the credential as out of sync.

The 400 error code might indicate missing or invalid parameters.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Update a credential      |                         |
|                          |example: JSON response   |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+


Request
^^^^^^^^^^^^^^^^^

This table shows the URI parameters for the request:

+-------------------+------------------+---------------------------------------+
|Name               |Type              |Description                            |
+===================+==================+=======================================+
|{tenant_id}        |xsd:string        |The tenant ID in a multi-tenancy cloud.|
+-------------------+------------------+---------------------------------------+
|{type}             |xsd:string        |Specify type of credential. Supported  |
|                   |                  |options                                |
|                   |                  |are``ssh_keys``and``cloud_files``.The  |
|                   |                  |GET calls also                         |
|                   |                  |support``types``and``connectors``.     |
+-------------------+------------------+---------------------------------------+
|{name}             |xsd:string        |Name or identifier for a credential.   |
+-------------------+------------------+---------------------------------------+





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ssh_keys                  |*(Required)*             |Name for the ssh key.    |
+--------------------------+-------------------------+-------------------------+
|public_key                |*(Required)*             |SSH public key.          |
+--------------------------+-------------------------+-------------------------+





**Example Update a credential example: JSON request**


.. code::

    {
    	"ssh_keys": {
    		"key_name": "cbdkey",
    		"public_key": "ssh-rsa AAkddddddddd3DX...5twE62lerq7Xhaff foo@bar"
    	}
    }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Update a credential example: JSON response**


.. code::

    {
    	"credentials": {
    		"ssh_keys": {
    			"key_name": "cbdkey"
    		}
    	}
    }
    

