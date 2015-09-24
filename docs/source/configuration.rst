===================
Theme configuration
===================

The theme includes a series of variables which can be configured to adapt the
data shown.

Actually for the theme to work as expected, showing the project's full data,
it is recommended filling up as much information as possible.

The data is added to the 'html_theme_options' map variable on the Sphinx
project 'conf.py' file. As these are theme options they are also stored
on the 'theme.conf' file.

------------------
Metadata variables
------------------

========== =====
Variable   Usage
========== =====
keywords   Content for the keywords field on the header
twitter_id Id for the twitter card on the header
========== =====

-----------
Author info
-----------

=========== =====
Variable    Usage
=========== =====
author_name The author to show on the footer
author_url  Webpage of the shown author
=========== =====

------------
Release info
------------

============== =====
Variable       Usage
============== =====
years          The years range in which the project was published, as a string
publish_date   Date in which the Sphinx-created page has been published
license_name   Name of the license under which the project has been released
license_url    URL for the license
supported_list List of versions supported by the project. Usually Python versions.
============== =====

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

-----
Links
-----

Links are a list of tuples containing the name and URL for each link.

================== =====
Variable           Usage
================== =====
general_info_links List of links to show on the general info column in the folder.
docs_links         List of links to generate the docs menu.
info_links         List of links to generate the information menu.
================== =====

