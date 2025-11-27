Development
===========

Setting Up Your Development Environment
---------------------------------------

Virtual Environment
~~~~~~~~~~~~~~~~~~~

It's recommended to use a virtual environment to manage dependencies:

.. code-block:: bash

   # Create a virtual environment
   python3 -m venv venv

   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate

   # Deactivate when done
   deactivate

Installing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Install all required packages:

.. code-block:: bash

   pip install -r requirements.txt

Dependencies
------------

The project uses the following key technologies:

* **Flask** - Web framework for building web applications
* **SQLAlchemy** - ORM for database interactions
* **PostgreSQL** - Database management system
* **bcrypt** - Password hashing and security
* **pytest** - Testing framework
* **Sphinx** - Documentation generator

Running Applications
--------------------

Most labs include an ``app.py`` file that can be run to start a local development server:

.. code-block:: bash

   cd labs/lab-X
   python3 app.py

The application will typically be available at ``http://127.0.0.1:5000``

Database Setup
--------------

1. Install PostgreSQL from https://www.postgresql.org/download/
2. Create a database (typically named ``marist``)
3. Create a ``.env`` file in the lab directory with your database credentials:

.. code-block:: env

   db_name=marist
   db_owner=postgres
   db_pass=your_password

Testing
-------

Run tests using pytest:

.. code-block:: bash

   cd labs/lab-X
   python3 -m pytest -v

Version Control
---------------

Always work in a branch for each lab:

.. code-block:: bash

   git checkout -b lab-X
   # Make changes
   git add .
   git commit -m "Your commit message"
   git push --set-upstream origin lab-X

