.. _put-update-a-script-v2-tenant-id-scripts-scriptid:

Update a script
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    PUT /v2/{tenant_id}/scripts/{scriptId}

This operation updates the specified user script.

You can update only the URL and name of the script to reflect either changes to script 
or script location.

The 400 error code might indicate missing or invalid parameters.

The 409 error code might indicate an invalid state.

This table shows the possible response codes for this operation:

+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|400                       |Bad Request              |The user-provided        |
|                          |                         |request contained an     |
|                          |                         |error.                   |
+--------------------------+-------------------------+-------------------------+
|413                       |Request Entity Too Large |The resource quota was   |
|                          |                         |exceeded.                |
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
|{scriptId}                |String                   |The script ID.           |
+--------------------------+-------------------------+-------------------------+

This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|**script**                |*(Optional)*             |Script information.      |
+--------------------------+-------------------------+-------------------------+
|script.\ **name**         |*(Optional)*             |Descriptive name for the |
|                          |                         |script. For example:     |
|                          |                         |Setup iPython Notebooks  |
+--------------------------+-------------------------+-------------------------+
|script.\ **url**          |*(Required)*             |URL where the script     |
|                          |                         |resides.                 |
+--------------------------+-------------------------+-------------------------+

**Example Update a script example: JSON request**


.. code::

   {
       "script": {
           "name": "Jupyter Notebooks",
           "url": "https://test.com/jupyter_install.sh"
       }
   }
   





Response
""""""""""""""""

**Example Create a script example: JSON response**


.. code::

   {
       "script": {
           "name": "Jupyter Notebooks",
           "created": "2014-06-14T10:10:10Z",
           "updated": "2015-03-14T10:10:10Z",
           "id": "1111-aaaa-bbbbb",
           "type": "POST_INIT",
           "url": "https://test.com/jupyter_install.sh",
           "is_public": false,
           "links": [
               {
                   "rel":"self",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/v2/1234/scripts/1111-aaaa-bbbbb"
               },
               {
                  "rel":"bookmark",
                  "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/scripts/1111-aaaa-bbbbb"
               }
           ]
       }
   }
   




