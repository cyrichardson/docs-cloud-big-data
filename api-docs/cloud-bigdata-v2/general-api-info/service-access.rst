.. _service-access:

========================
Service access endpoints
========================


The |apiservice| is a regionalized service. The user of the service is
therefore responsible for selecting the appropriate regional endpoint to ensure
access to servers, networks, or other Cloud services.

.. tip:: To help you decide which regionalized endpoint to use, read about
   :how-to:`special considerations<about-regions>` for choosing a data center.

The following table lists the |product name| endpoints that are available
for each region.


.. _api-info-service-access-regional:

.. list-table:: **Regionalized service endpoints**
    :widths: 10 40
    :header-rows: 1

    * - Region
      - Endpoint
    * - Chicago (ORD)
      - ``https://ord.bigdata.api.rackspacecloud.com/v2/$TENANT_ID/``
    * - Dallas/Ft. Worth (DFW)
      - ``https://dfw.bigdata.api.rackspacecloud.com/v2/$TENANT_ID/``
    * - Northern Virginia (IAD)
      - ``https://iad.bigdata.api.rackspacecloud.com/v2/$TENANT_ID/``
    * - London (LON)
      - ``https://lon.bigdata.api.rackspacecloud.com/v2/$TENANT_ID/``

Replace the ``$TENANT_ID`` with your actual account number that is returned as
part of the authentication response. The account number is located  after the
final slash (/) in the ``publicURL`` field.

.. note::

   You should copy the base URLs directly from the catalog rather than trying
   to construct them manually. You can find the complete URI to access the
   Cloud Servers API that includes your account number in the service catalog
   returned in the :ref:`authentication response <review-auth-resp>`. Search
   the catalog for the service name, ``cloudServersOpenStack``. Then copy the
   URI from the *publicURL* field included in the service information.

   Rackspace Cloud Identity returns a service catalog, which includes regional
   endpoints with your account ID. Your account ID, also known as project ID or
   tenant ID, refers to your Rackspace account number.
