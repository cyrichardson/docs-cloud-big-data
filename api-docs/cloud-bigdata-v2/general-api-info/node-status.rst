.. _node-status:

===========
Node status
===========

When you send an API request to list or get details about a node or nodes, the
following node status values might be returned:

-  ``BUILDING`` – Cloud Big Data is waiting for a nova resource to become
   available.

-  ``CONFIGURING`` – The server resource was acquired from nova and is being
   configured for cluster.

-  ``ACTIVE`` – The node is provisioned and part of a cluster.

-  ``ERROR`` – The provisioning failed for the node.

-  ``DELETING`` – A delete was requested but is not yet completed.

-  ``DELETED`` – The node has been deleted, and the nova resource has been
   freed.

-  ``DEACTIVATING`` – The node is preparing to be removed from the cluster.
