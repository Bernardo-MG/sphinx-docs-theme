===================
Theme configuration
===================

The theme includes a series of configuration variables. It is recommended
filling up as much information as possible to show the project's full data.

The configuration is added to the 'html_theme_options' map variable on the
Sphinx project 'conf.py' file. As these are theme options they are also stored
on the 'theme.conf' file.

-----
Links
-----

================== =====
Variable           Usage
================== =====
general_info_links List of links to show on the general info column in the folder.
navbar_links       Map of links to generate the navbar menu.
================== =====

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How are the links lists built?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The links list and map follow a simple structure where each link is a tuple
made up of a name and a URL, just as follows:

.. code::

    ('Usage', './usage.html')

These are given to the theme's configuration on the 'conf.py' file of the Sphinx
project, and as such a list of links would be like this:

.. code::

    'general_info_links': [('Acquire', './acquire.html'),
                           ('Usage', './usage.html')]

The map in similar way is just a list of tuples, containing a name and a list
of links:

.. code::

    'navbar_links': [('Documentation', [('Acquire', './acquire.html'),
                     ('Usage', './usage.html'),
                     ('Configuration', './configuration.html')])]

------------------
Metadata variables
------------------

========== ============================================ =======
Variable   Usage                                        Example
========== ============================================ =======
keywords   Content for the keywords field on the header Sphinx, theme, Bootstrap, documentation
twitter_id Id for the twitter card on the header        @BernardoMartG
========== ============================================ =======

-----------
Author info
-----------

=========== =====
Variable    Usage
=========== =====
author_name The author to show on the footer
author_url  Webpage for the shown author
=========== =====

------------
Release info
------------

============== =================================================================== =======
Variable       Usage                                                               Example
============== =================================================================== =======
years          The years range in which the project was published, as a string     2014-2015
publish_date   Date in which the Sphinx-created page has been published            datetime.datetime.now().date()
license_name   Name of the license under which the project has been released       MIT
license_url    URL for the license                                                 http://www.opensource.org/licenses/mit-license.php
============== =================================================================== =======

-----------------
Repositories info
-----------------

============== =====
Variable       Usage
============== =====
scm_name       Name of the source code repository being used
scm_url        URL for the source code repository being used
ci_name        Name of the source continuous integration service being used
ci_url         URL for the source continuous integration service being used
issues_name    Name of the issues service being used
issues_url     URL for the issues integration service being used
releases_repos List of releases repositories containing the project. It is a list of tuples containing the name and URL for each repository.
============== =====

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
How are the releases repositories links lists built?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Just like he previously mentioned links list:

.. code::

    'releases_repos': [('Pypi', 'https://pypi.python.org/pypi/sphinx-docs-theme')]
