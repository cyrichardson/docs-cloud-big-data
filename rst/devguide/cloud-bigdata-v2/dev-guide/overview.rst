.. _cbd-dgv2-overview:

========
Overview
========

Rackspace Cloud Big Data is an on-demand Apache Hadoop service on the Rackspace open cloud. The service supports a RESTful API and alleviates the pain associated with deploying, managing, and scaling Hadoop clusters.

Cloud Big Data is just as flexible and feature-rich as Hadoop. With Cloud Big Data, you benefit from on-demand servers, utility-based pricing, and access to the full set of Hadoop features and APIs. However, you do not have to worry about provisioning, growing, or maintaining your Hadoop infrastructure. The Cloud Big Data service uses an environment that is specifically optimized for Hadoop, which ensures that your jobs run efficiently and reliably. Note that you are still responsible for developing, troubleshooting, and deploying your applications.

The primary use cases for Cloud Big Data are as follows:

-  Create on-demand infrastructure for applications in production where
   physical servers would be too costly and time-consuming to configure
   and maintain.

-  Develop, test, and pilot data analysis applications.

Cloud Big Data provides the following benefits:

-  Create or resize Hadoop clusters in minutes and pay only for what you
   use.

-  Access the Hortonworks Data Platform (HDP), an enterprise-ready
   distribution that is 100 percent Apache open source.

-  Provision and manage Hadoop using an easy-to-use Control Panel and a
   RESTful API.

-  Seamlessly access data in Cloud Files containers.

-  Gain interoperability with any third party software tool that
   supports HDP.

-  Fanatical Support® on a 24x7x365 basis via chat, phone or ticket.

.. _cbd-dgv2-overview-intended:

Intended audience
~~~~~~~~~~~~~~~~~

This guide is intended to assist software developers who want to develop applications by using the Cloud Big Data API. It assumes the reader has a general understanding of Big Data concepts and is familiar with the following technology:

-  Hadoop, Apache Hadoop Distributed File System (HDFS), and MapReduce

-  Hortonworks Data Platform (HDP)

-  RESTful web services

-  HTTP/1.1 conventions

-  JSON serialization formats

.. _cbd-dgv2-overview-changehistory:

Document change history
~~~~~~~~~~~~~~~~~~~~~~~

This version of the guide replaces and obsoletes all earlier versions.
The most recent changes are described in the following table:

Revision Date
Summary of Changes
April 23, 2015

-  Corrected links in `Assigning roles to account
   users`_.

April 7, 2015

-  Added script support for clusters.

-  Updated the request and response bodies for the "Create cluster"
   operation.

April 1, 2015

-  Added the “Scripts" operations.

-  Updated the response body for the "List all stacks" operation.

-  Updated the response body for the "Show stack details" operation.

-  Changed the response code to 204 for the "Delete stack" operation.

-  Updated the response body for the "List all clusters" operation.

-  Changed **POST** to **PUT** in the request and added a request and
   response body for the "Resize cluster" operation.

-  Added a response body for "List cluster nodes" operation.

-  Updated the response body for the "List available flavors" operation.

-  Removed the "Show flavor details" operation description.

-  Updated the response body for the "Show resource limits" operation.

December 18, 2014

The following changes were made:

-  Updated distro calls with more details.

-  Made changes to the cluster request and response - added
   `keypair_name` and made `stack_id` and `node_groups` top level.

-  Changed `flavor` to `flavor_id` where it is referenced in stacks
   and clusters.

-  Added links to all resources.

-  Removed node details.

June 10, 2014

Initial release of the LAVA 2 API.

.. _Assigning roles to account users: http://docs-internal.rackspace.com/cbd/api/v1.0/cbd-devguide-2/content/Assigning-Roles-d1e001.html/Assigning-Roles-d1e001.html

.. _cbd-dgv2-overview-prereqs:

Prerequisites
~~~~~~~~~~~~~

To work with the Cloud Big Data API, you must have the following prerequisites:

-  A Rackspace Cloud account

-  A Rackspace Cloud username and password, as specified during
   registration

The following OS and Hadoop distribution are supported:

-  CentOS 6.5

-  HDP version 2.1 and 1.3

By using the Cloud Big Data API, you understand and agree to the following limitations and conditions:

-  Cloud Big Data includes a Swift integration feature wherein Hadoop, MapReduce, or Apache Pig jobs can directly reference Cloud Files containers.

The following resource limits apply:

-  Up to 3 data nodes

-  Up to 6 virtual CPUs

-  Up to 23040 GB of RAM

-  Up to 4500 GB of disk space

.. _cbd-dgv2-overview-apicontract:

API contract changes
~~~~~~~~~~~~~~~~~~~~

The API contract is not locked and might change. If the contract
changes, Rackspace will notify customers in release notes.

.. _cbd-dgv2-overview-pricing:

Pricing and service level
~~~~~~~~~~~~~~~~~~~~~~~~~

Cloud Big Data is part of the Rackspace Cloud and your use through the API will be billed according to the `pricing schedule`_.

The Service Level Agreement (SLA) for Cloud Big Data is available at http://www.rackspace.com/cloud/legal/sla.

.. _pricing schedule: http://www.rackspace.com/cloud/big-data/pricing/

.. _cbd-dgv2-overview-additional:

Additional resources
~~~~~~~~~~~~~~~~~~~~

You can download the most current versions of the `API-related documents`_.

The `Rackspace Cloud site`_ offers information about Rackspace Cloud products, links to official Rackspace support channels, including knowledge base articles, forums, phone, chat, and email.

Email all support questions to cbdteam@rackspace.com.

For information about getting started using Cloud Big Data, refer to `Getting Started with Rackspace Cloud Big Data`_.

Follow Rackspace updates and announcements `on Twitter`_.

This API uses `standard HTTP 1.1 response codes`_.

.. _API-related documents: http://docs.rackspace.com/api/

.. _Rackspace Cloud site: http://www.rackspace.com/cloud/

.. _Getting Started with Rackspace Cloud Big Data: http://docs.rackspace.com/api/

.. _on Twitter: http://www.twitter.com/rackspace

.. _standard HTTP 1.1 response codes: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html
