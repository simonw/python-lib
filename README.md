# python-lib cookiecutter template

Opinionated cookiecutter template for creating a new Python library

Use this template on your own machine with cookiecutter, or create a brand new repository based on this template entirely through the GitHub web interface using [python-lib-template-repository](https://github.com/simonw/python-lib-template-repository).

## Installation

You'll need to have [cookiecutter](https://cookiecutter.readthedocs.io/) installed. I recommend pipx for this:
```bash
pipx install cookiecutter
```
Regular `pip` will work OK too.

## Usage

Run `cookiecutter gh:simonw/python-lib` and then answer the prompts. Here's an example run:
```bash
cookiecutter gh:simonw/python-lib
```
```
lib_name []: python lib template demo
description []: Demonstrating https://github.com/simonw/python-lib
hyphenated [python-lib-template-demo]: 
underscored [python_lib_template_demo]: 
github_username []: simonw
author_name []: Simon Willison
```
I strongly recommend accepting the suggested value for "hyphenated" and "underscored" by hitting enter on those prompts.

This will create a directory called `python-lib-template-demo` - the name you enter is converted to lowercase and uses hyphens instead of spaces.

See https://github.com/simonw/python-lib-template-demo for the output of this example.

## Developing your library

Having created the new structure from the template, here's how to start working on the library.

If your library is called `my-new-library`, you can start working on it like so:
```bash
cd my-new-library
# Create and activate a virtual environment:
python3 -mvenv venv
source venv/bin/activate
# Install dependencies so you can edit the project:
pip install -e '.[test]'
# With zsh you have to run this again for some reason:
source venv/bin/activate
```
You can run the default test for your library like so:
```bash
pytest
```
This will execute the test in `tests/test_my_new_library.py`.

## Creating a Git repository for your library

You can initialize a Git repository for your library like this:
```bash
cd my-new-library
git init
git add .
git commit -m "Initial structure from template"
# Rename the 'master' branch to 'main':
git branch -m master main
```
## Publishing your library to GitHub

Use https://github.com/new to create a new GitHub repository sharing the same name as your library, which should be something like `my-new-library`.

Push your `main` branch to GitHub like this:
```bash
git remote add origin git@github.com:YOURNAME/my-new-library.git
git push -u origin main
```
The template will have created a GitHub Action which runs your library's test suite against every commit.

## Publishing your library as a package to PyPI

The template also includes a `publish.yml` GitHub Actions workflow for publishing packages to [PyPI](https://pypi.org/), using [pypa/gh-action-pypi-publish](https://github.com/pypa/gh-action-pypi-publish).

To use this action, you need to create a PyPI account and [configure a Trusted Publisher](https://til.simonwillison.net/pypi/pypi-releases-from-github) for this package.

Once you have created your account, navigate to https://pypi.org/manage/account/publishing/ and create a "pending publisher" for the package. Use the following values:

- **PyPI Project Name:** The name of your package
- **Owner:** Your GitHub username or organization - the "foo" in `github.com/foo/bar`
- **Repsitory name:** The name of your repository - the "bar" in `github.com/foo/bar`
- **Workflow name:** `publish.yml`
- **Environment name:** `release`

Now, any time you create a new "Release" on GitHub the Action will build your package and push it to PyPI.

The tag for your release needs to match the `VERSION` string at the top of your `pyproject.toml` file. You should bump this version any time you release a new version of your package.
