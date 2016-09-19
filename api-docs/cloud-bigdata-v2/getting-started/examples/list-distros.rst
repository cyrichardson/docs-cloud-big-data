.. _listing-distros:

Listing distros
---------------

Use the list :ref:`Distros<distros-versions-def>` operation to review the list
of supported data platform distributions and versions along with information
about the services and components supported by each distribution.

Following is the operation template:

.. code::

     GET /v2/{tenant\_id}/distros


cURL example
~~~~~~~~~~~~

The following example shows the cURL request and corresponding response for
listing information about the data platform distributions supported by
|product name|.

**List available distros cURL request**

.. code::

    $ curl -i -X GET $ENDPOINT/distros -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json"


This operation does not require a request body.


**JSON response**

.. code::

    {
        "distros": [
            {
                "id": "HDP1.3",
                "name": "Hortonworks Data Platform",
                "version": "1.3",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/distros/HDP1.3",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/distros/HDP1.3",
                        "rel": "bookmark"
                    }
                ],
            },
            {
                "id": "HDP2.2",
                "name": "Hortonworks Data Platform",
                "version": "2.2",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/distros/HDP2.2",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/distros/HDP2.2",
                        "rel": "bookmark"
                    }
                ],
            },
            {
                "id": "CDH5",
                "name": "Cloudera Hadoop",
                "version": "5",
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/distros/CDH5",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/distros/CDH5",
                        "rel": "bookmark"
                    }
                ],
            }
        ]
    }



Client example
~~~~~~~~~~~~~~

The following example shows the ``distros list`` lava client command to list
information about the data platform distributions supported by |product name|.


**View available distros by using the lava client**

.. code::

    $ lava distros list
    +--------+---------------------------+---------+
    |   ID   |            Name           | Version |
    +--------+---------------------------+---------+
    | HDP2.2 | HortonWorks Data Platform |   2.2   |
    +--------+---------------------------+---------+
