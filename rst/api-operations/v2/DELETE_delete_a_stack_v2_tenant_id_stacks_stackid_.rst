=============================================================================
Delete A Stack -  Rackspace Cloud Big Data Developer Guide v2
=============================================================================

Delete A Stack
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <DELETE_delete_a_stack_v2_tenant_id_stacks_stackid_.rst#request>`__
`Response <DELETE_delete_a_stack_v2_tenant_id_stacks_stackid_.rst#response>`__

.. code-block:: javascript

    DELETE /v2/{tenant_id}/stacks/{stackId}

Deletes the specified stack.

This functionality is not yet implemented.

You can delete only user-created stacks. Global stacks are read-only, and you cannot delete them.

The 400 error code might indicate missing or invalid parameters.

The 409 error code might indicate an invalid state.



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
|{stackId}                 |xsd:string               |The stack ID.            |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^




