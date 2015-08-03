
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Show Cluster Type Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v1.0/{tenant_id}/types/{typeId}

Shows details for a specified 				cluster type.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |                         |                         |
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
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{typeId}                  |xsd:string               |Specifies the type ID.   |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""


This operation does not accept a response body.




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
            

