=================
Sphinx Docs Theme
=================

A minimalist Bootstrap-based HTML5 theme for Sphinx, used to easily create a
noticeable documentation site.

The skin has been adapted from the static template `Docs Bootstrap Template`_,
which will be the visual reference to be followed by this project.

.. image:: https://badge.fury.io/py/sphinx-docs-theme.svg
    :target: https://pypi.python.org/pypi/sphinx-docs-theme
    :alt: CWR-API Pypi package page

.. image:: https://readthedocs.org/projects/sphinx-docs-theme/badge/?version=latest
    :target: http://sphinx-docs-theme.readthedocs.org/en/latest/
    :alt: Cookiecutter Python Library latest documentation Status
.. image:: https://readthedocs.org/projects/sphinx-docs-theme/badge/?version=develop
    :target: http://sphinx-docs-theme.readthedocs.org/en/develop/
    :alt: Cookiecutter Python Library development documentation Status

Features
--------

- Minimalist and reactive look
- HTML5
- Bootstrap
- Font Awesome icons

Documentation
-------------

Check the `latest docs`_ for the most current version of the documentation.

You can also create the documentation from the source files, kept in the 'docs'
folder, with the help of Sphinx. For this use the makefile, or the make.bat
file, contained on that folder.

Prerequisites
~~~~~~~~~~~~~

`Sphinx`_ is required to make use of this theme, as it is meant to be integrated
into a Sphinx project. To find more information about this check its webpage,
which will also tell which Python interpreters can be used.

All other dependencies are indicated on the requirements.txt file.
These can be installed with the included makefile by using the following
command:

``$ make requirements``

Installing
~~~~~~~~~~

The project is offered as a `Pypi package`_, and using pip is the preferred way
to install it. For this use the following command;

``$ pip install sphinx-docs-theme``

If manual installation is required, the project includes a setup.py file, along
a makefile allowing direct installation of the library, which can be done with
the following command:

``$ make install``

Usage
-----

The theme can be used just by adding the following lines to the conf.py file
of any `Sphinx`_ project:

.. code::

    import sphinx_docs_theme

    html_theme = 'sphinx_docs_theme'
    html_theme_path = sphinx_docs_theme.get_html_theme_path()

Collaborate
-----------

Any kind of help with the project will be well received, and there are two main ways to give such help:

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
.. _latest docs: http://sphinx-docs-theme.readthedocs.org/en/latest/
.. _Pypi package: https://pypi.python.org/pypi/sphinx-docs-theme
.. _MIT License: http://www.opensource.org/licenses/mit-license.php