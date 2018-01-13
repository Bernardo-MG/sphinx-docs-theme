===========
Development
===========

The project has some special requirements which matter only when developing or extending it.

Mainly that the frontend dependencies are handled through `npm`_. They are added to the project
automatically when running the install command, but not before packaging.

There is a command to take care of all the frontend dependencies:

.. code::

    python setup.py frontend

.. _npm: https://www.npmjs.com/