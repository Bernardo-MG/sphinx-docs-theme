#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Docs Sphinx Theme Python library documentation build configuration file.

import ast
import re
import sys
import os
import datetime
from codecs import open
from os import path

# -- Version --------------------------------------------------------------

# Regular expression for the version
_version_re = re.compile(r'__version__\s+=\s+(.*)')

# Path to the project's root
here = path.abspath(path.dirname(__file__))

# Gets the version for the source folder __init__.py file
with open('../../sphinx_docs_theme/__init__.py', 'rb',
          encoding='utf-8') as f:
    version_lib = f.read()
    version_lib = _version_re.search(version_lib).group(1)
    version_lib = str(ast.literal_eval(version_lib.rstrip()))

# -- Code location --------------------------------------------------------

sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('../../sphinx_docs_theme'))


# -- General configuration ------------------------------------------------

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.ifconfig',
    'sphinx.ext.viewcode',
]

# Templates.
templates_path = ['_templates']

# Only accepts reStructuredText
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Docs Sphinx Theme'
project_safe = project.replace(' ', '_')
copyright = u'%s, Bernardo Martínez Garrido' % datetime.datetime.now().year
authors = [u'Bernardo Martínez Garrido']

# The version info for the project.
#
# Semantic version value.
version = version_lib
# The full version, including alpha/beta/rc tags.
release = version

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

import sphinx_docs_theme

# Activate the theme.
html_theme = 'sphinx_docs_theme'
html_theme_path = sphinx_docs_theme.get_html_theme_path()

# Theme options.
# html_theme_options = {
#     'navbar_fixed_top': 'true',
#     'navbar_site_name': 'Contents',
#     'bootstrap_version': '3',
#     'source_link_position': 'footer',
#     'bootswatch_theme': 'yeti',
#     'navbar_links': [
#         (scm_name,
#          scm_url,
#          True),
#     ],
# }

# Theme options.
html_theme_options = {
    'keywords': 'Sphinx, theme, Bootstrap, documentation',
    'author_name': u'Bernardo Martínez Garrido',
    'author_url': 'https://github.com/Bernardo-MG',
    'twitter_id': '@wandrell',
    'publish_date': datetime.datetime.now().date(),
    'version': version,
    'scm_name': 'Github',
    'scm_url': 'https://github.com/Bernardo-MG/sphinx-docs-theme',
    'ci_name': 'Travis',
    'ci_url': 'https://travis-ci.org/Bernardo-MG/sphinx-docs-theme',
    'issues_name': 'Github',
    'issues_url': 'https://github.com/Bernardo-MG/sphinx-docs-theme/issues',
    'supported_list': ['Sphinx'],
    'releases_repos': [('Pypi','https://pypi.python.org/pypi/sphinx-docs-theme')],
}

# Output file base name for HTML help builder.
htmlhelp_basename = '%s doc' % project

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
}

# List of LaTeX documents.
latex_documents = [
    (master_doc, '%s.tex' % project_safe, '%s Documentation' % project,
     ','.join(authors), 'manual'),
]


# -- Options for manual page output ---------------------------------------

# List of manual pages.
man_pages = [
    (master_doc, project, '%s Documentation' % project,
     [','.join(authors)], 1)
]


# -- Options for Texinfo output -------------------------------------------

# List of Texinfo documents.
texinfo_documents = [
    (master_doc, project, '%s Documentation' % project,
     ','.join(authors), project, 'Docs Sphinx Theme.',
     'Miscellaneous'),
]


# -- Intersphinx links ----------------------------------------------------

# Intersphinx mapping.
intersphinx_mapping = {
    'https://docs.python.org/': None,
}
