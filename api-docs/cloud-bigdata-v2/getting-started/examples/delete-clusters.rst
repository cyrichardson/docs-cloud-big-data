.. _delete-clusters:

Deleting clusters
-----------------

You can use the delete clusters operation to remove unused Hadoop clusters.
The delete cluster operation deletes all servers associated with the cluster
and any data stored in the cluster.

You cannot delete a clusters that is in the process of being created or
resized.

Following is the operation template:

.. code::

     DELETE /v2/{tenant_id}/clusters/{id}


cURL example
~~~~~~~~~~~~

The following examples show the cURL request and corresponding response
to delete a cluster.


**Delete cluster cURL request**

.. code::

    $ curl -i -X DELETE $ENDPOINT/clusters/yourClusterID -d \
        -H "Accept: application/json" \
        -H "X-Auth-Token:$AUTH_TOKEN" \
        -H "Content-Type: application/json"

This operation does not accept a request body.

This operation does not return a response body.


Client example
~~~~~~~~~~~~~~

The following example shows the ``clusters delete`` lava client command.

**Remove clusters by using the delete lava client command**

.. code::

    $ lava clusters delete c5444b98-f4b4-aaaa-bbbb-b6e9d3313da1
