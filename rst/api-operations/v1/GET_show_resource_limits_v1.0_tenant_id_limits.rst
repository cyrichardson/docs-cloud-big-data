=============================================================================
Show Resource Limits -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

Show Resource Limits
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_resource_limits_v1.0_tenant_id_limits.rst#request>`__
`Response <GET_show_resource_limits_v1.0_tenant_id_limits.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/limits

Shows the absolute resource limits, such as remaining node count, available RAM, and remaining disk space, for the user.



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





**Example Show Resource Limits: JSON request**


.. code::

    {
       "limits":{
          "absolute":{
             "disk":{
                "limit":5120,
                "remaining":5120
             },
             "nodeCount":{
                "limit":5,
                "remaining":5
             },
             "ram":{
                "limit":40960,
                "remaining":40960
             },
             "vcpus":{
                "limit":10,
                "remaining":10
             }
          },
          "links":[
             {
                "href":"http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/limits",
                "rel":"self"
             },
             {
                "href":"http://dfw.bigdata.api.rackspacecloud.com/1234/limits",
                "rel":"bookmark"
             }
          ]
       }
    }
            

