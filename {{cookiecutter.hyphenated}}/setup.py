from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="{{ cookiecutter.hyphenated }}",
    description="{{ cookiecutter.description }}",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",{% if cookiecutter.author_name %}
    author="{{ cookiecutter.author_name }}",{% endif %}{% if cookiecutter.github_username %}
    url="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}",
    entry_points="""
        [console_scripts]
        {{ cookiecutter.hyphenated }}={{ cookiecutter.hyphenated }}.cli:cli
    """,
    project_urls={
        "Issues": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/issues",
        "CI": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/actions",
        "Changelog": "https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.hyphenated }}/releases",
    },{% endif %}
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["{{ cookiecutter.underscored }}"],
    install_requires=[ "click", "setuptools", "pip"],
    extras_require={"test": ["pytest", "pytest-cov", "black", "ruff", "click"]},
    python_requires=">=3.7"
)
