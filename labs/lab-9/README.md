# Lab #9 - Documentation

## Overview
This lab covers creating documentation using Sphinx for the CMPT221 repository.

## Setup Instructions

1. **Activate your virtual environment**

2. **Install Sphinx** (if not already installed):
   ```bash
   pip install -U sphinx
   ```

3. **Navigate to the docs directory**:
   ```bash
   cd labs/lab-9/docs
   ```

4. **Build the documentation**:
   ```bash
   make html
   # or on Windows without make:
   make.bat html
   # or:
   python3 -m sphinx.cmd.build . _build
   ```

## GitHub Pages Deployment

**IMPORTANT**: After building your documentation, you need to move the built files to the repository root `/docs` directory for GitHub Pages.

Run these commands from your repository ROOT (`/cmpt221`):

```bash
# 1. Create a new directory named docs
mkdir -p docs

# 2. Move all files from the labs/lab-9/docs/_build/html/* directory to the new /docs dir
cp -r labs/lab-9/docs/_build/html/* ./docs/

# 3. If created, move your .nojekyll file to the /docs directory
if [ -f .nojekyll ]; then
    mv .nojekyll ./docs/
fi
```

Alternatively, you can use the provided script:
```bash
./labs/lab-9/deploy-docs.sh
```

## GitHub Pages Configuration

After moving the files:

1. Go to your GitHub repository
2. Click **Settings**
3. Click **Pages** from the left menu
4. Under **Branch**, select `gh-pages` branch (or `main` branch and `/docs` folder)
5. Save - GitHub will provide you with the published URL

## Submission

1. Commit and push your changes:
   ```bash
   git add .
   git commit -m "completed lab 9"
   git push --set-upstream origin lab-9
   ```

2. Submit the GitHub Pages URL to Brightspace

