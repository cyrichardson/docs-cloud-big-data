.. _get-list-all-clusters-v2:

List all clusters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/clusters

This operation lists all clusters for your account.


This table shows the possible response codes for this operation:

+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+


Request
""""""""""""""""

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+

This operation does not accept a request body.

Response
""""""""""""""""

**Example List all clusters: JSON response**


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
   




