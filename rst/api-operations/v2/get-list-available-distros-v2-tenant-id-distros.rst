
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
List Available Distros -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

List Available Distros
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <get-list-available-distros-v2-tenant-id-distros.html#request>`__
`Response <get-list-available-distros-v2-tenant-id-distros.html#response>`__

.. code::

    GET /v2/{tenant_id}/distros

Lists all available distros.



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





**Example List Available Distros: JSON response**


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
    

