=============================================================================
Show Cluster Type Details -  Rackspace Cloud Big Data Developer Guide v1
=============================================================================

Show Cluster Type Details
~~~~~~~~~~~~~~~~~~~~~~~~~

`Request <GET_show_cluster_type_details_v1.0_tenant_id_types_typeid_.rst#request>`__
`Response <GET_show_cluster_type_details_v1.0_tenant_id_types_typeid_.rst#response>`__

.. code-block:: javascript

    GET /v1.0/{tenant_id}/types/{typeId}

Shows details for a specified cluster type.



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





**Example Show Cluster Type Details: JSON request**


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
            

