# PyTptCLI
Template for single python scripts run from command line interface.

The template is designed to receive settings passed using a single yaml file.
This of course can be changed.

Based on structure suggested by [Python Application Layouts: A Reference
by Kyle Stratis](https://realpython.com/python-application-layouts/)

Follow instructions in [Sphinx Getting started](https://www.sphinx-doc.org/en/master/tutorial/getting-started.html#setting-up-your-project-and-development-environment) to set up the documentation directories if required.

It is strongly suggested that you make a virtual environment
```
python -m venv .venv
```

and after installing dependent packages frees these to requirements.txt
```
pip freeze > requirements.txt
```

## Versions and Releases

### Versions
x.y.z

- x: major version when you make incompatible API change
- y: minor version when you add functionality in a backwards compatible manner
- z: patch version when you make backwards compatible bug fixes

for more details see [Semantic Versioning 2.0.0](https://semver.org/#semantic-versioning-200)

### Releases

[Managing releases in a repository](https://docs.github.com/en/github/administering-a-repository/managing-releases-in-a-repository)

## Documentation with Material for Mkdocs

[Creating your site](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration)

## Making PyPi packages

[Packaging Python Projects](https://packaging.python.org/en/latest/tutorials/packaging-projects/)