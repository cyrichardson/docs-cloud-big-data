=============================================================================
Show Resource Limits -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Show Resource Limits
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_resource_limits_v2_tenant_id_limits.rst#request>`__
`Response <GET_show_resource_limits_v2_tenant_id_limits.rst#response>`__

.. code-block:: javascript

    GET /v2/{tenant_id}/limits

Shows the absolute resource limits for the user, including the remaining node count, available RAM, and remaining disk space.



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
        "limits": {
            "absolute": {
                "disk": {
                    "limit": 100000,
                    "remaining": 28882
                },
                "node_count": {
                    "limit": 100,
                    "remaining": 50
                },
                "ram": {
                    "limit": 50000,
                    "remaining": 34567
                },
                "vcpus": {
                    "limit": 50,
                    "remaining": 25
                }
            },
        }
    }
    

