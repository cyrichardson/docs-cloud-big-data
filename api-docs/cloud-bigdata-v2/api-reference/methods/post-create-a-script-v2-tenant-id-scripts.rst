.. _post-create-a-script-v2-tenant-id-scripts:

Create a script
~~~~~~~~~~~~~~~

.. code::

    POST /v2/{tenant_id}/scripts

This operation creates a new script.

You can create a custom script that can be run during various phases of the
clusters lifecycle. These scripts are invoked on all nodes of the cluster. The
script type that is currently supported is ``POST_INIT``, which runs after the
cluster has been completely set up. The script must be executable. Preferably,
the script should be a bash script, but it could be a python script, or a
self-contained executable that works with the base OS installed libraries.

By default, product-provided scripts that have a ``is_public`` flag run. You do
not have the option to edit these scripts.

.. note::
   A POST_INIT script runs on all new nodes. This script runs first on all
   nodes when you create the cluster, and then runs on any subsequent resizing
   of the cluster. The script also runs when you add new nodes to the cluster.

You receive an error if a script with the specified name already exists.

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
-------

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |String                   |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+


This table shows the body parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|**script**                |*(Required)*             |Script information.      |
+--------------------------+-------------------------+-------------------------+
|script.\ **name**         |*(Required)*             |Descriptive name for the |
|                          |                         |script. For example:     |
|                          |                         |Setup iPython Notebooks  |
+--------------------------+-------------------------+-------------------------+
|script.\ **type**         |*(Required)*             |Indicates when a script  |
|                          |                         |gets run. Supported      |
|                          |                         |types are POST_INIT.     |
+--------------------------+-------------------------+-------------------------+
|script.\ **url**          |*(Required)*             |URL where the script     |
|                          |                         |resides.                 |
+--------------------------+-------------------------+-------------------------+




**Example Create a script example: JSON request**


.. code::

   {
       "script": {
           "name": "iPython Notebooks",
           "type": "POST_INIT",
           "url": "https://example.com/ipynb_install.sh"
       }
   }


Response
--------

**Example Create a script example: JSON response**


.. code::

   {
       "script": {
           "created": "2014-06-14T10:10:10Z",
           "updated": "",
           "id": "1111-aaaa-bbbbb",
           "name": "iPython Notebooks",
           "type": "POST_INIT",
           "url": "https://example.com/ipynb_install.sh",
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

