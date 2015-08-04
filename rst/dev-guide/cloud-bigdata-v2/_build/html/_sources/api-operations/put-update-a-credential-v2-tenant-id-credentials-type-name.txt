
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Update A Credential
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    PUT /v2/{tenant_id}/credentials/{type}/{name}

This operation updates the specified user credential.

The update marks clusters that already use the credential as out of sync.

The 400 error code might indicate missing or invalid 				parameters.



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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ssh_keys                  |*(Required)*             |SSH key information.     |
+--------------------------+-------------------------+-------------------------+
|key_name                  |*(Required)*             |Name for the ssh key.    |
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
""""""""""""""""





**Example Update a credential example: JSON response**


.. code::

    {
    	"credentials": {
    		"ssh_keys": {
    			"key_name": "cbdkey"
    		}
    	}
    }
    


