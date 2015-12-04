
Viewing resource limits
---------------------------

Your use of the Rackspace Cloud Big Data API is subject to resource
limits. You can view the limits associated with a user account by 
using the get limits operation. The response returns a list of limits that includes 
information such as remaining node count, available RAM, and remaining disk space.

Following is the operation template:

.. code::

     GET $API_ENDPOINT/limits
     
     
cURL example
^^^^^^^^^^^^^^^
     
The following examples show the cURL request and corresponding response
for viewing resource limits.

 
**View resource limits cURL request**

.. code::  

    curl -i -X GET $API_ENDPOINT/limits -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 

 
**JSON response**

.. code::  

    {
        "limits": {
            "absolute": {
                "disk": {
                    "limit": 100000,
                    "remaining": 28882
                },
                "node_count": {
                    "limit": 100,
                    "remaining": 50
                },
                "ram": {
                    "limit": 50000,
                    "remaining": 34567
                },
                "vcpus": {
                    "limit": 50,
                    "remaining": 25
                }
            },
        }
    }

Client example
^^^^^^^^^^^^^^^^^^

The following example shows how to view resource limits by using the lava client.

 
**View resource limits by using the lava client**

.. code::  

    $ lava limits get
    +-------------------------------+
    |             Quotas            |
    +----------+--------+-----------+
    | Property |  Limit | Remaining |
    +----------+--------+-----------+
    |  Nodes   |     20 |        18 |
    |   RAM    | 614400 |    599040 |
    |   Disk   | 115000 |    112500 |
    |  VCPUs   |    160 |       156 |
    +----------+--------+-----------+
