Development
===========

Setting Up Your Development Environment
---------------------------------------

Virtual Environment
~~~~~~~~~~~~~~~~~~~

You'll want to use a virtual environment, it makes things way easier. Learned this in lab 2!

.. code-block:: bash

   # Create the virtual environment
   python3 -m venv venv

   # Activate it
   # macOS/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate

   # When you're done working
   deactivate

Installing Dependencies
~~~~~~~~~~~~~~~~~~~~~~~

Once your virtual environment is activated, install everything:

.. code-block:: bash

   pip install -r requirements.txt

Dependencies
------------

Here's what we're using in this project:

* **Flask** - Makes web development way easier
* **SQLAlchemy** - The ORM that lets us use Python instead of raw SQL
* **PostgreSQL** - Our database
* **bcrypt** - For password security (used in lab 6)
* **pytest** - Testing framework we used in lab 8
* **Sphinx** - What built this documentation

Running Applications
--------------------

Most labs have an ``app.py`` file. To run it:

.. code-block:: bash

   cd labs/lab-X
   python3 app.py

Then open your browser and go to ``http://127.0.0.1:5000``. Don't forget to refresh if you make changes!

Database Setup
--------------

From lab 3, here's how to set up your database:

1. Download PostgreSQL from https://www.postgresql.org/download/
2. Create a database called ``marist`` (or whatever you want)
3. Make a ``.env`` file in your lab directory:

.. code-block:: env

   db_name=marist
   db_owner=postgres
   db_pass=your_password_here

**Important**: Don't commit your ``.env`` file! It's in .gitignore for a reason.

Testing
-------

For labs with tests (like lab 8), run them with:

.. code-block:: bash

   cd labs/lab-X
   python3 -m pytest -v

The ``-v`` flag gives you more detailed output.

Version Control
---------------

Always work in a branch! Never commit directly to main:

.. code-block:: bash

   git checkout -b lab-X
   # Do your work here
   git add .
   git commit -m "describe what you did"
   git push --set-upstream origin lab-X

