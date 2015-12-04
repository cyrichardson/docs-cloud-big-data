.. _listing-scripts:

Listing scripts
~~~~~~~~~~~~~~~~~~

Use the list :ref:`Scripts<scripts-def>` operation to view the scripts
available in your Cloud Big Data environment.

Following is the operation template:

.. code::

     GET /v2/{tenant\_id}/distros
     
In the following :ref:`curl<list-script-curl-example>` and 
:ref:`client<list-script-client-example>`, the Cloud Big Data environment includes the 
following two scripts:

- The ipynb_install.sh script installs iPython notebooks on a cluster.
- The mllibs.sh script installs the MongoDB connector on a cluster.

These scripts run automatically on each server node after a cluster is set up. 

.. _list-script-curl-example:
     
cURL example
^^^^^^^^^^^^^^

The following example shows the cURL request and corresponding response
for listing all scripts. 
 
**Example: List all scripts cURL request**

.. code::  

    $ curl -i -X GET $API_ENDPOINT/scripts -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json" 
     

 
**JSON response**

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


.. _list-script-client-example:
     
Client example
^^^^^^^^^^^^^^^^^

The following example shows the ``scripts list`` lava client command. 
 
**List scripts by using the lava client**

.. code::  

    $ lava scripts list
    +--------------------------------------+--------+-----------+--------+---------------------------+------------------------------+
    |                  ID                  |  Name  |    Type   | Public |          Created          |             URL              |
    +--------------------------------------+--------+-----------+--------+---------------------------+------------------------------+
    | 44f31579-035c-4c63-9ebc-3670fc117506 | sample | POST_INIT | False  | 2015-06-30 17:03:12+00:00 | http://example.com/sample.sh |
    +--------------------------------------+--------+-----------+--------+---------------------------+------------------------------+
