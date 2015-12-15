.. _create-manage-clusters:

Creating and managing Hadoop clusters 
---------------------------------------

You can use the |apiservice| to create and manage Hadoop clusters. 
The examples and information in the following sections show how 
to complete the following API operations by using the cURL and the lava client.

- View hardware configurations available for building a cluster.
- Get information about the data platform distributions and versions supported by 
  |product name|
- Review the services and components included in the software stacks supported by 
  |product name|
- Create, resize, and delete clusters
- Get information about all server nodes in a cluster
- Add scripts that run automatically against all servers after cluster set up is completed

.. note:: 
     These examples use the ``$ENDPOINT`` and ``$AUTH_TOKEN`` environment 
     variables to specify the API endpoint and authentication values for accessing the 
     service. Make sure you :ref:`configure these variables<configure-environment-variables>` 
     before running the code samples. 

.. include:: examples/list-flavors.rst
.. include:: examples/list-distros.rst
.. include:: examples/list-stacks.rst
.. include:: examples/create-cluster.rst
.. include:: examples/list-clusters.rst
.. include:: examples/view-node-details.rst
.. include:: examples/resize-clusters.rst
.. include:: examples/create-scripts.rst
.. include:: examples/list-scripts.rst
.. include:: examples/delete-clusters.rst
