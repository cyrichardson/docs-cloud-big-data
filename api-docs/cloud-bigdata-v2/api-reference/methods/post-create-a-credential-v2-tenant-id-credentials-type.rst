.. _post-create-a-credential-v2-tenant-id-credentials-type:

Create a credential
~~~~~~~~~~~~~~~~~~~

.. code::

    POST /v2/{tenant_id}/credentials/{type}

This operation creates a new credential for the specified type.

Based on the chosen type, the request body varies. A general pattern is
followed of a dict of the ``type`` that contains one or more credential related
fields.

The ``HTTP 400`` error code might indicate any of the following issues:

*  The response body is invalid.
*  The type specified in the request body and URI do not match.
*  The credential type is invalid.


The 409 error code might indicate that there is a duplicate primary identifier
for the create request, for example, a duplicate key name or user name.

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
|409                       |Conflict                 |The requested resource   |
|                          |                         |cannot currently be      |
|                          |                         |operated on.             |
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
|{type}                    |String                   |Specify type of          |
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
|\ **ssh_keys**            |*(Required)*             |SSH key information.     |
+--------------------------+-------------------------+-------------------------+
|ssh_keys.\ **key_name**   |*(Required)*             |Name for the SSH key.    |
+--------------------------+-------------------------+-------------------------+
|ssh_keys.\ **public_key** |*(Required)*             |SSH public key.          |
+--------------------------+-------------------------+-------------------------+



**Example Create a credential - ssh_keys example: JSON request**


.. code::

   {
   	"ssh_keys": {
   		"key_name": "cbdkey",
   		"public_key": "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
   	}
   }


This table shows the body parameters for the request:

+---------------------------+-------------------------+-------------------------+
|Name                       |Type                     |Description              |
+===========================+=========================+=========================+
|**cloud-files**            |*(Required)*             |                         |
+---------------------------+-------------------------+-------------------------+
|cloud-files.\ **username** |*(Required)*             |Cloud Files account user |
|                           |                         |name.                    |
+---------------------------+-------------------------+-------------------------+
|cloud-files.\ **api_key**  |*(Required)*             |API key for Cloud Files  |
|                           |                         |                         |
+---------------------------+-------------------------+-------------------------+


**Example Create a credential - cloud_files example: JSON request**


.. code::

   {
   	"cloud_files": {
   		"username": "cfuser",
   		"api_key": "samplekey"
    	}
    }


Response
--------

**Example: Create a credential - ssh_keys example: JSON response**


.. code::

   {
   	"credentials": {
   		"ssh_keys": {
   			"key_name": "cbdkey"
   		}
   	}
   }





.. code::

   {
   	"credentials": {
   		"cloud_files": {
   			"username": "cfuser"
   		}
   	}
   }

