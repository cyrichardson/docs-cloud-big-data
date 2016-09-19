.. _credentials:

======================
Credentials operations
======================

Use the Credentials API operations to add SSH keys and other connector
credentials to connect your |service| clusters to your cloud data storage
backend.

You must add an SSH key for each cluster.

|product name| currently supports the following credential types:

- Rackspace Cloud files ``username`` and ``apiKey``
- Amazon s3, ``access_key_id`` and ``access_secret_key``
- Apache Ambari, ``username`` and ``password``


.. include:: methods/get-list-all-credentials-v2-tenant-id-credentials.rst
.. include:: methods/get-list-credentials-by-type-v2-tenant-id-credentials-type.rst
.. include:: methods/post-create-a-credential-v2-tenant-id-credentials-type.rst
.. include:: methods/put-update-a-credential-v2-tenant-id-credentials-type-name.rst
.. include:: methods/delete-delete-a-credential-v2-tenant-id-credentials-type-name.rst