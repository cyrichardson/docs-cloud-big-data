.. _cbd-dgv2-faults:

======
Faults
======

When an error occurs, the Cloud Big Data service returns a fault object that contains an HTTP error response code that denotes the type of error. In the body of the response, the system will return additional information about the fault.

The following table lists possible fault types with their associated error codes and descriptions.

+--------------------+------------+-----------------------------------------+
|     Fault type     | Associated | Description                             |
|                    | error code |                                         |
+====================+============+=========================================+
| badRequest         | 400        | The user-provided request contained an  |
|                    |            | error.                                  |
+--------------------+------------+-----------------------------------------+
| unauthorized       | 401        | The supplied token is not authorized to |
|                    |            | access the resources. The token is      |
|                    |            | either expired or invalid.              |
+--------------------+------------+-----------------------------------------+
| forbidden          | 403        | Access to the requested resource was    |
|                    |            | denied.                                 |
+--------------------+------------+-----------------------------------------+
| itemNotFound       | 404        | The back-end services did not find      |
|                    |            | anything matching the request URI.      |
+--------------------+------------+-----------------------------------------+
| conflictingRequest | 409        | The requested resource cannot currently |
|                    |            | be operated on.                         |
+--------------------+------------+-----------------------------------------+
| overLimit          | 413        | The resource quota was exceeded.        |
+--------------------+------------+-----------------------------------------+
| lavaFault          | 500        | An unknown exception occurred.          |
+--------------------+------------+-----------------------------------------+
| serviceUnavailable | 503        | he service is currently unavailable.    |
+--------------------+------------+-----------------------------------------+
