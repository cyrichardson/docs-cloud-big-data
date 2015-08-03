# wadl2rst

Automates the process of taking the WADL API information and outputting it as rST.

## Installation

    pip install -e git+git@github.rackspace.com:Product-DevOps/wadl2rst.git@master#egg=wadl2rst

## Command Line Usage

    usage: wadl2rst [-h] [--version] [config_file]

    Given a config file, generate rST based on the WADLs contained therein. If
    there is no config_file given, it will look for a file named
    'wadl2html.config.yaml' in the current working directory.

    positional arguments:
     config_file  configuration file containing information to run

    optional arguments:
     -h, --help   show this help message and exit
     --version    print the version of the application and exit

## Config file Format

File format:

    wadl_path:
        title: {book_title}
        [output_directory: {directory to place files}]

- *wadl_path*: Path to the wadl file to process, can be relative or absolute
- *book_title*: Book title as shown on the title of the rST pages
- *output_directory* (optional): used to override the default output directory

File format example:

    samples/cloud-load-balancers/wadl/rax-cloudLoadBalancers-api-v1.wadl:
        title: Rackspace Cloud Load Balancers Developer Guide - API v1.0

    samples/cloud-servers/wadl/12934-extensions.wadl:
        title: Rackspace Cloud Servers Developer Guide - API v2.0
        output_directory: rst/dev-guide/api-operations/cloud-servers

    samples/cloud-servers/wadl/3217-supporting.wadl:
        title: Rackspace Cloud Servers Developer Guide - API v2.0
        output_directory: rst/dev-guide/api-operations/cloud-servers
