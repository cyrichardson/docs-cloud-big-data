=============================================================================
Show Cluster Details -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

Show Cluster Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cluster_details_v1.0_tenant_id_clusters_clusterid_.rst#request>`__
`Response <GET_show_cluster_details_v1.0_tenant_id_clusters_clusterid_.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/clusters/{clusterId}

Shows details for a specified cluster.



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
|{clusterId}               |xsd:string               |Specifies the cluster ID.|
+--------------------------+-------------------------+-------------------------+








**Example Show Cluster Details: JSON request**


.. code::

    GET https://dfw.bigdata.api.rackspacecloud.com/v1.0/7654321/clusters/ac111111-2d86-4597-8010-cbe787bbbc41
    Accept: application/json 
    X-Auth-Token:ea85e6ac-baff-4a6c-bf43-848020ea3812
    Content-Type: application/json  


Response
^^^^^^^^^^^^^^^^^^





**Example Show Cluster Details: JSON request**


.. code::

    Status: 200 OK
    Date: Mon, 06 Aug 2012 21:54:21 GMT
    Content-Type: application/json
    Content-Length: 110

