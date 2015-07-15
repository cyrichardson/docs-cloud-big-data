=============================================================================
List All Clusters -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

List All Clusters
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_all_clusters_v1.0_tenant_id_clusters.rst#request>`__
`Response <GET_list_all_clusters_v1.0_tenant_id_clusters.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/clusters

Lists all clusters for your account.



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





**Example List All Clusters: JSON request**


.. code::

    {
       "clusters":[
          {
             "id":"db478fc1-2d86-4597-8010-cbe787bbbc41",
             "name":"slice",
             "created":"2012-12-27T10:10:10Z",
             "updated":"2012-12-27T10:15:10Z",
             "clusterType":"HADOOP_HDP2_1",
             "flavorId":"hadoop1-7",
             "nodeCount":5,
             "postInitScriptStatus":"SUCCEEDED",
             "progress":1.0,
             "status":"ACTIVE",
             "links":[
                {
                   "rel":"self",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41"
                },
                {
                   "rel":"bookmark",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/db478fc1-2d86-4597-8010-cbe787bbbc41"
                }
             ]
          },
          {
             "id":"ac111111-2d86-4597-8010-cbe787bbbc41",
             "name":"real",
             "created":"2012-12-27T10:10:10Z",
             "updated":"2012-12-27T10:15:10Z",
             "clusterType":"HBASE_HDP2_1",
             "flavorId":"hadoop1-60",
             "nodeCount":20,
             "postInitScriptStatus":null,
             "progress":1.0,
             "status":"ACTIVE",
             "links":[
                {
                   "rel":"self",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/clusters/ac111111-2d86-4597-8010-cbe787bbbc41"
                },
                {
                   "rel":"bookmark",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/ac111111-2d86-4597-8010-cbe787bbbc41"
                }
             ]
          }
       ]
    }

