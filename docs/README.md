# Information
This document provides an overview of this docs directory and the template's development tooling.

## File Structure
| File | Description |
|--|--|
| [docs](./docs) | Additional documentation, images for README.md and more. |
| [src](./src) | Contains your actual Python package source code. |
| [tests](./tests) | Contains all your tests, separate from the main source. |
| [pyproject.toml](./pyproject.toml) | The central configuration file. It defines project metadata, dependencies, and settings for tools like linters and formatters. |

## Dependencies
### [Release Drafter](https://github.com/release-drafter/release-drafter)
Automates the creation of draft release notes for your GitHub releases based on merged pull requests.

#### Location
| File | Description |
|--|--|
| [.github/workflows/release-drafter.yml](./.github/workflows/release-drafter.yml) | Contains the workflow that runs Release Drafter. |
| [.github/release-drafter.yml](./.github/release-drafter.yml) | Contains the configuration of Release Drafter. |

### Linting & Security Scanning: [Checkov](https://github.com/bridgecrewio/checkov)
These tools help ensure your Terraform code is valid, follows best practices, and is free from common security vulnerabilities.
* **Checkov**: A static code analysis tool for IaC to find misconfigurations that may lead to security or compliance problems.

#### Location
| File | Description |
|--|--|
| [.github/workflows/terraform-linter.yml](./.github/workflows/terraform-docs.yml) | Contains the workflow that runs TFLint, Trivy & Checkov. |
| [.checkov.yaml](./.checkov.yaml) | Contains the configuration of Chekov. |

### [Pre-commit](https://github.com/pre-commit/pre-commit)
A framework for managing and maintaining multi-language pre-commit hooks. It runs checks on your code before you commit, helping to enforce code quality and catch issues early.

#### Location
| File | Description |
|--|--|
| [.pre-commit-config.yaml](./.pre-commit-config.yaml) | Contains the configuration of pre-commit. |

#### Usage
First, install dependencies:
```bash
```

1. Install git hooks: `pre-commit install`
1. Manually run all files: `pre-commit run --all-files`
1. Manually run a specific hook: `pre-commit run <hook_id>`
1. Skip hooks: `git commit --no-verify -m "Your commit message"`
