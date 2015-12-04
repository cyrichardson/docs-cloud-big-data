.. _create-scripts:

Creating scripts
~~~~~~~~~~~~~~~~~~

You can create a custom script and add it to the Cloud Big Data environment. Scripts can 
be run during various phases of a cluster's lifecycle. When it is invoked, the script 
runs on all nodes in a cluster. Cloud Big Data only supports scripts with a ``POST_INIT`` 
type. These scripts run after cluster setup is complete. 
  
The script must be executable. You can create bash scripts, python scripts, or 
a self-contained executable that works with the base OS-installed libraries. The

.. note::
     Cloud Big Data has a few default, product-provided scripts that have an ``is_public`` 
     flag. You do not have the option to edit them.

Following is the operation template:

.. code::

    POST /v2/{tenant_id}/scripts 	
    
.. _create-script-curl-example:
    
cURL example
^^^^^^^^^^^^^^

The following examples show the cURL request, request body, and corresponding response
to add a script that installs iPython Notebooks on a cluster. 
 
**Create a script cURL request**

.. code::  

    $curl -i -X POST $API_ENDPOINT/script -d \
       -H "X-Auth-Token: $AUTH_TOKEN" \
       -H "Accept: application/json" \
       -H "Content-type: application/json" 
     

 
**JSON request body**

.. code::  

    {
        "script": {
            "name": "iPython Notebooks",
            "type": "POST_INIT",
            "url": "https://example.com/ipynb_install.sh"
        }
    }

 
**JSON response**

.. code::  

    {
        "script": {
            "created": "2014-06-14T10:10:10Z",
            "updated": "",
            "id": "1111-aaaa-bbbbb",
            "name": "iPython Notebooks",
            "type": "POST_INIT",
            "url": "https://example.com/ipynb_install.sh",
            "is_public": false,
            "links": [
                {
                    "rel":"self",
                    "href":"https://dfw.bigdata.api.rackspacecloud.com/v2/1234/scripts/1111-aaaa-bbbbb"
                },
                {
                   "rel":"bookmark",
                   "href":"https://dfw.bigdata.api.rackspacecloud.com/1234/scripts/1111-aaaa-bbbbb"
                }
            ]
        }
    }

    
.. _create-script-client-example:
    
Client example
^^^^^^^^^^^^^^^^^

The following example shows the ``scripts create`` lava client command to create 
a script to run on a cluster.
 
**Create a script by using the lava client**

.. code::  

    $ lava scripts create sample http://example.com/sample.sh post_init
    +---------+--------------------------------------+
    | ID      | 44f31579-035c-4c63-9ebc-3670fc117506 |
    | Name    |                               sample |
    | Type    |                            POST_INIT |
    | Public  |                                False |
    | Created |            2015-06-30 17:03:12+00:00 |
    | URL     |         http://example.com/sample.sh |
    +---------+--------------------------------------+


    +------------------------------------------------------------+
    |                        Node Groups                         |
    +-----------+-----------+-------+----------------------------+
    |     ID    |   Flavor  | Count |         Components         |
    +-----------+-----------+-------+----------------------------+
    |   master  | hadoop1-4 |     1 |     [{name=Namenode}]      |
    | secondary | hadoop1-4 |     1 | [{name=SecondaryNamenode}] |
    |   slave   | hadoop1-7 |     4 |     [{name=Datanode},      |
    |           |           |       |    {name=KafkaBroker},     |
    |           |           |       |  {name=ZookeeperClient}]   |
    | zookeeper | hadoop1-2 |     3 |  [{name=ZookeeperServer},  |
    |           |           |       |  {name=ZookeeperClient}]   |
    +-----------+-----------+-------+----------------------------+
