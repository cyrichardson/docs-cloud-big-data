.. _get-list-available-distros-v2-:

List available distros
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/distros

This operation lists all available distros.

This table shows the possible response codes for this operation.

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
**Example List available distros: JSON response**


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
   




