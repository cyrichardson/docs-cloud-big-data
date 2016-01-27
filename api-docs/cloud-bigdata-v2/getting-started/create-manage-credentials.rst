.. _create-manage-credentials:

Create and manage credentials
-----------------------------------

Before you can create Hadoop clusters, you need to add credentials to 
specify SSH keys and other connector credentials to use with Cloud Big Data clusters. 

..  note:: 
    Your Cloud Big Data credentials are different from your cloud account.
    Your credentials have the following characteristics and requirements:

    -  A credential is the configuration for the administration and login account for 
       the cluster. 

    -  You can add any number of SSH credentials and attach them to a cluster.
    
    -  Each cluster can contain only one Cloud Files credential connector.

After you create a credential, you attach it to clusters that you provision by using 
the API. Then, you can use the credentials to SSH into a remote server to transfer data, 
run or troubleshoot jobs, and so on.


Creating a credential
~~~~~~~~~~~~~~~~~~~~~~~~

The create credential operation adds a credential by type, for example ``ssh_keys``, 
``cloud_files``, or ``s3``. You need to supply the credential values for each credential 
that you create.

Cloud Big Data supports credentials to connect to the following Cloud storage systems: 
Rackspace Cloud Files, AWS s3, and Apache Ambari. 

Following is the operation template:

.. code::

     POST {endpoint}/credentials/{type}
     

The request body varies based on the credential type. The general pattern is to specify a 
request body that contains a dictionary of (*type*,*name*) pairs. 

cURL example
^^^^^^^^^^^^^^^^

The following examples show the cURL request and corresponding response
for creating a credential.

 
**Create an SSH credential cURL request**

.. code::  

    $ curl -i -X POST $ENDPOINT/credentials/ssh_keys -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 


**JSON request body**

.. code::
     
   {
      "ssh_keys": {
         "key_name": "cbdkey",
         "public_key": "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
      }
    }
 
**JSON response body**

.. code:: 
   
   {
      "credentials": {
        "ssh_keys": {
          "key_name": "cbdkey"
        }
      }
    }

**Create a Cloud Files credential cURL request**

.. code::  

    $ curl -i -X POST $ENDPOINT/credentials/cloud_files  -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 
     

**JSON request body**

.. code:: 
   
   {
      "credentials": {
       "cloud_files": {
         "username": "cfuser",
         "api_key": "samplekey"
        }
      }
    }

**JSON response body**

.. code::  
    
   {
      "credentials": {
       "cloud_files": {
         "username": "cfuser"
        }
      }
   }
    

**Create an AWS s3 credential cURL request**

.. code::  
    
    $ curl -i -X POST $ENDPOINT/credentials/s3 -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 
    

**JSON request body**

.. code:: 
   
    {
      "s3": {
        "access_key_id": "<s3-access-key-id>",
        "access_secret_key": "<s3-access-key>"
      }
    }
    
    
**JSON response body**

.. code::  
   
    {
      "credentials": {
        "s3": {
        "access_key_id": "123456"
        }
      }
    }
    

**Create an Ambari credential cURL request**
 
.. code::  
    
    $ curl -i -X POST $ENDPOINT/credentials/ambari -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json"
    
    
**JSON request body**

.. code:: 
    
    {
       "ambari": {
         "username": "ambariuser",
         "password": "testPassword"
       }
    }  
     
    
**JSON response**

.. code::  
  
    {
      "credentials": {
        "ambari": {
          "username": "ambariuser"
        }
      }
    }


Client example
^^^^^^^^^^^^^^^

The following example shows how to create a credential by using the lava client. 

**Create an SSH credential by using the lava client**

.. code::  

    $ lava credentials create_ssh_key cbdkey "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
    +------+---------+
    | Type | SSH Key |
    | Name |  cbdkey |
    +------+---------+

 
**Create a Cloud Files credential by using the lava client**

