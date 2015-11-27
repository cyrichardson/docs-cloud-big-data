==================================================================================================
Creating and managing credentials - Rackspace Cloud Big Data Getting Started Guide, v2  - API v2.0
==================================================================================================

.. rubric::  Creating and managing credentials
   :name: creating-and-managing-credentials
   :class: title

**Contents**

`Creating a
credential <createManageCredentials.html#createCredential>`__
`cURL example <createManageCredentials.html#curlCreateCredential>`__
`Client example <createManageCredentials.html#clientCreateCredential>`__
`Listing all
credentials <createManageCredentials.html#listCredentials>`__
`cURL example <createManageCredentials.html#curelListCredentials>`__
`Client example <createManageCredentials.html#clientListCredentials>`__
`Updating
credentials <createManageCredentials.html#updateCredentials>`__
`cURL example <createManageCredentials.html#curlUpdateCredentials>`__
`Client
example <createManageCredentials.html#clientUpdateCredentials>`__
`Deleting
credentials <createManageCredentials.html#deleteCredentials>`__
`cURL example <createManageCredentials.html#curlDeleteCredentials>`__
`Client example <createManageCredentials.html#clientDeleteCredential>`__

Before you can create Hadoop clusters, you must create credentials.
Credentials allow you to setup SSH keys and other connector credentials
for use with clusters.

..  note:: 
Note
Your Cloud Big Data credentials are different from your cloud account.
Your credentials have the following characteristics and requirements:

-  A credential is the configuration for the administration and login
   account for the cluster.

-  You can create any number of SSH credentials and attach to a cluster.

-  Each cluster can contain only one Cloud Files credential connector.

After you create a credential, you can attach that credential to
clusters that you provision by using the API. This allows you to
remotely SSH into a server to transfer data, run or troubleshoot jobs,
and so on.

.. rubric::  Creating a credential
   :name: creating-a-credential
   :class: title

`cURL example <createManageCredentials.html#curlCreateCredential>`__
`Client example <createManageCredentials.html#clientCreateCredential>`__

Verb
URI
Description
**POST**
/v2/{tenant\_id}/credentials/{type}
Creates a credential.
This operation adds new credentials for a specific type. Based on the
chosen type, ``ssh_keys`` or ``cloud_files``, the request body varies. A
general pattern is followed of a dict of the type that contains one or
more credential related fields.

.. rubric::  cURL example
   :name: curl-example
   :class: title

The following examples show the cURL request and corresponding response
for creating a credential.

 
**Example 1. cURL create a credential - ssh\_keys request**

.. code::  

    curl -i -X POST https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/ssh_keys -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 
     

 
**Example 2. Create a credential - ssh\_keys request: JSON body**

.. code::  

    {
        "ssh_keys": {
            "key_name": "cbdkey",
            "public_key": "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
        }
    }

 
**Example 3. Create a credential - ssh\_keys response: JSON**

.. code::  

    {
        "credentials": {
            "ssh_keys": {
                "key_name": "cbdkey"
            }
        }
    }

 
**Example 4. cURL create a credential - cloud\_files request**

.. code::  

    curl -i -X POST https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/cloud_files -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 
     

 
**Example 5. Create a credential - cloud\_files request: JSON body**

.. code::  

    {
        "cloud_files": {
            "username": "cfuser",
            "api_key": "samplekey"
        }
     }

 
**Example 6. Create a credential - cloud\_files response: JSON**

.. code::  

    {
        "credentials": {
            "cloud_files": {
                "username": "cfuser"
            }
        }
    }

.. rubric::  Client example
   :name: client-example
   :class: title

Using the client, create credentials as shown in the following example.

 
**Example 7. Create a SSH credential using the CLI**

.. code::  

    $ lava credentials create_ssh_key cbdkey "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
    +------+---------+
    | Type | SSH Key |
    | Name |  cbdkey |
    +------+---------+

 
**Example 8. Create a Cloud Files credential using the CLI**

.. code::  

    $ lava credentials create_cloud_files cfuser samplekey
    +----------+-------------+
    | Type     | Cloud Files |
    | Username |      cfuser |
    +----------+-------------+

.. rubric::  Listing all credentials
   :name: listing-all-credentials
   :class: title

`cURL example <createManageCredentials.html#curelListCredentials>`__
`Client example <createManageCredentials.html#clientListCredentials>`__

Verb
URI
Description
**GET**
/v2/{tenant\_id}/credentials
Lists all user credentials.
This operation lists all user credentials.

.. rubric::  cURL example
   :name: curl-example-1
   :class: title

This operation does not accept a request body.

The following examples show the cURL request and corresponding response
for listing all user credentials.

 
**Example 9. cURL list all credentials request**

.. code::  

    curl -i -X GET https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 
     

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

.. rubric::  Client example
   :name: client-example-1
   :class: title

Using the client, list all credentials as shown in the following
example.

 
**Example 10. List all credentials using the CLI**

.. code::  

    $ lava credentials list
    +-------------+--------+
    |     Type    |  Name  |
    +-------------+--------+
    |   SSH Key   | cbdkey |
    | Cloud Files | cfuser |
    +-------------+--------+

.. rubric::  Updating credentials
   :name: updating-credentials
   :class: title

`cURL example <createManageCredentials.html#curlUpdateCredentials>`__
`Client
example <createManageCredentials.html#clientUpdateCredentials>`__

Verb
URI
Description
**PUT**
/v2/{tenant\_id}/credentials/{type}/{name}
Updates the specified user credential.
The update marks clusters that already use the credential as out of
sync.

.. rubric::  cURL example
   :name: curl-example-2
   :class: title

The following examples show the cURL request and corresponding response
for updating a credential.

 
**Example 11. cURL update a credential request**

.. code::  

    curl -i -X PUT https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/ssh_keys/cbdkey -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 
     

 
**Example 12. Update a credential request: JSON body**

.. code::  

    {
        "ssh_keys": {
            "key_name": "cbdkey",
            "public_key": "ssh-rsa AAkddddddddd3DX...5twE62lerq7Xhaff foo@bar"
        }
    }

 
**Example 13. Update a credential response: JSON**

.. code::  

    {
        "credentials": {
            "ssh_keys": {
                "key_name": "cbdkey"
            }
        }
    }

.. rubric::  Client example
   :name: client-example-2
   :class: title

Using the client, update a credential as shown in the following example.

 
**Example 14. Update a credential using the CLI**

.. code::  

    $ lava credentials update_ssh_key cbdkey "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
    +------+---------+
    | Type | SSH Key |
    | Name |  cbdkey |
    +------+---------+

.. rubric::  Deleting credentials
   :name: deleting-credentials
   :class: title

`cURL example <createManageCredentials.html#curlDeleteCredentials>`__
`Client example <createManageCredentials.html#clientDeleteCredential>`__

Verb
URI
Description
**DELETE**
/v2/{tenant\_id}/credentials/{type}/{name}
Deletes the specified user credential.
You can delete only credentials that are not used by any active
clusters.

.. rubric::  cURL example
   :name: curl-example-3
   :class: title

The following example show the cURL request for deleting a credential.

 
**Example 15. cURL delete a credential request**

.. code::  

    curl -i -X DELETE https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/ssh_keys/cbdkey -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 
     

This operation does not accept a request body.

This operation does not return a response body.

.. rubric::  Client example
   :name: client-example-3
   :class: title

Using the client, delete a credential as shown in the following example.

 
**Example 16. Delete a credential using the CLI**

.. code::  

    $ lava credentials delete_ssh_key cbdkey
                        
