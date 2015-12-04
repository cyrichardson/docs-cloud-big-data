.. _list-stacks:

Listing available stacks
~~~~~~~~~~~~~~~~~~~~~~~~~

Stacks are high-level software building blocks that compose a Cloud Big Data architecture. 
Stacks are comprised of services, which in turn are comprised of components. A stack is 
specific to a distribution due to differences in services that are supported across 
distributions.

You can create a stack or use one of the preconfigured stacks. 

Following is the operation template:

.. code::

     GET /v2/{tenant_id}/stacks
    
 
cURL example
^^^^^^^^^^^^^^

The following example show the cURL request and corresponding response
for listing all stacks. This operation does not accept a request body.
 
**List all stacks cURL request**

.. code::  

    $ curl -i -X GET https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/stacks -d \         
        -H "X-Auth-Token: yourAuthToken" \
        -H "Accept: application/json" \
        -H "Content-type: application/json"
    
    
**JSON response**

.. code::  

    {
        "stacks": [
            {
                "distro": "HDP2.2",
                "id": "HDP2.2_Hadoop",
                "name": "Core Hadoop",
                "description": "Core Hadoop Stack with Hive",
                "services": [
                    {
                        "modes": ["HA"],
                        "name": "HDFS"
                    },
                    {
                        "name": "Yarn"
                    },
                    {
                        "name": "MapReduce"
                    },
                    {
                        "name": "Hive"
                    },
                    {
                        "name": "Pig"
                    }
                ],
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks/HDP2.2_Hadoop",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/stacks/HDP2.2_Hadoop",
                        "rel": "bookmark"
                    }
                ],
            },
            {
                "distro": "HDP2.2",
                "id": "HDP2.2_HBase",
                "name": "HBase",
                "description": "Core Hadoop Stack with HBase",
                "services": [
                    {
                        "modes": ["HA"],
                        "name": "HDFS"
                    },
                    {
                        "name": "Yarn"
                    },
                    {
                        "name": "HBase"
                    },
                    {
                        "name": "MapReduce"
                    },
                    {
                        "name": "Hive"
                    },
                    {
                        "name": "Pig"
                    }
                ],
                "links": [
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks/HDP2.2_HBase",
                        "rel": "self"
                    },
                    {
                        "href": "https://dfw.bigdata.api.rackspacecloud.com/1234/stacks/HDP2.2_HBase",
                        "rel": "bookmark"
                    }
                ],
            }
        ],
        "links": [
            {
                "href": "https://dfw.bigdata.api.rackspacecloud.com/v2/1234/stacks?limit=2&marker=HDP2.2_HBase",
                "rel": "next"
            },
        ]
    }


Client example
^^^^^^^^^^^^^^^^^

The following example shows the ``stacks list`` lava client command to view the 
available software stack for each distribution.

 
**View available stacks by using the lava client**

.. code::  

    $ lava stacks list
    +---------------+---------------------------+--------+---------------------------------------------------+----------------------------------+
    |       ID      |            Name           | Distro |                    Description                    |             Services             |
    +---------------+---------------------------+--------+---------------------------------------------------+----------------------------------+
    | HADOOP_HDP2_2 |       Hadoop HDP 2.2      | HDP2.2 |   Core batch processing systems and interactive   | [{name=HDFS, modes=[Secondary]}, |
    |               |                           |        |                querying with Hive.                |      {name=YARN, modes=[]},      |
    |               |                           |        |                                                   |   {name=MapReduce, modes=[]},    |
    |               |                           |        |                                                   |      {name=Hive, modes=[]},      |
    |               |                           |        |                                                   |      {name=Pig, modes=[]},       |
    |               |                           |        |                                                   |     {name=Sqoop, modes=[]},      |
    |               |                           |        |                                                   |     {name=Oozie, modes=[]},      |
    |               |                           |        |                                                   |     {name=Flume, modes=[]},      |
    |               |                           |        |                                                   |   {name=Zookeeper, modes=[]}]    |
    |               |                           |        |      of a distributed message queuing system.     |     {name=Kafka, modes=[]},      |
    |               |                           |        |                                                   |   {name=Zookeeper, modes=[]}]    |
    |  SPARK_HDP2_2 |       Spark HDP 2.2       | HDP2.2 | Spark on Yarn supporting both batch and real-time | [{name=HDFS, modes=[Secondary]}, |
    |               |                           |        |                    processing.                    |      {name=YARN, modes=[]},      |
    |               |                           |        |                                                   |   {name=MapReduce, modes=[]},    |
    |               |                           |        |                                                   |      {name=Hive, modes=[]},      |
    |               |                           |        |                                                   |      {name=Pig, modes=[]},       |
    |               |                           |        |                                                   |   {name=Zookeeper, modes=[]},    |
    |               |                           |        |                                                   |     {name=Spark, modes=[]}]      |
    +---------------+---------------------------+--------+---------------------------------------------------+----------------------------------+

