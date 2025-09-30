# Information
This document provides an overview of this docs directory and the development tooling.

## File Structure
| File | Description |
|--|--|
| [docs](./docs) | Contains project documentation, such as this file. |
| [src](./src) | Contains your actual Python package source code. |
| [tests](./tests) | Contains all your tests, separate from the main source. |
| [pyproject.toml](./pyproject.toml) | The central configuration file. Defines project metadata, dependencies, and all tool settings. |
| [.github/workflows](./.github/workflows) | Contains all GitHub Actions workflows for CI/CD and automation. |

## Development Tooling
> [!NOTE]
> Most tools are configured within the `pyproject.toml` file.

### [Ruff](https://github.com/astral-sh/ruff)
A Python linter and code formatter, used to enforce a consistent code style and catch common errors.

### [Mypy](https://github.com/python/mypy)
A static type checker for Python. Mypy analyzes your type hints to help you find bugs before you even run your code.

### [Pytest](https://github.com/pytest-dev/pytest)
The standard framework for writing and running tests in Python. It's used to verify that your code works as expected. All tests should be created in the `tests` directory.

### [Pre-commit](https://github.com/pre-commit/pre-commit)
A framework for managing and maintaining multi-language pre-commit hooks. It runs checks on your code before you commit, helping to enforce code quality and catch issues early. The configuration is in `.pre-commit-config.yaml`.

### [Release Drafter](https://github.com/release-drafter/release-drafter)
Automates the creation of draft release notes for your GitHub releases based on merged pull requests. Its configuration and workflow are in `.github/release-drafter.yml`.

## Local Development Usage
### Install Dependencies
To get started, install the project and all the development tools:
```bash
pip install .[dev]
```

### Using Pre-commit
- **Install git hooks**: `pre-commit install` (This only needs to be run once per project clone).
- **Manually run on all files**: `pre-commit run --all-files`
- **Skip hooks for a single commit**: `git commit --no-verify -m "Your commit message"`