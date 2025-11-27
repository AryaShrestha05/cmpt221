# Deployment Instructions for Lab 9

## Building the Documentation

After setting up Sphinx and creating your documentation files, build the HTML documentation:

```bash
cd labs/lab-9/docs
make html
```

Or if you don't have `make` installed:
```bash
cd labs/lab-9/docs
python3 -m sphinx.cmd.build . _build
```

This will create the HTML files in `labs/lab-9/docs/_build/html/`

## Deploying to GitHub Pages

**IMPORTANT**: GitHub Pages requires documentation to be in either:
- The repository root
- A `/docs` directory at the repository root

After building your documentation, follow these steps from your repository ROOT (`/cmpt221`):

### Option 1: Using the provided script (macOS/Linux)

```bash
# From repository root
./labs/lab-9/deploy-docs.sh
```

### Option 2: Manual steps

```bash
# 1. Create a new directory named docs at repository root
mkdir -p docs

# 2. Move all files from labs/lab-9/docs/_build/html/* to ./docs/
cp -r labs/lab-9/docs/_build/html/* ./docs/

# 3. Create .nojekyll file (tells GitHub not to process with Jekyll)
touch ./docs/.nojekyll
```

**Note**: If a `.nojekyll` file already exists at the repository root, move it to the docs directory:
```bash
mv .nojekyll ./docs/
```

## GitHub Pages Configuration

1. Go to your GitHub repository
2. Click **Settings**
3. Click **Pages** from the left sidebar
4. Under **Source**, select:
   - Branch: `main` (or your default branch)
   - Folder: `/docs`
5. Click **Save**

GitHub will provide you with a URL like: `https://username.github.io/cmpt221/`

## Troubleshooting

- If your documentation doesn't appear, check that:
  - All files were copied to `/docs` correctly
  - The `.nojekyll` file exists in `/docs`
  - GitHub Pages is configured to use the `/docs` folder
  - You've pushed all changes to GitHub

- If you see 404 errors:
  - Wait a few minutes for GitHub Pages to build
  - Check the Actions tab for any build errors
  - Verify the branch and folder settings in Pages configuration