.. code::  

    $ lava credentials create_cloud_files cfuser samplekey
    +----------+-------------+
    | Type     | Cloud Files |
    | Username |      cfuser |
    +----------+-------------+
    

Listing credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can list all or specified credentials for the current user by submitting a list 
credentials operation. 

Following is the operation template:

.. code::

     GET {endpoint}/{tenant_id}/credentials/{type}

To see all credentials, omit the ``type`` parameter when you submit the request. 

cURL examples
^^^^^^^^^^^^^^^^^

The following examples show the cURL request and corresponding response
to get all credentials that have been added to Cloud Big Data.
 
**List all credentials cURL request**

.. code::  

    $ curl -i -X GET $ENDPOINT/credentials \
        -H "X-Auth-Token: yourAuthToken" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 
    
     
**JSON response**

Note that the response returns empty sets for credentials types that you have not 
configured. 

.. code::  

    {
       "credentials": {
         "s3": [],
         "ambari": [],
         "cloud_files": [],
         "ssh_keys": [
           {
             "key_name": "cbdkey"
           },
           {
             "key_name": "cbdkey2"
           }
         ]
       }
    }
       

Client example
^^^^^^^^^^^^^^^

The following example shows how to create a credential by using the lava client. 

**Create an SSH credential client request**

Using the client, list all credentials as shown in the following
example.

 
**List all credentials using the lava client**

.. code::  

    $ lava credentials list
    +------------+--------+
    |     Type   |  Name  |
    +------------+--------+
    | SSH Key    | cbdkey |
    | SSH Key    | cbdkey2|
    | Cloud Files| cfuser |
    +------------+--------+



Updating credentials
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Updates the specified user credential. When the update operation runs, clusters 
that use the credential are marked as out of sync.

Following is the operation template:

.. code::

     PUT $ENDPOINT/credentials/{type}/{name} 
     
    
cURL example
^^^^^^^^^^^^^^^^^

The following examples show the cURL request and corresponding response
for updating a credential.

 
**Update a credential cURL request**

.. code::  

    $ curl -i -X PUT https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/ssh_keys/cbdkey \
       -d \
       -H "X-Auth-Token: yourAuthToken" \
       -H "Accept: application/json" \
       -H "Content-type: application/json" 
     

**JSON request body**

.. code::  

    {
        "ssh_keys": {
            "key_name": "cbdkey",
            "public_key": "ssh-rsa AAkddddddddd3DX...5twE62lerq7Xhaff foo@bar"
        }
    }

 
**JSON response**

.. code::  

    {
        "credentials": {
            "ssh_keys": {
                "key_name": "cbdkey"
            }
        }
    }


Client example
^^^^^^^^^^^^^^^^^^^^^

The following example shows how to update a credential by using the lava client. 

**Update a credential by using the lava client**

.. code::  

    $ lava credentials update_ssh_key cbdkey "ssh-rsa AAkphQZaDNi2Ij3DX...5twE62lerq7Xhaff foo@bar"
    +------+---------+
    | Type | SSH Key |
    | Name |  cbdkey |
    +------+---------+


Deleting credentials
~~~~~~~~~~~~~~~~~~~~~~~

Use the delete credentials operation to remove a specified user credential. When the 
update operation runs, any clusters that use the credential are marked as out of sync.
You can delete only credentials that are not used by any active clusters.

Following is the operation template:

.. code::

     DELETE $ENDPOINT/credentials/{type}/{name} 
     

cURL example
^^^^^^^^^^^^^^^

The following example shows a cURL request for deleting an SSH credential.

 
**Delete a credential cURL request**

.. code::  

    $ curl -i -X DELETE https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/credentials/ssh_keys/cbdkey -d \
        -H "X-Auth-Token: yourAuthToken" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 
     

This operation does not accept a request body or return a response body.


Client example
^^^^^^^^^^^^^^^

The following example shows a client request for deleting an SSH credential by using the 
client.

 
**Delete an ssh key credential by using the CLI**

.. code::  

    $ lava credentials delete_ssh_key cbdkey
                        
