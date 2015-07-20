
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

=============================================================================
Show Cluster Type Details -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

Show Cluster Type Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <get-show-cluster-type-details-v1.0-tenant-id-types-typeid.html#request>`__
`Response <get-show-cluster-type-details-v1.0-tenant-id-types-typeid.html#response>`__

.. code::

    GET /v1.0/{tenant_id}/types/{typeId}

Shows details for a specified 				cluster type.



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
|{typeId}                  |xsd:string               |Specifies the type ID.   |
+--------------------------+-------------------------+-------------------------+








Response
^^^^^^^^^^^^^^^^^^





**Example Show Cluster Type Details: JSON response**


.. code::

    {
       "type":{
          "id":"HADOOP_HDP2_1",
          "links":[
             {
                "href":"http://dfw.bigdata.api.rackspacecloud.com/v1.0/1234/types/HADOOP_HDP2_1",
                "rel":"self"
             },
             {
                "href":"http://dfw.bigdata.api.rackspacecloud.com/1234/types/HADOOP_HDP2_1",
                "rel":"bookmark"
             }
          ],
          "name":"Hadoop (HDP 2.1)",
          "services":[
    
          ]
       }
    }
            

