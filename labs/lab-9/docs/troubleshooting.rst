Troubleshooting
===============

This section describes some common issues that can arise and possible solutions.

Issue #1: Sphinx Build Failure
-------------------------------

**Description**: When running ``make html``, Sphinx fails to build the documentation with errors about missing modules or configuration issues.

**Solution**: 

* Ensure Sphinx is installed in your virtual environment: ``pip install sphinx``
* Verify all required dependencies are installed: ``pip install -r requirements.txt``
* Check that the ``conf.py`` file exists and is properly configured
* Make sure you're running the build command from the ``labs/lab-9/docs`` directory
* If using Windows without make, use ``make.bat html`` instead

Issue #2: GitHub Pages 404 Error
---------------------------------

**Description**: After deploying documentation to GitHub Pages, the site shows a 404 error or doesn't display correctly.

**Solution**:

* Verify the ``docs`` directory is at the repository root (not in ``labs/lab-9/``)
* Ensure the ``.nojekyll`` file exists in the ``docs`` directory
* Check GitHub Pages settings: Source should be "Deploy from a branch", Branch should be ``lab-9``, Folder should be ``/docs``
* Wait a few minutes for GitHub to build and deploy the site (check the Actions tab)
* Verify all HTML files were copied from ``_build/html`` to the ``docs`` directory
* Clear browser cache and try accessing the site again

Issue #3: Virtual Environment Package Issues
---------------------------------------------

**Description**: Modules are not found even after installation, or packages are installed in the wrong environment.

**Solution**:

* Verify your virtual environment is activated (look for ``(venv)`` in your terminal prompt)
* Reinstall all packages: ``pip install -r requirements.txt``
* Check which Python interpreter is being used: ``which python3`` (macOS/Linux) or ``where python`` (Windows)
* Ensure your IDE (VS Code, PyCharm, etc.) is configured to use the virtual environment's Python interpreter
* If issues persist, recreate the virtual environment: ``deactivate``, then ``python3 -m venv venv``, then ``source venv/bin/activate`` (macOS/Linux) or ``venv\Scripts\activate`` (Windows)

