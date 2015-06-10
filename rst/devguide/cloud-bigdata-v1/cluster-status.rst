.. cbd-dgv2-clusterstatus:

==============
Cluster status
==============

When you send an API request to create, list, or delete a cluster or clusters, the following cluster status values might be returned:

-  BUILDING – The cluster is being provisioned.

-  CONFIGURING – The cluster is being configured.

-  ACTIVE – The cluster is online and available to for use.

-  UPDATING – The cluster is being updated, either through a resize operation or another update operation.

-  ERROR – The cluster failed to start up.

-  DELETING – The cluster is being deleted.

-  DELETED – The cluster is deleted.

The following figure shows the cluster states and the operations that are valid for each one.

**Cluster states with valid operations**

.. image:: /_images/cluster-states.png
