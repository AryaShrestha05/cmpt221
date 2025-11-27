Troubleshooting
===============

Common Issues and Solutions
---------------------------

I've run into these problems before, here's what worked for me:

Database Connection Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Can't connect to PostgreSQL

**What I did**:

* Make sure PostgreSQL is actually running - check pgAdmin
* Double-check your ``.env`` file has the right info (spent way too long on this once)
* Make sure you created the database in pgAdmin first
* Verify the database name matches what's in your ``.env`` file

Virtual Environment Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: "Module not found" even though you just installed it

**What I did**:

* Check if your virtual environment is activated - look for ``(venv)`` in your terminal
* Sometimes you need to reinstall: ``pip install -r requirements.txt``
* Make sure VS Code (or whatever editor) is using the right Python interpreter

Port Already in Use
~~~~~~~~~~~~~~~~~~~

**Problem**: Flask says port 5000 is already in use

**What I did**:

* Kill whatever's using port 5000:
  
  .. code-block:: bash

     # macOS/Linux:
     lsof -ti:5000 | xargs kill -9
     
     # Windows:
     netstat -ano | findstr :5000
     taskkill /PID <PID> /F

* Or just use a different port in ``app.py``:
  
  .. code-block:: python

     app.run(debug=True, port=5001)

Import Errors
~~~~~~~~~~~~~

**Problem**: Import errors everywhere

**What I did**:

* Make sure you're in the right directory
* Check that ``__init__.py`` files exist in your package folders (this got me in lab 4)
* Double-check your import paths are correct
* Make sure you actually installed the package: ``pip install <package-name>``

Password Hashing Issues
~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Login won't work even with the right password

**What I did** (from lab 6):

* Make sure you're encoding passwords the same way (UTF-8)
* Check that you're using bcrypt for both hashing when signing up AND verifying when logging in
* The salt should be generated automatically, so make sure you're not doing anything weird there

Testing Issues
~~~~~~~~~~~~~~

**Problem**: Tests won't run or pytest isn't found

**What I did** (from lab 8):

* Install pytest: ``pip install pytest pytest-flask``
* Make sure test files are named correctly (start with ``test_``)
* Check your ``conftest.py`` has the right setup
* Run tests from the lab directory, not the root

Git Issues
~~~~~~~~~~

**Problem**: Merge conflicts or can't push

**What I did**:

* Pull the latest changes first: ``git pull origin main``
* Fix conflicts manually (VS Code makes this easier)
* Make sure you're on the right branch: ``git branch``
* Check your remote: ``git remote -v``

Getting Help
------------

When I'm stuck:

1. Read the error message - it usually tells you what's wrong
2. Google the error (Stack Overflow usually has the answer)
3. Check the lab's ``.md`` file for hints
4. Look at the Resources section above
5. Ask for help - no shame in it!

