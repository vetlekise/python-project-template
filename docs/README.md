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
Automates the creation of draft release notes for your GitHub releases based on merged pull requests. Its configuration and workflow are in the `.github` directory.

## Local Development Usage
### Install Dependencies
To get started, install the project and all the development tools:
```bash
pip install -e .[dev]
```

### Using Pre-commit
- **Install git hooks**: `pre-commit install` (This only needs to be run once per project clone).
- **Manually run on all files**: `pre-commit run --all-files`
- **Skip hooks for a single commit**: `git commit --no-verify -m "Your commit message"`

## Writing Documentation
This project uses [MkDocs](https://github.com/mkdocs/mkdocs) with the [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings?tab=coc-ov-file) plugin to build a full documentation website from your Markdown files and Python docstrings. Its configuration is stored in `mkdocs.yml`.

The recommended format for docstrings is the **Google Python Style Guide**. Use sections like `Args`:, `Returns`:, and `Raises`: to ensure your docstrings are parsed correctly.

### Docstring Format
Here is an example of a well-documented function:

```python
def connect_to_api(api_key: str, endpoint: str, timeout: int = 10) -> dict:
    """Connects to an API endpoint and returns the JSON response.

    This function attempts to establish a connection to a given API
    endpoint using the provided API key.

    Args:
        api_key (str): The authentication key for the API.
        endpoint (str): The full URL of the API endpoint to connect to.
        timeout (int, optional): The connection timeout in seconds.
            Defaults to 10.

    Returns:
        dict: A dictionary containing the JSON response from the API.

    Raises:
        ValueError: If the API key is empty or the endpoint is invalid.
        ConnectionError: If a connection cannot be established.
    """
    # function implementation...
```

### Viewing Docs Locally
To preview your documentation website as you make changes, run the following command from the project root:
```bash
mkdocs serve
```

This will start a local web server, and you can view your site at `http://127.0.0.1:8000`. The site will automatically reload when you save changes.

## Documentation Deployment to GitHub Pages
The workflow in `.github/workflows/docs.yml` automatically builds and deploys your documentation website to GitHub Pages. To enable the workflow, add the file extension `.yml` to the file.

For this to work, you must perform a **one-time setup** in your repository settings:
1. Navigate to your repository's **Settings** tab.
2. Go to the **Pages** section in the left sidebar.
3. Under **Build and deployment**, set the **Source** to **GitHub Actions**.

After this is configured, any push to the `main` branch will trigger the workflow and update your live documentation site.

### Using Custom Domain
To use a custom domain (e.g., `www.your-project.com`) for your documentation site:

#### Configure Your DNS Provider
1. Log in to your domain registrar (e.g., GoDaddy, Namecheap).
2. Create a `CNAME` record for your **subdomain** that points to `<your-username>.github.io`.

#### Configure GitHub
1. In your repository, go to **Settings** > **Pages**.
2. Under **Custom domain**, enter your full domain (e.g., `www.your-project.com`) and click **Save**.
3. Once the domain is verified, check the **Enforce HTTPS** box.