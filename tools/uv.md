# uv - Fast Python Package Manager

`uv` is an extremely fast Python package installer and resolver, written in Rust. It's designed as a drop-in replacement for pip and pip-tools.

## Installation

```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# With brew
brew install uv

# With pip
pip install uv
```

## Basic Usage

```bash
# Create a virtual environment
uv venv

# Install packages
uv pip install requests
uv pip install -r requirements.txt

# Compile requirements
uv pip compile requirements.in -o requirements.txt

# Show installed packages
uv pip list

# Uninstall packages
uv pip uninstall requests
```

## uv pip sync

`uv pip sync` synchronizes the environment to match a requirements file exactly. It will install missing packages and uninstall any packages not listed in the requirements file.

```bash
# Sync environment with requirements.txt
uv pip sync requirements.txt

# Sync with multiple requirement files
uv pip sync requirements.txt dev-requirements.txt

# Dry run to see what would change
uv pip sync requirements.txt --dry-run

# Sync with a specific Python version
uv pip sync requirements.txt --python 3.11
```

### Common Workflow

```bash
# 1. Compile dependencies from requirements.in
uv pip compile requirements.in -o requirements.txt

# 2. Sync environment to match compiled requirements
uv pip sync requirements.txt

# This ensures your environment exactly matches the locked dependencies
```

## uvx - Run Python Tools

`uvx` runs Python applications in isolated temporary environments (similar to `npx` for Node.js).

```bash
# Run a Python tool without installing it
uvx ruff check .
uvx black --check .
uvx pytest

# Run a specific version
uvx ruff@0.1.0 check .

# Run with additional packages
uvx --with pandas --with numpy python script.py

# Run from a specific Python version
uvx --python 3.11 black --check .

# Run a script from a URL
uvx https://example.com/script.py
```

### Common Tools to Run with uvx

```bash
# Code formatting
uvx black .
uvx isort .

# Linting
uvx ruff check .
uvx flake8 .
uvx pylint mypackage/

# Type checking
uvx mypy .

# Testing
uvx pytest
uvx coverage run -m pytest

# Project scaffolding
uvx cookiecutter gh:user/template

# HTTP requests
uvx httpie https://api.example.com

# Package publishing
uvx twine upload dist/*
```

## Project Management

```bash
# Initialize a new project
uv init myproject
cd myproject

# Add a dependency
uv add requests

# Add a dev dependency
uv add --dev pytest

# Remove a dependency
uv remove requests

# Run a command in the project environment
uv run python script.py
uv run pytest

# Sync project dependencies
uv sync
```

## Performance Comparison

uv is significantly faster than pip:
- 10-100x faster for most operations
- Parallel downloads
- Better dependency resolution
- Cached package installations

## Tips

- Use `uv pip sync` for reproducible environments in CI/CD
- Use `uvx` for one-off tool executions without polluting your environment
- Combine with `requirements.in` files for dependency management
- uv caches packages globally for faster reinstalls
- uv respects `PIP_INDEX_URL` and other pip environment variables

## Resources

- [Official Documentation](https://github.com/astral-sh/uv)
- [uv vs pip Performance](https://github.com/astral-sh/uv#benchmarks)
