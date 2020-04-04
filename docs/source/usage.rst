=====
Usage
=====

The Sphinx Docs Theme is meant for `Sphinx`_ projects.

There are two ways to apply it, which are nearly the same. It can be
installed in the local repository and then be used as a dependency, or the
project code (the 'sphinx_docs_theme' folder) can be copied to the Sphinx project
themes folder.

--------------------
Setting up the theme
--------------------

~~~~~~~~~~~~~~~~~~~~~~~~
Using it as a dependency
~~~~~~~~~~~~~~~~~~~~~~~~

If the project has been installed in the local libraries repository, it can be
used just by adding the following lines to the conf.py file of any Sphinx
project:

.. code::

    import sphinx_docs_theme

    html_theme = 'sphinx_docs_theme'
    html_theme_path = sphinx_docs_theme.get_html_theme_path()

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Using it from the Sphinx themes folder
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Another possibility is just adding the project code, contained int the
'sphinx_docs_theme' folder, to the themes folder of your Sphinx project, which
is:

.. code::

    docs\_themes\

And then it is just needed to add the following files to the conf.py file:

.. code::

    html_theme = 'sphinx_docs_theme'
    html_theme_path = ["_themes", ]

---------------
Theme variables
---------------

After setting up the theme the theme variables should be configured. To find
more about them check the `configuration`_ section.


.. _Sphinx: http://sphinx-doc.org/
.. _configuration: ./configuration.html