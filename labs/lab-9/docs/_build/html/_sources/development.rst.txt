.. _`Development`:

Development
===========

This section is intended for developers that want to create a fix or develop an enhancement to the cmpt221 application.

Code of Conduct
---------------

Coding conventions set by the maintainers are to be followed.

Repository
----------

The repository for cmpt221 is on Github: https://github.com/AryaShrestha05/cmpt221

Development Environment
-----------------------

A `Python virtual environment`_ is recommended. Once the virtual environment is activated, clone the cmpt221 repository and prepare the development environment with 

.. _Python virtual environment: https://virtualenv.pypa.io/en/latest/

.. code-block:: text

    $ git clone https://github.com/AryaShrestha05/cmpt221.git

    $ cd cmpt221

    $ pip install -r requirements.txt

This will install all local prerequisites needed for ``cmpt221`` to run.

Pytest
-------------------

Unit tests are developed using Pytest. To run the test suite, issue:

.. code-block:: text

    $ cd labs/lab-8/tests

    $ pytest test_app.py

Build Documentation
-------------------

The Github pages site is used to publish documentation for the cmpt221 application at https://aryashrestha05.github.io/cmpt221/

To build the documentation, issue:

.. code-block:: text

    $ cd labs/lab-9/docs

    $ make html

    # windows users without make installed use:

    $ make.bat html

The top-level document to open with a web-browser will be  ``labs/lab-9/docs/_build/html/index.html``.

To publish the page, copy the contents of the directory ``labs/lab-9/docs/_build/html`` into the ``docs`` directory at the repository root. Then, commit and push to the ``lab-9`` branch.

