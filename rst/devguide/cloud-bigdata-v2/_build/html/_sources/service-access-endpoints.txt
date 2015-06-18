.. _cbd-dgv2-service:

========================
Service access endpoints
========================

The Cloud Big Data service is a regionalized service. The user of the service is therefore responsible for appropriate replication, caching, and overall maintenance of Cloud Big Data data across regional boundaries to other Cloud Servers.

The endpoints to use for your Cloud Big Data API calls are summarized in the following table.

To help you decide which regionalized endpoint to use, read `About regions`_ about special considerations for choosing a data center.

**Regionalized service endpoints**

+-------------------------+---------------------------------------------------------------------+
|         Region          |                                Endpoint                             |
+=========================+=====================================================================+
| Chicago (ORD)           | ``https://ord.bigdata.api.rackspacecloud.com/v2/yourAccountID/``    |
+-------------------------+---------------------------------------------------------------------+
| Dallas/Ft. Worth (DFW)  | ``https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/``    |
+-------------------------+---------------------------------------------------------------------+
| Northern Virginia (IAD) | ``https://iad.bigdata.api.rackspacecloud.com/v2/yourAccountID/``    |
+-------------------------+---------------------------------------------------------------------+
| London (LON)            | ``https://lon.bigdata.api.rackspacecloud.com/v2/yourAccountID/``    |
+-------------------------+---------------------------------------------------------------------+

Replace the ``yourAccountID`` placeholder with your actual account number, which is returned as part of the authentication service response, after the final **/** in the ``publicURL`` field.

.. _About regions: http://www.rackspace.com/knowledge_center/article/about-regions