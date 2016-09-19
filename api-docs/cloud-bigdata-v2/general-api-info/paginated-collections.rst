.. _paginated-collections:

=====================
Paginated collections
=====================

To reduce load on the service, retrieve operations return a maximum limit of
100 items at a time. If a request supplies no limit or one that exceeds the
configured  default limit, the default limit is used instead.

This behavior is called *pagination*. Pagination gives you the ability to
limit the size of the returned data and to retrieve a specified subset of a
large data set.  Pagination has two key concepts: limit and marker.

* *Limit* is the restriction on the maximum number of items for that type that
  can be returned.

* *Marker* is a reference to an object's ID and is in the list of paged
  results for a particular resource. For example, if the resource is a load
  balancer, the marker is the load balancer ID at which to begin the list of
  the paged results.

To navigate the collection, you can set the ``limit`` and ``marker``
parameters in the URI. For example, ``?limit=10&marker=1234`` displays a
maximum of 10 load balancers in the paginated results, beginning with the
load balancer whose ID is 1234.

You can also use the ``offset`` parameter, which is a count of the number
of objects from where the paginated list is started.

If a marker beyond the end of a list is given, an empty list is returned.

Pagination applies only to the operations listed in the following table:

.. list-table::
   :widths: 10 30 30
   :header-rows: 1

   * - Method
     - URI
     - Description
   * - **GET**
     - /v2/{tenant_id}/clusters
     - Lists all clusters for your account.
   * - **GET**
     - /v2/{tenant_id}/clusters/{clusterId}/nodes
     - Lists all nodes for the specified cluster.
   * - **GET**
     - /v2/{tenant_id}/flavors
     - Lists all available flavors, including the drive size and the amount of
       RAM.

The default paging limit for all calls is 25 calls with a maximum of 200 items.
Requests for more than 200 items result in a ``400`` error.

See the following example of the operation to list paged nodes.

.. _cbd-dgv2-pagination-request:

**Example: List nodes paged request: JSON**

.. code::

    GET /v2/yourAccountID/clusters/ac111111-2d86-4597-8010-cbe787bbbc41/nodes?limit=2
    X-Auth-Token: yourAuthToken
    Accept: application/json
    Content-Type: application/json

Notice that the preceding paged request example sets the limit to 2
(``?limit=2``), so the example response that follows shows 2 nodes.

.. _cbd-dgv2-pagination-response:

**Example: List nodes paged response: JSON**

.. code::

    {
        "nodes": [
                  {
                  "id": "000",
                  "created": "2014-08-11T10:10:10Z",
                  "role": "NAMENODE",
                  "name": "NAMENODE-1",
                  "status": "ACTIVE",
                  "addresses": {
                  "public": [
                             {
                             "addr": "168.x.x.3",
                             "version": 4
                             }
                             ],
                  "private": [
                              {
                              "addr": "10.x.x.3",
                              "version": 4
                              }
                              ]
                  },
                  "services": [
                               {
                               "name": "namenode"
                               },
                               {
                               "name": "jobtracker"
                               },
                               {
                               "name": "ssh",
                               "uri": "ssh://user@168.x.x.3"
                               }
                               ],
                  "links": [
                            {
                            "rel": "self",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
                            },
                            {
                            "rel": "bookmark",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/000"
                            }
                            ]
                  },
                  {
                  "id": "aaa",
                  "role": "GATEWAY",
                  "name": "GATEWAY-1",
                  "status": "ACTIVE",
                  "addresses": {
                  "public": [
                             {
                             "addr": "168.x.x.4",
                             "version": 4
                             }
                             ],
                  "private": [
                              {
                              "addr": "10.x.x.4",
                              "version": 4
                              }
                              ]
                  },
                  "services": [
                               {
                               "name": "pig"
                               },
                               {
                               "name": "hive"
                               },
                               {
                               "name": "ssh",
                               "uri": "ssh://user@168.x.x.4"
                               },
                               {
                               "name": "status",
                               "uri": "http://10.x.x.4"
                               },
                               {
                               "name": "hdfs-scp",
                               "uri": "scp://user@168.x.x.4:9022"
                               }
                               ],
                  "links": [
                            {
                            "rel": "self",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
                            },
                            {
                            "rel": "bookmark",
                            "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41/nodes/aaa"
                    }
                ]
            }
        ]
    }

