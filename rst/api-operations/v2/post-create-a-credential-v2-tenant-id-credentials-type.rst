
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
Create A Credential -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Create A Credential
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <post-create-a-credential-v2-tenant-id-credentials-type.html#request>`__
`Response <post-create-a-credential-v2-tenant-id-credentials-type.html#response>`__

.. code::

    POST /v2/{tenant_id}/credentials/{type}

Creates a new credential for the specified type.

This operation adds new credentials for a specific type. Based on the chosen type, the 					request body varies. A general pattern is followed of a dict of the ``type`` that 					contains one or more credential related fields.

The 400 error code might indicate any of the 				following issues:



*  The response body is invalid.
*  The type specified in the request body and URI do not match.
*  The credential type is invalid.


The 409 error code might indicate that there is a duplicate primary identifier for the create request, for example, a duplicate key name or user name.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |Create a credential -    |                         |
|                          |ssh_keys example: JSON   |                         |
|                          |response                 |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
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





This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|ssh_keys                  |*(Required)*             |Name for the ssh key.    |
+--------------------------+-------------------------+-------------------------+
|public_key                |*(Required)*             |SSH public key.          |
+--------------------------+-------------------------+-------------------------+





**Example Create a credential - ssh_keys example: JSON request**


.. code::

    {
    	"ssh_keys": {
    		"key_name": "cbdkey",
    		"public_key": "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
    	}
    }
    


**Example Create a credential - cloud_files example: JSON request**


.. code::

    {
    	"cloud_files": {
    		"username": "cfuser",
    		"api_key": "samplekey"
     	}
     }
    


Response
^^^^^^^^^^^^^^^^^^





**Example Create a credential - ssh_keys example: JSON response**


.. code::

    {
    	"credentials": {
    		"ssh_keys": {
    			"key_name": "cbdkey"
    		}
    	}
    }
    

