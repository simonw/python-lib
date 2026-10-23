# {{ cookiecutter.hyphenated }}

[![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.hyphenated }}.svg)](https://pypi.org/project/{{ cookiecutter.hyphenated }}/){% if cookiecutter.github_username %}
[![Tests](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions/workflows/test.yml)
[![Changelog](https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}?include_prereleases&label=changelog)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/blob/main/LICENSE){% endif %}

{{ cookiecutter.description }}

## Installation

Install this library using `pip`:
```bash
pip install {{ cookiecutter.hyphenated }}
```
## Usage

Usage instructions go here.

## Development

To contribute to this library, first checkout the code. Then run the tests with [uv](https://docs.astral.sh/uv/):
```bash
cd {{ cookiecutter.hyphenated }}
uv run pytest
```
This will create a virtual environment and install the package along with its development dependencies.

If you prefer to use `pip` (version 25.1 or later), create a virtual environment and install the dependencies like this:
```bash
python -m venv venv
source venv/bin/activate
python -m pip install -e . --group dev
python -m pytest
```
