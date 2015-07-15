=============================================================================
List Credentials By Type -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List Credentials By Type
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_credentials_by_type_v2_tenant_id_credentials_type_.rst#request>`__
`Response <GET_list_credentials_by_type_v2_tenant_id_credentials_type_.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/credentials/{type}

Lists all user credentials of the specified type.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |List credential - types  |                         |
|                          |example: JSON response   |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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








Response
^^^^^^^^^^^^^^^^^^





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
    

