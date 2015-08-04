This system uses the python sphinx tool for structure & building as part of the static build process. Included is a Makefile & make.bat file for cross platform building (for development/contribution).

Layout:

    _static: static assets unique to the documentation; this may include js, css, images, etc.
    _templates: custom html templates
    conf.py: Configuration, no touchy.
    index.rst: Main index / landing page for the docs
    make.bat: windows build script
    Makefile: linux/osx build

You will need Sphinx installed to build - however to contribute, all you need is a basic understanding of the project layout and Restructured Text. Here is an excellent ReST primer.

Once you're all set up: in order to build run:

make html

You will see the build output and the static files will be dropped in:

_build/html


Then open the index.html file to preview.