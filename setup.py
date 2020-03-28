# -*- coding: utf-8 -*-
import io
from os.path import dirname
from os.path import join

from setuptools import find_packages, setup, Command
from setuptools.command.install import install

from tox_test_command import ToxTestCommand
from sphinx.setup_command import BuildDoc
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


class FrontendCommand(Command):
    """
    Frontend building command.
    """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import subprocess

        # Installs dependencies
        subprocess.check_call('npm install', shell=True)

        # Copies libraries
        subprocess.check_call('npm run copy-all', shell=True)

        # Minifies files
        subprocess.check_call('npm run minify-css', shell=True)


class InstallWithFrontend(install):

    def __init__(self, dist, **kw):
        super().__init__(dist, **kw)
        self.frontend_command = FrontendCommand(dist, **kw)

    def run(self):
        self.frontend_command.run()

        self.do_egg_install()


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
    url='https://github.com/Bernardo-MG/sphinx-docs-theme',
    download_url='https://github.com/Bernardo-MG/sphinx-docs-theme',
    keywords=['sphinx', 'theme', 'bootstrap', 'html5', 'python'],
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Sphinx',
        'Framework :: Sphinx :: Theme',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Documentation',
        'Topic :: Documentation :: Sphinx',
        'Topic :: Software Development :: Documentation'
    ],
    long_description=read('README.rst'),
    install_requires=[
        'Fabric',
        'Sphinx',
        'bernardomg.tox-test-command',
        'bernardomg.version-extractor'
    ],
    python_requires='>=3.6',
    tests_require=_tests_require,
    extras_require={'test': _tests_require},
    cmdclass={
        'build_docs': BuildDoc,
        'frontend': FrontendCommand,
        'install': InstallWithFrontend,
        'test': ToxTestCommand
    },
)
