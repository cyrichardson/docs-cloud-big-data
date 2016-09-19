.. _auth-using-client:

Authenticating by using the Lava client
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To authenticate using the lava client and get the service catalog, perform the
following steps:

#. If you haven't already done so, install the Lava client and set the
   environment variables. See :ref:`install-CLI-client<install-CLI-client>`.


1. Run the ``authenticate`` command with the parameters shown below.

   .. code::

       $ lava --user [username] --tenant [tenant_id] --api-key [api_key] --region DFW authenticate


   If the command runs successfully, your authentication token is
   displayed, as shown in the following example.


   **Example: Authentication response using CLI utility**

   .. code::

       AUTH_TOKEN=692c2a14-39ad-4ee0-991d-06cd7331f3ca


2. Export the ``AUTH_TOKEN`` and ``LAVA2_API_URL`` environment variables
   as shown in the following example. Replace ``yourTenantId`` with your actual
   tenant ID.


   **Example: Export environment variables**

   .. code::

       $ export AUTH_TOKEN=692c2a14-39ad-4ee0-991d-06cd7331f3ca
       $ export LAVA2_API_URL="https://dfw.bigdata.api.rackspacecloud.com/v2/{tenantID}"


3. To confirm that the client is running, run the distros list command.

   .. code::

       +----------+----------------------------------+---------+
       |    ID    |               Name               | Version |
       +----------+----------------------------------+---------+
       |  HDP2.3  |    HortonWorks Data Platform     |   2.3   |
       | Spark1.5 | Apache Spark (Technical Preview) |   1.5   |
       +----------+----------------------------------+---------+


