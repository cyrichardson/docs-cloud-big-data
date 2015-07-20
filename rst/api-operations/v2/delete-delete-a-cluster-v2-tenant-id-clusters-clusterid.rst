
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
Delete A Cluster -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Delete A Cluster
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <delete-delete-a-cluster-v2-tenant-id-clusters-clusterid.html#request>`__
`Response <delete-delete-a-cluster-v2-tenant-id-clusters-clusterid.html#response>`__

.. code::

    DELETE /v2/{tenant_id}/clusters/{clusterId}

Deletes the specified cluster.

This operation deletes the cluster that is specified 				by ``clusterId``.

The 400 error code might indicate missing or invalid 				parameters.

The 409 error code might indicate an invalid 				state.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|204                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|400                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|404                       |                         |                         |
+--------------------------+-------------------------+-------------------------+
|409                       |                         |                         |
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




