=============================================================================
List Cluster Nodes -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List Cluster Nodes
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_list_cluster_nodes_v2_tenant_id_clusters_clusterid_nodes.rst#request>`__
`Response <GET_list_cluster_nodes_v2_tenant_id_clusters_clusterid_nodes.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/clusters/{clusterId}/nodes

Lists all nodes for the specified cluster.

Valid values for the request body parameter ``postInitScriptStatus`` are ``FAILED``, ``PENDING``, ``DELIVERED``, ``RUNNING``, ``SUCCEEDED``, and ``None``.

Valid values for the node status are in `"Node status" <http://docs-internal-staging.rackspace.com/cbd/api/v1.0/cbd-devguide-2/content/node_status.html>`__.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
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
|{clusterId}               |xsd:string               |The cluster ID.          |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example List Cluster Nodes: JSON request**


.. code::

    {
        "nodes": [
            {
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-444",
                "name": "master-1",
                "node_group": "master",
                "status": "ACTIVE",
                "updated": "",
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
                "flavor_id": "hadoop1-4",
                "components": [
                    {
                        "name": "Namenode",
                        "nice_name": "HDFS Namenode",
                        "uri": "http://master-1.local:50070"
                    },
                    {
                        "name": "ResourceManager",
                        "nice_name": "YARN Resource Manager",
                        "uri": "http://master-1.local:8088"
                    },
                    {
                        "name": "YarnTimelineServer",
                        "nice_name": "YARN Timeline History Server",
                        "uri": "http://master-1.local:8188"
                    },
                    {
                        "name": "JobHistoryServer",
                        "nice_name": "MapReduce History Server",
                        "uri": "http://master-1.local:19888"
                    }
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-444"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-444"
                    }
                ]
    		},
    		{
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-333",
                "name": "slave-1",
                "node_group": "slave",
                "status": "ACTIVE",
                "updated": "",
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
                "flavor_id": "hadoop1-7",
                "components": [
                    {
                        "name": "Datanode",
                        "nice_name": "HDFS Datanode",
                        "uri": "http://slave-1.local:50075"
                    },
                    {
                        "name": "NodeManager",
                        "nice_name": "YARN Node Manager",
                        "uri": "http://slave-1.local:8042"
                    },
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-333"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-333"
                    }
                ]
    		},
    		{
                "created": "2014-06-14T10:10:10Z",
                "id": "111-222-555",
                "name": "slave-2",
                "node_group": "slave",
                "status": "ACTIVE",
                "updated": "",
                "addresses": {
    				"public": [
    					{
    						"addr": "168.x.x.5",
    						"version": 4
    					}
    				],
    				"private": [
    					{
    						"addr": "10.x.x.5",
    						"version": 4
    					}
    				]
                },
                "flavor_id": "hadoop1-7",
                "components": [
                    {
                        "name": "Datanode",
                        "nice_name": "HDFS Datanode",
                        "uri": "http://slave-2.local:50075"
                    },
                    {
                        "name": "NodeManager",
                        "nice_name": "YARN Node Manager",
                        "uri": "http://slave-2.local:8042"
                    },
                ],
                "links": [
                    {
                        "rel": "self",
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes/111-222-555"
                    },
                    {
                       "rel": "bookmark",
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/clusters/aaa-bbbb-cccc/nodes/111-222-555"
                    }
                ]
    		}
        ],
        "links":[
            {
                "rel":"next",
                "href":"https://dfw.bigdata.api.rackspacecloud.com/v2/1234/clusters/aaa-bbbb-cccc/nodes?limit=3&marker=111-222-555"
            }
        ]
    }
    

