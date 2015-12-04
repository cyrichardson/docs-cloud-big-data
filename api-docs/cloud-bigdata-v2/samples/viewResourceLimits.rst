========================================================================================
Viewing resource limits - Rackspace Cloud Big Data Getting Started Guide, v2  - API v2.0
========================================================================================

.. rubric::  Viewing resource limits
   :name: viewing-resource-limits
   :class: title

**Contents**

`cURL example <viewResourceLimits.html#curlViewResourceLimits>`__
`Client example <viewResourceLimits.html#clientViewResourceLimits>`__

The use of the Rackspace Cloud Big Data API is subject to resource
limits. You can view the limits associated with your account by using
the operation to view the resource limits, which displays limits such as
remaining node count, available RAM, and remaining disk space for the
user.

Verb
URI
Description
**GET**
/v2/{tenant\_id}/limits
Displays the resource limits for the user.

.. rubric::  cURL example
   :name: curl-example
   :class: title

This operation does not accept a request body.

The following examples show the cURL request and corresponding response
for viewing resource limits.

 
**Example 17. cURL view resource limits request: JSON**

.. code::  

    curl -i -X GET https://dfw.bigdata.api.rackspacecloud.com/v2/yourAccountID/limits -d \
    -H "X-Auth-Token: yourAuthToken" \
    -H "Accept: application/json" \
    -H "Content-type: application/json" 

 
**Example 18. View resource limits response: JSON**

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

.. rubric::  Client example
   :name: client-example
   :class: title

Using the client, view the limits associated with your account by using
the ``limits`` command.

 
**Example 19. View resource limits**

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
