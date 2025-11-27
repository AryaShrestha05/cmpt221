Troubleshooting
===============

Common Issues and Solutions
---------------------------

Database Connection Errors
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Cannot connect to PostgreSQL database

**Solutions**:

* Verify PostgreSQL is running: Check the service status in pgAdmin
* Check ``.env`` file exists and contains correct credentials
* Verify database name, username, and password are correct
* Ensure database has been created in pgAdmin

Virtual Environment Issues
~~~~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Module not found errors after installing packages

**Solutions**:

* Ensure virtual environment is activated (check for ``(venv)`` in terminal prompt)
* Reinstall dependencies: ``pip install -r requirements.txt``
* Verify you're using the correct Python interpreter in your IDE

Port Already in Use
~~~~~~~~~~~~~~~~~~~

**Problem**: ``Address already in use`` error when running Flask app

**Solutions**:

* Find and kill the process using port 5000:
  
  .. code-block:: bash

     # On macOS/Linux:
     lsof -ti:5000 | xargs kill -9
     
     # On Windows:
     netstat -ano | findstr :5000
     taskkill /PID <PID> /F

* Or change the port in ``app.py``:
  
  .. code-block:: python

     app.run(debug=True, port=5001)

Import Errors
~~~~~~~~~~~~~

**Problem**: ``ModuleNotFoundError`` or ``ImportError``

**Solutions**:

* Ensure you're in the correct directory
* Check that all ``__init__.py`` files exist in package directories
* Verify the module path is correct in import statements
* Ensure the package is installed: ``pip install <package-name>``

Password Hashing Issues
~~~~~~~~~~~~~~~~~~~~~~~

**Problem**: Password verification fails even with correct password

**Solutions**:

* Ensure passwords are encoded consistently (UTF-8)
* Verify bcrypt is being used for both hashing and verification
* Check that salt is being generated properly

Testing Issues
~~~~~~~~~~~~~~

**Problem**: Tests fail or pytest not found

**Solutions**:

* Install pytest: ``pip install pytest pytest-flask``
* Ensure test files start with ``test_`` or end with ``_test.py``
* Check that test fixtures are properly configured in ``conftest.py``
* Run tests from the correct directory

Git Issues
~~~~~~~~~~

**Problem**: Merge conflicts or push rejected

**Solutions**:

* Pull latest changes: ``git pull origin main``
* Resolve conflicts manually in the affected files
* Ensure you're on the correct branch: ``git branch``
* Check remote is set correctly: ``git remote -v``

Getting Help
------------

If you continue to experience issues:

1. Check the error message carefully - it often contains useful information
2. Search for the error message online (Stack Overflow, GitHub Issues)
3. Review the relevant lab's documentation files (``*.md``)
4. Consult the Resources section for official documentation
5. Reach out to your instructor or teaching assistant

