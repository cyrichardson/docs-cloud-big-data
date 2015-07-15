=============================================================================
Show Flavor Details -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

Show Flavor Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_flavor_details_v1.0_tenant_id_flavors_flavorid_.rst#request>`__
`Response <GET_show_flavor_details_v1.0_tenant_id_flavors_flavorid_.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/flavors/{flavorId}

Shows details for a specified flavor.



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
|{flavorId}                |xsd:string               |Specifies the flavor ID. |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Flavor Details: JSON request**


.. code::

    {
       "flavor":{
          "disk":1250,
          "id":"hadoop1-7",
          "links":[
             {
                "href":"https://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/flavors/hadoop1-7",
                "rel":"self"
             },
             {
                "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/flavors/hadoop1-7",
                "rel":"bookmark"
             }
          ],
          "name":"Small Hadoop Instance",
          "ram":7680,
          "vcpus":2
       }
    }
    

