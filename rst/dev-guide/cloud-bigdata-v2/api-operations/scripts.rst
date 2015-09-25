.. _scripts:

Scripts 
~~~~~~~~~~~~

You can create a custom script that runs during various phases of the cluster's lifecycle. 
The script is invoked on all nodes of the cluster. The script types currently supported are 
"POST_INIT", which run after the cluster is completely set up. The script must be 
executable. Preferably, the script should be a bash script, but it could be a python 
script, or a self-contained executable that works with the base OS-installed libraries.

Use the Scripts API operations to create, update, and delete a script, and to list all global, 
product-provided, and user-created scripts.

.. include:: methods/delete-delete-a-script-v2-tenant-id-scripts-scriptid.rst
.. include:: methods/get-list-all-scripts-v2-tenant-id-scripts.rst
.. include:: methods/post-create-a-script-v2-tenant-id-scripts.rst
.. include:: methods/put-update-a-script-v2-tenant-id-scripts-scriptid.rst
