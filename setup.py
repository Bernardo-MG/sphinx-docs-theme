# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup

from tox_test_command import ToxTestCommand
from version_extractor import extract_version_init


"""
PyPI configuration module.

This is prepared for easing the generation of deployment files.
"""

__license__ = 'MIT'

# Source package
_source_package = 'sphinx_docs_theme/'

# Test requirements
_tests_require = ['tox']


# Gets the long description from the readme
def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


setup(
    name='sphinx-docs-theme',
    packages=find_packages(),
    include_package_data=True,
    package_data={
    },
    version=extract_version_init(_source_package),
    description='Sphinx Theme for documentation sites.',
    author='Bernardo Martínez Garrido',
    author_email='programming@bernardomg.com',
    license='MIT',
    url='https://github.com/Bernardo-MG/sphinx_docs_theme',
    download_url='https://github.com/Bernardo-MG/sphinx_docs_theme',
    keywords=['sphinx', 'theme', 'bootstrap', 'html5', 'python'],
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'Fabric',
        'Sphinx'
    ],
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={
        'test': ToxTestCommand
    },
)
