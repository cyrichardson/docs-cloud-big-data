.. _listing-hardware-configuration-flavors:

Listing flavors
---------------

A flavor is an available hardware configuration for a cluster. Each flavor has
a unique combination of memory capacity and priority for CPU time. As the
flavor size increases, a cluster has more RAM and higher priority for CPU time.

Before you create a cluster, use the list flavors operation to view the
available configurations and determine which one to use for building your
cluster.

Following is the operation template:

.. code::

     GET /v2/{tenant\_id}/flavors


cURL example
~~~~~~~~~~~~

The following example shows the cURL request and corresponding response
for listing

**List flavors cURL request**

.. code::

    $ curl -i -X GET $ENDPOINT/flavors -d \
        -H "X-Auth-Token: $AUTH_TOKEN" \
        -H "Accept: application/json" \
        -H "Content-type: application/json"


This operation does not require a request body.


**JSON response body**

.. code::

    {
        "flavors": [
            {
                "disk": 10000,
                "id": "hadoop1-60",
                "name": "XLarge Hadoop Instance",
                "ram": 61440,
                "vcpus": 16,
                "class": "hadoop1"
            },
            {
                "disk": 1250,
                "id": "hadoop1-7",
                "name": "Small Hadoop Instance",
                "ram": 8192,
                "vcpus": 2,
                "class": "hadoop1"
            },
            {
                "disk": 3200,
                "id": "onmetal-io1",
                "name": "OnMetal IO 1",
                "ram": 122880,
                "vcpus": 40,
                "class": "onmetal"
            }
        ],
        "links": [
            {
                "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/flavors?limit=2&amp;marker=hadoop1-7",
                "rel": "next"
            }
        ]
    }


Client example
~~~~~~~~~~~~~~

The following example shows the ``flavors list`` lava client command to list
the hardware configuration flavors available for building a cluster.

**List available hardware configuration flavors by using the lava client**

.. code::

    $ lava flavors list
    +------------+------------------------+-------+-------+-------+
    |     ID     |          Name          |   RAM | VCPUs |  Disk |
    +------------+------------------------+-------+-------+-------+
    | hadoop1-15 | Medium Hadoop Instance | 15360 |     4 |  2500 |
    | hadoop1-30 | Large Hadoop Instance  | 30720 |     8 |  5000 |
    | hadoop1-60 | XLarge Hadoop Instance | 61440 |    16 | 10000 |
    | hadoop1-7  | Small Hadoop Instance  |  7680 |     2 |  1250 |
    +------------+------------------------+-------+-------+-------+
