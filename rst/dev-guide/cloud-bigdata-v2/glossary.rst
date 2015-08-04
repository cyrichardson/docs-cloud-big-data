.. _cbd-dgv2-glossary:

========
Glossary
========

Cluster
    A cluster consists of a group of servers running a distributed system coordinating and functioning as one. A cluster consists of a single stack. Examples are a Hadoop cluster or a HBase cluster.

Component
    A service can have one or more components. A component can be a specific configuration for a service or additional modes of operation. Examples are HDFS Secondary Namenode or HDFS HA.
    
Credentials
    Credentials allow you to setup ssh keys and other connector credentials for use with clusters.

Distro
    Distros provide a list of supported distributions and their corresponding versions, as well as a list of supported services and components per distribution.

Flavor
    A flavor is an available configuration for Cloud Big Data. Each flavor has a unique combination of memory capacity and priority for CPU time.
    
HDFS
    The Apache Hadoop Distributed File System. This is the default file system used in Cloud Big Data.

MapReduce
    A framework for performing calculations on the data in the distributed file system. Map tasks run in parallel with each other. Reduce tasks also run in parallel with each other.

Node
    A node is a single instance within a cluster running one or more services. In a network, a node (or server) is a connection point, either a redistribution point or an end point for data transmissions. In general, a node has programmed or engineered capability to recognize and process or forward transmissions to other nodes. A node is a member of a cluster.

Resource limits
    Resource limits include items such as remaining node count, available RAM, and remaining disk space for the user.

SCP server proxy
    An SCP service that runs on your Hadoop cluster and distributes your files across the cluster.
    
Scripts
    You can create a custom script that runs during various phases of the cluster's lifecycle. The script is invoked on all nodes of the cluster. The script types currently supported are "POST_INIT", which run after the cluster is completely set up. The script must be executable. Preferably, the script should be a bash script, but it could be a python script, or a self-contained executable that works with the base OS-installed libraries.

Service
    A service is any individual software component that can function on its own or depend on other services to provide added functionality. Examples are HDFS, Pig, and Hive.

Service catalog
    Your service catalog is the list of services available to you, as returned along with your authentication token and an expiration date for that token. All the services in your service catalog should recognize your token as valid until it expires.

    The catalog listing for each service provides at least one endpoint URL for that service. Other information, such as regions and versions and tenants, is provided if it is relevant to your access to this service.

Stack
    Stacks are high-level building blocks of software that compose a Big Data architecture. Stacks are comprised of services, which in turn are comprised of components. A stack is specific to a distribution due to the differences in services that are supported across distributions.

Tenant
    A container used to group or isolate resources or identity objects. Depending on the service operator, a tenant could map to a customer, account, organization, or project.
