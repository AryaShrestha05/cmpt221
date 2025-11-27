#!/bin/bash

# Script to deploy Sphinx documentation to GitHub Pages
# Run this from the repository root (/cmpt221)

echo "Deploying documentation to GitHub Pages..."

# Check if we're in the repository root
if [ ! -d "labs/lab-9/docs/_build/html" ]; then
    echo "Error: Documentation not built yet. Please run 'make html' in labs/lab-9/docs/ first."
    exit 1
fi

# 1. Create docs directory if it doesn't exist
mkdir -p docs

# 2. Copy all files from _build/html to docs directory
echo "Copying built documentation to ./docs/..."
cp -r labs/lab-9/docs/_build/html/* ./docs/

# 3. Create .nojekyll file if it doesn't exist (tells GitHub Pages to process Jekyll)
echo "Creating .nojekyll file..."
touch ./docs/.nojekyll

echo "Documentation deployed successfully to ./docs/"
echo ""
echo "Next steps:"
echo "1. Commit the docs directory: git add docs/ && git commit -m 'Add documentation'"
echo "2. Push to GitHub: git push"
echo "3. Configure GitHub Pages in repository settings to use /docs folder"

