.. _list-clusters:

Listing clusters
----------------

Use the list clusters operation to view the clusters available in your account.


Following is the operation template:

.. code::

     GET /v2/{tenant\_id}/clusters


cURL example
~~~~~~~~~~~~

The following examples show the cURL request and the corresponding response for
listing clusters.


**Example: List clusters cURL request**

.. code::

    curl -i -X GET $ENDPOINT/clusters -d \
    -H "X-Auth-Token: $AUTH_TOKEN" \
    -H "Accept: application/json" \
    -H "Content-type: application/json"


**JSON response**

.. code::

    {
        "clusters": [
            {
                "created": "2014-06-14T10:10:10Z",
                "id": "aaa-bbbb-cccc",
                "name": "test",
                "status": "ACTIVE",
                "stack_id": "HDP2.1_Hadoop",
                "updated": "",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc",
                        "rel": "bookmark"
                    }
                ],
            }
        ],
        "links": [
            {
                "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters&limit=1&marker=aaa-bbbb-cccc",
                "rel": "next"
            }
        ]
    }


Client example
~~~~~~~~~~~~~~

Using the client, list clusters using the ``clusters list`` command as shown in
the following example.


**Example: List clusters lava client command**

.. code::

    $ lava clusters list
    +--------------------------------------+-------------+--------+--------------+---------------------------+
    |                  ID                  |     Name    | Status |    Stack     |          Created          |
    +--------------------------------------+-------------+--------+--------------+---------------------------+
    | c5444b98-f4b4-aaaa-bbbb-b6e9d3313da1 |     test    | ACTIVE | KAFKA_HDP2_2 | 2015-06-30 06:10:37+00:00 |
    +--------------------------------------+-------------+--------+--------------+---------------------------+
