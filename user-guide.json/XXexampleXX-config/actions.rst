.. _actions:

-------------------
XXexampleXX actions
-------------------
You can perform the following actions against an active, running server.

To learn how to perform XXexampleXX actions by using your choice of interface,
begin at the following sections:

* :ref:`gui`
* :ref:`cli`
* :ref:`api`

Rebuild
-------
The rebuild action rebuilds a server on the same physical host with
a selected base image or saved snapshot. The image that you select must be
within the same operating system family (Windows or Linux).
Your public and ServiceNet IP addresses are retained.
All data and disk formatting is lost.

.. TIP::
   For details and examples, click the name of the interface you want to use:

   * :kc-article:`Control Panel <managing-your-server-rebuild-a-cloud-server>`
   * :rax-dev-docs:`CLI <rack-cli/services/servers/#rebuild>`
   * :rax-api:`API <api-ref.html#rebuildServer>`

Delete
------
The delete action permanently deletes a server. Latent data is not recoverable
from the disk of a deleted server.

For details and examples, click the name of the interface you want to use.

.. TIP::
   For details and examples, click the name of the interface you want to use:

   * :kc-article:`Control Panel <managing-your-server-deleting-your-cloud-server>`
   * :rax-dev-docs:`CLI <rack-cli/services/servers/#delete>`
   * :rax-api:`API <api-ref.html#deleteServer>`
