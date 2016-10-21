# -*- coding: utf-8 -*-
import os

"""
    Docs Sphinx Theme
    ~~~~~~~~~~~~~~~~~
    Sphinx Theme for documentation sites
    :copyright: (c) 2015-2016 by Bernardo Martínez Garrido
    :license: MIT, see LICENSE for more details.
"""

__version__ = '0.2.3'
__license__ = 'MIT'


def get_html_theme_path():
    """Return list of HTML theme paths."""
    cur_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    return [cur_dir]
