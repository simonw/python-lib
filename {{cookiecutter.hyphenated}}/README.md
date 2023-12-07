<p align="center">
{% if cookiecutter.author_name %}
<p align="center">
   <img width="50%" height="40%" src="{{ cookiecutter.logo_img_url }}" alt="Logo">
  </p>
{% endif %}
  <h1 align="center">{{ cookiecutter.lib_name }}</h1>
  <p align="center">
  <strong>{{ cookiecutter.description }}</strong>
    <br> <br />
    <a href="#status"><strong> Status</strong></a> |
    <a href="#why"><strong> Why</strong></a> |
    <a href="#how"><strong> How </strong></a> |
    <a href="#installation"><strong> Installation </strong></a> |
    <a href="#usage"><strong> Usage </strong></a> |
    <a href="#roadmap"><strong> Roadmap </strong></a> 

   </p>
<p align="center">

<p align="center">
<a href="https://pypi.org/project/{{ cookiecutter.hyphenated }}/"><img src="https://img.shields.io/pypi/v/{{ cookiecutter.hyphenated }}?label=PyPI"></a>
<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/actions/workflows/test.yml?branch=mainline"><img src="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/actions/workflows/test.yml/badge.svg"></a>
<a href="https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}"><img src="https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/branch/main/graph/badge.svg"></a>  
<a href="https://opensource.org/licenses/Apache-2.0"><img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg"></a>
<a href="https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/releases"><img src="https://img.shields.io/github/v/release/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}?include_prereleases&label=changelog"></a>

## Status

## Why

## How


## Installation

## Usage

```bash
pip install {{ cookiecutter.hyphenated }}
```

