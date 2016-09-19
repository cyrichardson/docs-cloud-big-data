.. _install-CLI-client:

Install Lava client
~~~~~~~~~~~~~~~~~~~

The Lava client is a command-line tool that provides access to all public Cloud
Big Data API methods. To send requests using the client, you have to install
it.

Before installing the lava client, make sure you have the following
prerequisites.

- Linux or Mac OS X
- Python 2.7.2 or later
- Rackspace Cloud account and access to Rackspace Cloud Big Data

To install the python-lavaclient from PyPI using pip,l perform the following
steps.

#. Run the following commands on a Mac OS X or Linux distribution to install
   the lava client:

   .. code::

	   $ sudo pip install lavaclient

#. Run the help command to ensure that the client has been installed
   correctly and to review information about using the client.

   .. code::

      $ lava --help

To get started using the client, see :ref:`authenticate by using the lava
client <auth-using-client>`