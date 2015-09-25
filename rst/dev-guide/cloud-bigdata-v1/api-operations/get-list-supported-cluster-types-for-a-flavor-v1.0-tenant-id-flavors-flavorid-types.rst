
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

.. _get-list-supported-cluster-types-for-a-flavor-v1.0-tenant-id-flavors-flavorid-types:

List supported cluster types for a flavor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/flavors/{flavorId}/types

This operation lists the supported cluster types 				for a specified flavor.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|404                       |Not Found                |The back-end services    |
|                          |                         |did not find anything    |
|                          |                         |matching the request URI.|
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
|{flavorId}                |String                   |Specifies the flavor ID. |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""










**Example List supported cluster types for a flavor: JSON response**


.. code::

   {
       "types": [
           {
               "id": "HADOOP_HDP1_3",
               "links": [
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP1_3",
                       "rel": "self"
                   },
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP1_3",
                       "rel": "bookmark"
                   }
               ],
               "name": "Hadoop (HDP 1.3)",
               "version": "1.3"
           },
           {
               "id": "HADOOP_HDP2_1",
               "links": [
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP2_1",
                       "rel": "self"
                   },
                   {
                       "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP2_1",
                       "rel": "bookmark"
                   }
               ],
               "name": "Hadoop (HDP 2.1)",
               "version": "2.1"
           }
       ]
   }




