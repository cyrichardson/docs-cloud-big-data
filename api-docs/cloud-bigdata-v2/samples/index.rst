==============================================================
Rackspace Cloud Big Data Getting Started Guide, v2  - API v2.0
==============================================================

API v2.0

©
2015
Rackspace US, Inc.

This guide is intended for software developers interested in developing
applications using the Rackspace Cloud Big Data Application Programming
Interface (API). The document is for informational purposes only and is
provided “AS IS.”

RACKSPACE MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND, EXPRESS OR
IMPLIED, AS TO THE ACCURACY OR COMPLETENESS OF THE CONTENTS OF THIS
DOCUMENT AND RESERVES THE RIGHT TO MAKE CHANGES TO SPECIFICATIONS AND
PRODUCT/SERVICES DESCRIPTION AT ANY TIME WITHOUT NOTICE. RACKSPACE
SERVICES OFFERINGS ARE SUBJECT TO CHANGE WITHOUT NOTICE. USERS MUST TAKE
FULL RESPONSIBILITY FOR APPLICATION OF ANY SERVICES MENTIONED HEREIN.
EXCEPT AS SET FORTH IN RACKSPACE GENERAL TERMS AND CONDITIONS AND/OR
CLOUD TERMS OF SERVICE, RACKSPACE ASSUMES NO LIABILITY WHATSOEVER, AND
DISCLAIMS ANY EXPRESS OR IMPLIED WARRANTY, RELATING TO ITS SERVICES
INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTY OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT.

Except as expressly provided in any written license agreement from
Rackspace, the furnishing of this document does not give you any license
to patents, trademarks, copyrights, or other intellectual property.

Rackspace®, Rackspace logo and Fanatical Support® are registered service
marks of Rackspace US, Inc. All other product names and trademarks used
in this document are for identification purposes only and are property
of their respective owners.

2015-06-30

--------------

**List of Examples**

1. `cURL create a credential - ssh\_keys
request <createManageCredentials.html#d6e53>`__
2. `Create a credential - ssh\_keys request: JSON
body <createManageCredentials.html#d6e58>`__
3. `Create a credential - ssh\_keys response:
JSON <createManageCredentials.html#d6e61>`__
4. `cURL create a credential - cloud\_files
request <createManageCredentials.html#d6e64>`__
5. `Create a credential - cloud\_files request: JSON
body <createManageCredentials.html#d6e69>`__
6. `Create a credential - cloud\_files response:
JSON <createManageCredentials.html#d6e72>`__
7. `Create a SSH credential using the
CLI <createManageCredentials.html#d6e78>`__
8. `Create a Cloud Files credential using the
CLI <createManageCredentials.html#d6e81>`__
9. `cURL list all credentials
request <createManageCredentials.html#d6e103>`__
10. `List all credentials using the
CLI <createManageCredentials.html#d6e112>`__
11. `cURL update a credential
request <createManageCredentials.html#d6e133>`__
12. `Update a credential request: JSON
body <createManageCredentials.html#d6e138>`__
13. `Update a credential response:
JSON <createManageCredentials.html#d6e141>`__
14. `Update a credential using the
CLI <createManageCredentials.html#d6e147>`__
15. `cURL delete a credential
request <createManageCredentials.html#d6e168>`__
16. `Delete a credential using the
CLI <createManageCredentials.html#d6e178>`__
17. `cURL view resource limits request:
JSON <viewResourceLimits.html#d6e200>`__
18. `View resource limits response:
JSON <viewResourceLimits.html#d6e205>`__
19. `View resource limits <viewResourceLimits.html#d6e212>`__
20. `cURL list flavors request:
JSON <CBD_createManageClusters.html#d6e239>`__
21. `List flavors response:
JSON <CBD_createManageClusters.html#d6e244>`__
22. `List flavors and associated resources by using the flavors list
command with the CLI <CBD_createManageClusters.html#d6e251>`__
23. `cURL list available distros request:
JSON <CBD_createManageClusters.html#d6e274>`__
24. `List available distros response:
JSON <CBD_createManageClusters.html#d6e279>`__
25. `View available distros with the
CLI <CBD_createManageClusters.html#d6e286>`__
26. `cURL list all stacks request:
JSON <CBD_createManageClusters.html#d6e308>`__
27. `List all stacks response:
JSON <CBD_createManageClusters.html#d6e313>`__
28. `View available stacks with the
CLI <CBD_createManageClusters.html#d6e320>`__
29. `cURL create cluster
request <CBD_createManageClusters.html#d6e341>`__
30. `Create cluster request: JSON
body <CBD_createManageClusters.html#d6e346>`__
31. `Create cluster response:
JSON <CBD_createManageClusters.html#d6e349>`__
32. `Create a cluster with the
CLI <CBD_createManageClusters.html#d6e356>`__
33. `cURL list clusters request:
JSON <CBD_createManageClusters.html#d6e378>`__
34. `List clusters response:
JSON <CBD_createManageClusters.html#d6e383>`__
35. `List clusters with the
CLI <CBD_createManageClusters.html#d6e390>`__
36. `cURL list cluster nodes request:
JSON <CBD_createManageClusters.html#d6e412>`__
37. `List cluster nodes response:
JSON <CBD_createManageClusters.html#d6e417>`__
38. `Query the details of a cluster by using the show and nodes commands
with the CLI <CBD_createManageClusters.html#d6e425>`__
39. `cURL resize cluster request:
JSON <CBD_createManageClusters.html#d6e463>`__
40. `Resize cluster request: JSON
body <CBD_createManageClusters.html#d6e469>`__
41. `Resize cluster response:
JSON <CBD_createManageClusters.html#d6e472>`__
42. `Increase cluster size by using the resize command with the
CLI <CBD_createManageClusters.html#d6e480>`__
43. `cURL create a script <CBD_createManageClusters.html#d6e510>`__
44. `Create a script request: JSON
body <CBD_createManageClusters.html#d6e515>`__
45. `Create a script response:
JSON <CBD_createManageClusters.html#d6e518>`__
46. `Create a script with the
CLI <CBD_createManageClusters.html#d6e524>`__
47. `cURL list all scripts
request <CBD_createManageClusters.html#d6e546>`__
48. `List all scripts response:
JSON <CBD_createManageClusters.html#d6e551>`__
49. `List available scripts with the
CLI <CBD_createManageClusters.html#d6e557>`__
50. `cURL delete cluster request:
JSON <CBD_createManageClusters.html#d6e579>`__
51. `Remove clusters by using the delete
command <CBD_createManageClusters.html#d6e591>`__
