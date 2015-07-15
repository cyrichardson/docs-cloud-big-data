=============================================================================
List All Scripts -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List All Scripts
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_all_scripts_v2_tenant_id_scripts.rst#request>`__
`Response <GET_list_all_scripts_v2_tenant_id_scripts.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/scripts

Lists all scripts, including global, product-provided scripts and user-created scripts.



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





**Example List All Scripts: JSON request**


.. code::

    {
        "scripts": [
            {
                "created": "2014-06-14T10:10:10Z",
                "updated": "",
                "id": "1111-aaaa-bbbbb",
                "name": "iPython Notebooks",
                "type": "POST_INIT",
                "url": "https://example.com/ipynb_install.sh",
                "is_public": false,
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/scripts/1111-aaaa-bbbbb"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/scripts/1111-aaaa-bbbbb"
                    }
                ]
            },
            {
                "created": "2014-06-14T10:10:10Z",
                "updated": "",
                "id": "1111-aaaa-cccc",
                "name": "ml_libs",
                "type": "POST_INIT",
                "url": "https://example.com/mllibs.sh",
                "is_public": false,
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/scripts/1111-aaaa-cccc"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/scripts/1111-aaaa-cccc"
                    }
                ]
            },
            {
                "created": "2014-06-14T10:10:10Z",
                "updated": "",
                "id": "aaa-bbbb-33333",
                "name": "Mongo DB Connector",
                "type": "POST_INIT",
                "url": "https://example.com/mongodb_connector.sh",
                "is_public": true,
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/scripts/aaa-bbbb-33333"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/scripts/aaa-bbbb-33333"
                    }
                ]
            },
        ],
        "links": [
            {
               "rel": "next",
               "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/scripts?limit=3&amp;marker=aaa-bbbb-33333"
            }
        ]
    }

