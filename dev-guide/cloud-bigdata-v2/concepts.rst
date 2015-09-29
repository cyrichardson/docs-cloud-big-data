.. _concepts:

========
Concepts
========

To use the Cloud Big Data API effectively, you should understand the following terminology:


.. _credentials-def:

Credentials
~~~~~~~~~~~~~

Credentials allow you to set up SSH keys and other connector credentials for use with clusters.


.. _distros-versions-def:

Distros
~~~~~~~

Distros provide a list of supported distributions and their corresponding versions, as well as a list of supported services and components per distribution.

.. _stacks-blocks-def: 

Stacks
~~~~~~

Stacks are high-level building blocks of software that compose a Big Data architecture. Stacks are comprised of services, which in turn are comprised of components. A stack is specific to a distribution due to the differences in services that are supported across distributions.

.. _clusters-def: 

Clusters
~~~~~~~~

Clusters are a group of servers (nodes). In Cloud Big Data, the servers are virtual.

.. _nodes-def:

Nodes
~~~~~

In a network, a node (or server) is a connection point – either a redistribution point or an end point for data transmissions. In general, a node has programmed or engineered capability to recognize and process or forward transmissions to other nodes. A node is a member of a cluster.

.. _scripts-def:

Scripts
~~~~~~~

You can create a custom script that runs during various phases of the cluster's lifecycle. The script is invoked on all nodes of the cluster. The script types currently supported are "POST_INIT", which run after the cluster is completely set up. The script must be executable. Preferably, the script should be a bash script, but it could be a python script, or a self-contained executable that works with the base OS-installed libraries.

.. _flavor-def: 

Flavor
~~~~~~

A flavor is an available configuration for Cloud Big Data. Each flavor has a unique combination of memory capacity and priority for CPU time.


..  _resource-limits-def:

Resource limits
~~~~~~~~~~~~~~~

Resource limits include items such as remaining node count, available RAM, and remaining disk space for the user.

