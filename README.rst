=================
Sphinx Docs Theme
=================

A minimalist Bootstrap-based HTML5 theme for Sphinx. For generating
documentation sites.

Check the `latest docs`_ to find out how to set it up.

The skin has been adapted from the static template `Docs Bootstrap Template`_,
and it is the visual reference to be followed by the project.

.. image:: https://badge.fury.io/py/sphinx-docs-theme.svg
    :target: https://pypi.python.org/pypi/sphinx-docs-theme
    :alt: Sphinx docs theme Pypi package page

.. image:: https://img.shields.io/badge/docs-release-blue.svg
    :target: http://docs.bernardomg.com/sphinx-docs-theme
    :alt: Sphinx docs theme latest documentation
.. image:: https://img.shields.io/badge/docs-develop-blue.svg
    :target: http://docs.bernardomg.com/development/sphinx-docs-theme
    :alt: Sphinx docs theme development documentation

Features
--------

- Minimalist and reactive look
- `HTML5`_
- `Bootstrap 4`_
- `Font Awesome`_ icons
- `highlight.js`_ for syntax highlighting
- Prepared for `Facebook's Open Graph`_ and `Twitter Cards`_

Demo
----

To check the Sphinx Docs Theme at work take a look at the documentation, linked
below this section, which is created with Sphinx and making use of this theme.

Documentation
-------------

Documentation sources are included with the project, and used to generate the
documentation sites:

- The `latest docs`_ are always generated for the latest release, kept in the 'master' branch
- The `development docs`_ are generated from the latest code in the 'develop' branch

The source files for the docs, a small `Sphinx`_ project, are kept in the 'docs folder.

These can be built if needed:

``python setup.py build_docs``

Usage
-----

The project is a `Sphinx`_ theme, which can be used in a similar way to any
other such theme.

Prerequisites
~~~~~~~~~~~~~

`Sphinx`_ is required to make use of this theme, as it is meant to be integrated
into a Sphinx project. To find more information about this check its webpage,
which will also tell which Python interpreters can be used.

All other Python dependencies are indicated on the requirements.txt file.

These dependencies can be installed with:

``pip install --upgrade -r requirements.txt``

The frontend libraries are defined as `npm`_ dependencies, and require this package
manager to be defined.

These dependencies can be installed with:

``python setup.py frontend``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``pip install sphinx-docs-theme``

If needed, manual installation is possible:

``python setup.py install``

Using it as a dependency
~~~~~~~~~~~~~~~~~~~~~~~~

If the project has been installed in the local libraries repository, it can be
used just by adding the following lines to the conf.py file of any Sphinx
project:

.. code::

    import sphinx_docs_theme

    html_theme = 'sphinx_docs_theme'
    html_theme_path = sphinx_docs_theme.get_html_theme_path()

Using it from the Sphinx themes folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another possibility is just adding the project code, contained int the
'sphinx_docs_theme' folder, to the themes folder of your Sphinx project, which
is:

``docs\_themes\sphinx_docs_theme\``

And then it is just needed to add the following files to the conf.py file:

.. code::

    html_theme = 'sphinx_docs_theme'
    html_theme_path = ["_themes", ]

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main
ways to give such help:

- Reporting errors and asking for extensions through the issues management
- or forking the repository and extending the project

Issues management
~~~~~~~~~~~~~~~~~

Issues are managed at the GitHub `project issues tracker`_, where any Github
user may report bugs or ask for new features.

Getting the code
~~~~~~~~~~~~~~~~

If you wish to fork or modify the code, visit the `GitHub project page`_, where
the latest versions are always kept. Check the 'master' branch for the latest
release, and the 'develop' for the current, and stable, development version.

License
-------

The project has been released under the `MIT License`_.


.. _Docs Bootstrap Template: https://github.com/Bernardo-MG/docs-bootstrap-template
.. _Sphinx: http://sphinx-doc.org/
.. _GitHub project page: https://github.com/Bernardo-MG/sphinx-docs-theme
.. _project issues tracker: https://github.com/Bernardo-MG/sphinx-docs-theme/issues
.. _latest docs: http://docs.bernardomg.com/sphinx-docs-theme
.. _development docs: http://docs.bernardomg.com/development/sphinx-docs-theme
.. _Pypi package: https://pypi.python.org/pypi/sphinx-docs-theme
.. _MIT License: http://www.opensource.org/licenses/mit-license.php

.. _npm: https://www.npmjs.com/

.. _HTML5: http://www.w3.org/TR/html5/
.. _Bootstrap 4: http://getbootstrap.com
.. _Font Awesome: https://fortawesome.github.io/Font-Awesome/
.. _highlight.js: https://highlightjs.org/
.. _Facebook's Open Graph: http://ogp.me/
.. _Twitter Cards: https://dev.twitter.com/cards/overview
