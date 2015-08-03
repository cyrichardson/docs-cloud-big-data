
.. THIS OUTPUT IS GENERATED FROM THE WADL. DO NOT EDIT.

Show Distro Details
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

    GET /v2/{tenant_id}/distros/{distro_id}

For the specified distro, the operation provides a detailed list of all the supported services and their corresponding components and modes of operation.



This table shows the possible response codes for this operation:


+--------------------------+-------------------------+-------------------------+
|Response Code             |Name                     |Description              |
+==========================+=========================+=========================+
|200                       |OK                       |Success.                 |
+--------------------------+-------------------------+-------------------------+
|404                       |Not Found                |The back-end services    |
|                          |                         |did not find anything    |
|                          |                         |matching the request URI.|
+--------------------------+-------------------------+-------------------------+


Request
""""""""""""""""

This table shows the URI parameters for the request:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|{tenant_id}               |xsd:string               |The tenant ID in a multi-|
|                          |                         |tenancy cloud.           |
+--------------------------+-------------------------+-------------------------+
|{distro_id}               |xsd:string               |A specific distribution  |
|                          |                         |ID.                      |
+--------------------------+-------------------------+-------------------------+





This operation does not accept a request body.




Response
""""""""""""""""


This table shows the body parameters for the response:

+--------------------------+-------------------------+-------------------------+
|Name                      |Type                     |Description              |
+==========================+=========================+=========================+
|id                        |                         |Identifier for a         |
|                          |                         |particular distribution. |
|                          |                         |For example: HDP2.1      |
+--------------------------+-------------------------+-------------------------+
|name                      |                         |Descriptive name for a   |
|                          |                         |distribution. For        |
|                          |                         |example: Hortonworks     |
|                          |                         |Data Platform            |
+--------------------------+-------------------------+-------------------------+
|version                   |                         |Version of the           |
|                          |                         |distribution. For        |
|                          |                         |example: 2.1             |
+--------------------------+-------------------------+-------------------------+
|services                  |                         |List of services that    |
|                          |                         |are supported for a      |
|                          |                         |particular distribution. |
|                          |                         |For example: HDFS, Yarn, |
|                          |                         |and so on.               |
+--------------------------+-------------------------+-------------------------+
|name                      |                         |Name of a particular     |
|                          |                         |service. For example:    |
|                          |                         |HDFS                     |
+--------------------------+-------------------------+-------------------------+
|version                   |                         |Version of the service.  |
|                          |                         |For example: 2.4         |
+--------------------------+-------------------------+-------------------------+
|components                |                         |Subset of services that  |
|                          |                         |relate to individual     |
|                          |                         |processes. For example:  |
|                          |                         |Namenode, Datanode       |
+--------------------------+-------------------------+-------------------------+
|modes                     |                         |Certain services can     |
|                          |                         |operate in different     |
|                          |                         |modes. This details the  |
|                          |                         |list of supported modes. |
|                          |                         |For example: HA,         |
|                          |                         |Secondary Namenode,      |
|                          |                         |Federated HDFS.          |
+--------------------------+-------------------------+-------------------------+
|modes                     |                         |Short description of the |
|                          |                         |service.                 |
+--------------------------+-------------------------+-------------------------+
|name                      |                         |Component name. For      |
|                          |                         |example: Namenode        |
+--------------------------+-------------------------+-------------------------+
|mode                      |                         |Specifies that a         |
|                          |                         |particular component is  |
|                          |                         |applicable only for a    |
|                          |                         |certain mode of          |
|                          |                         |operation of the         |
|                          |                         |service. For example:    |
|                          |                         |Journal Node applies     |
|                          |                         |only for a HA Namenode.  |
+--------------------------+-------------------------+-------------------------+





**Example Show Distro Details: JSON response**


.. code::

    {
        "distro": {
            "id": "HDP2.2",
            "name": "HortonWorks Data Platform",
            "links": [
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/distros/HDP2.2",
                    "rel": "self"
                },
                {
                    "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/distros/HDP2.2",
                    "rel": "bookmark"
                }
            ],
            "services": [
                {
                    "components": [
                        {
                            "name": "Namenode"
                        },
                        {
                            "mode": "Secondary",
                            "name": "SecondaryNamenode"
                        },
                        {
                            "name": "Datanode"
                        }
                    ],
                    "description": "Hadoop Distributed File System (HDFS) is a scalable, fault-tolerant, distributed file system that provides scalable and reliable data storage designed to span large clusters of commodity servers. ",
                    "modes": [
                        {
                            "name": "Secondary"
                        }
                    ],
                    "name": "HDFS",
                    "version": "2.6",
                },
                {
                    "components": [
                        {
                            "name": "ResourceManager"
                        },
                        {
                            "name": "NodeManager"
                        },
                        {
                            "name": "TimelineHistoryServer"
                        }
                    ],
                    "description": "YARN (Yet Another Resource Negotiator) is a core component of Hadoop, managing access to all resources in a cluster. YARN brokers access to cluster compute resources on behalf of multiple applications, using selectable criteria such as fairness or capacity, allowing for a more general-purpose resource management.",
                    "name": "Yarn",
                    "version": "2.6"
                },
                {
                    "components": [
                        {
                            "name": "MRHistoryServer"
                        },
                        {
                            "name": "MRClient"
                        }
                    ],
                    "description": "Hadoop MapReduce is a software framework for easily writing applications which process vast amounts of data (multi-terabyte data-sets) in-parallel on large clusters (thousands of nodes) of commodity hardware in a reliable, fault-tolerant manner.",
                    "name": "MapReduce",
                    "version": "2.6"
                },
                {
                    "components": [
                        {
                            "name": "HiveServer2"
                        },
                        {
                            "name": "HiveMetastore"
                        },
                        {
                            "name": "HiveAPI"
                        },
                        {
                            "name": "HiveClient"
                        }
                    ],
                    "description": "Apache Hive is a data warehouse infrastructure built on top of Hadoop for providing data summarization, query, and analysis. Hive provides a mechanism to project structure onto this data and query the data using a SQL-like language called HiveQL.",
                    "name": "Hive",
                    "version": "0.14"
                },
                {
                    "components": [
                        {
                            "name": "PigClient"
                        }
                    ],
                    "description": "Apache Pig is a platform for analyzing large data sets that consists of a high-level language (Pig Latin) for expressing data analysis programs, coupled with infrastructure for evaluating these programs. Pig Latin abstracts the programming from the Java MapReduce idiom into a notation similar to that of SQL for RDBMS systems.",
                    "name": "Pig",
                    "version": "0.14"
                }
            ],
            "version": "2.2"
        }
    }
    

