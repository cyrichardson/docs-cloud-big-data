# Userguide template for *single product*

This user-guide directory provides the source for a single-product user guide model.

Contents  *generated with [DocToc](http://doctoc.herokuapp.com/)*

  - [Overview](#overview)
  - [Alternatives](#alternatives)
  - [Customizing your guide](#customizing-your-guide)
    - [Parts that are your content](#parts-that-are-your-content)
    - [Parts that assemble your content](#parts-that-assemble-your-content)
  - [Building from source](#building-from-source)
    - [Prerequisites](#prerequisites)
    - [Publishing your guide](#publishing-your-guide)

##Overview

Here's a summary of the steps to create a publishable deliverable from this model:

- Copy the entire /user-guide-single-product/ directory
  to wherever you want to work with it
- Install Sphinx and its prereqs to confirm that you can [build from source](#building-from-source)
- Customize your content
- Run `make html`` to confirm that your customizations build
- Merge your customized content into the master branch of your GitHub repository,
- Contact the DevDoc team to request help reviewing and publishing your content


##Alternatives

If this template is not a good match for the user guide you intend to create,
examine the other 
[Rackspace documentation templates](https://github.com/rackerlabs//docs-templates/)

##Customizing your guide

Copy all the parts from this folder to your own GitHub repo,
then customize them to present your own content as noted here.

### Parts that are your content

**index.rst**

This is the starting point for a guide to
one product.
``index.rst`` shapes the guide
to help readers notice
important features of the product and learn to use them.

- Replace all occurrences of ``XXexampleXX``
  with something identifying this
  product.
  If you can, name the product consistently with the name for it that
  readers encounter elsewhere in their experiences at Rackspace,
  especially in control panels.

- Create pages or sections
  introducing the guide itself,
  introducing the product covered in the guide,
  introducing the use of product interfaces,
  introducing configuration options,
  introducing pre-production hardening steps,
  and introducing guidelines for normal operation (`` toctree::``).

  Make these consistent with the navigation structure you describe
  in ``_toc.rst``.

**contactus.rst**

- Customize a contact-us page (/XXexampleXX-guide-intro/contactus.rst)
  with instructions for readers
  who have suggestions or questions (``:ref:``).  

**bestpractice.rst**

- Customize a best-practices page (/XXexampleXX-ops/bestpractice.rst)
  with advice about choosing wisely among available options.
  If you publish that advice elsewhere, such as in a blog, link to that here.

**keepup.rst**

- Customize a keeping-up page (/XXexampleXX-ops/keepup.rst)
  with advice about maintaining awareness of change.
  If you provide release notes, a news feed, a blog,
  or some other means of notifying
  users of changes and new ideas, link to that here.

**limits.rst**

- Customize a limits page (/XXexampleXX-ops/limits.rst)
  with details about rate limits, absolute limits, spending limits,
  or any other usage rules that can cause otherwise-valid operations to fail.
  If you provide a method for users to query or change their limits,
  explain or link to that here.

**somethingnew.rst**

- Customize a something-new page (/XXexampleXX-ops/somethingnew.rst)
  with details about how first-time use differs from ongoing operation.

**support.rst**

- Customize a support page (/XXexampleXX-ops/support.rst)
  with instructions about how to get help from Rackspace.
  If support can involve fees or is limited to specific hours or is controlled by
  a Service Level Agreement (SLA) or is only available to customers who have
  signed up for it, explain that here.

**troubleshoot.rst**

- Customize a troubleshooting page (/XXexampleXX-ops/troubleshoot.rst)
  with instructions about how to investigate and resolve problems.

**/_images/**

- Store images here that you want to include anywhere
  in the guide.

  For example, if you have a drawing in ``/_images/cloudimagesharing.png``,
  you can include it anywhere in the guide with
  ``.. figure:: /_images/cloudimagesharing.png``.

  You can see this demonstrated at ``index.rst``.
  Remove the demonstration if you do not wish to include it in
  the published guide.

- If an image requires a source document for maintenance,
  include that source document in ``/_images/``.

  For example, cloudimagesharing.png was created at www.draw.io;
  you can change it there by opening cloudimagesharing.xml.

**/_common/**

- Store text fragments here that you want to include anywhere
  in the guide.

  For example, if you have a warning in ``/_common/warning-draft.txt``,
  you can include it anywhere in the guide with
  ``.. include:: /_common/warning-draft.txt``.

  You can see this demonstrated at ``index.rst``.
  Remove the demonstration if you do not wish to include it in
  the published guide.

**everywhere**

- Look for occurrences of ``XXexampleXX`` and replace those with
  filenames and content appropriate for this guide.

- Replace general-purpose sample content,
  borrowed from other user guides, with content
  directly relevant to this guide.

  For example, replace the problem-solving guidance in troubleshoot.rst
  with specific suggestions for solving problems with *this* product.

### Parts that assemble your content

**conf.py**

- Update ``project = 'Rackspace XXexampleXX User Guide'`` to name this project.

- Update the ``extlinks`` list to provide full URLs and abbreviated references for
  sites outside this guide that you link to repeatedly.

  Even if you change nothing else in ``extlinks``,
  change the definition of ``'git-repo'``
  to point to the doc source repository for this guide.

- Update ``html_short_title = 'XXexampleXX Guide'`` to name this guide.

- Update ``htmlhelp_basename = 'XXexampleXXGuidedoc'`` to name this document.

- Update ``latex_documents = [
  (master_doc, 'RackspaceXXexampleXXGuide.tex',
  u'Rackspace XXexampleXX Guide Documentation',
  u'Rackspace', 'manual'),]`` to create a LaTex document tree structure.

- Update ``man_pages = [
    (master_doc, 'rackspaceXXexampleXXuserguide', u'Rackspace XXexampleXX Guide Documentation',
    [author], 1)]`` to create a manual page structure.

**_toc.rst**

- Update ``XXexampleXX User Guide <self>`` to show the guide's title for the
  top of the left-hand navigation bar.

- Update the remainder of ``toc.rst`` to list sections in the order they should
  appear in the left-hand navigation bar.

**_deconst.json**

- Update ``"contentIDBase": "https://github.com/rackerlabs/XXexampleXX/"``
  to identify the GitHub repository containing this guide's doc source.

**.travis.yml**

- This file has credentials for production and staging servers,
  and for notifications in Slack.
  I don't know how to generate them.


## Building from source

These instructions are for local builds using the Sphinx template specified in the 
conf.py file. If you want to build locally using the Rackspace 
documentation templates, use the [Deconst client](https://github.com/deconst/client).

### Prerequisites

- Python 2.7 or later
- Mac OSx: Install [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) or [pyenv](https://github.com/yyuu/pyenv)
- Windows: Install Python, pip, and virtualenv (See [How to install Python, pip, and virtualenv with PowerShell](http://www.tylerbutler.com/2012/05/how-to-install-python-pip-and-virtualenv-on-windows-with-powershell/)).

To set up your build environment:

1. Run the following commands to Activate your virtual environment:

   ```
    bin activate env-name
     
   ```   

2. Run the following commands to install Sphinx and other required packages:

    ```
      pip install -r requirements.txt
     
    ```
    
To build the documentation, run the following commands:

    cd user-guide
    make clean html

To view the HTML build results in the target directory (``_build/html/``), run the following command:

    open _build/html/index.html
    

## Publishing your guide

For initial setup, contact devdoc@rackspace.com to request help with the following 
tasks to build and deliver your content to production: 

- Configure your Sphinx project to be built and delivered on developer.rackspace.com

- Review your documentation and set up an editorial review process for ongoing 
  content development.

Once your content is built and delivered to developer.rackspace.com/docs/user-guides/, you 
can rebuild and redeploy your content automatically by merging changes to the master 
branch of the doc source repository.  


