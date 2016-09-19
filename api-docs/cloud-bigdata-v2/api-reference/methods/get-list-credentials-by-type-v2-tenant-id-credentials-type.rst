.. _get-list-credentials-by-type-v2:

List credentials by type
~~~~~~~~~~~~~~~~~~~~~~~~

.. code::

    GET /v2/{tenant_id}/credentials/{type}

This operation lists all user credentials of the specified type.

This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|404                       |Not Found                |The back-end services    |
|                          |                         |did not find anything    |
|                          |                         |matching the request URI.|
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

This operation does not accept a request body.


Response
--------

**Example List credential - types example: JSON response**


.. code::

   {
       "credentials": [
           {
               "connector": true,
               "links": [
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/credentials/cloud_files",
                       "rel": "self"
                   },
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/credentials/cloud_files",
                       "rel": "bookmark"
                   }
               ],
               "schema": [
                   "username",
                   "api_key"
               ],
               "type": "cloud_files"
           },
           {
               "connector": false,
               "links": [
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/credentials/ssh_keys",
                       "rel": "self"
                   },
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/credentials/ssh_keys",
                       "rel": "bookmark"
                   }
               ],
               "schema": [
                   "key_name",
                   "public_key"
               ],
               "type": "ssh_keys"
           }
       ]
   }





.. code::

   {
       "credentials": {
           "ssh_keys": [
               {
                   "key_name": "cbdkey"
               }
           ]
       }
   }





.. code::

   {
       "credentials": {
           "cloud_files": [
               {
                   "username": "cfuser"
               }
           ]
       }
   }





