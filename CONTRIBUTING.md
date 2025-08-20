# Contributing to django-fingerprinting-middleware 🚀

First off, thanks for considering contributing! Your help makes this project better for everyone. 💛

This guide will walk you through how to get started, code conventions, testing, and submitting contributions.


## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Setup](#development-setup)
4. [Coding Guidelines](#coding-guidelines)
5. [Testing](#testing)
6. [Git Workflow](#git-workflow)
7. [Pull Requests](#pull-requests)
8. [Reporting Issues](#reporting-issues)
9. [Community](#community)


## Code of Conduct

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md). We are committed to providing a welcoming and harassment-free environment for all contributors.


## Getting Started

### 1. Fork the repository

Click “Fork” in the top-right corner.


### 2. Clone your fork

```bash
git clone git@github.com:k3y5tr0k3/django-fingerprinting-middleware.git
cd django-fingerprinting-middleware
```


### 3. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r test-requirements.txt
```


## Development Setup

We use Hatch for building.

```bash
pip install hatch
```


## Coding Guidelines

**Language:** Python >= 3.12

**Style:** PEP8

**Formatting:** We use black for formatting, and you can automatically reformat the project code with:

```bash
ruff format
```

**Linting:** We use ruff:

```bash
ruff check
```

**Docstrings:** Strict Google style docstrings

**Tests:** Every new function must include tests. One to test success flow, and one for every possible failure scenario/exception.

## Testing

We use pytest for testing:

```bash
pytest
```

**Ensure all tests pass locally.**

**Coverage should not decrease.**

## Git Workflow

**Create a feature branch**

```bash
git checkout -b feature/my-awesome-feature
```

**Commit changes**

```bash
git add .
git commit -m "Add my awesome feature"
```

**Rebase frequently with main**

```bash
git fetch origin
git rebase origin/main
```

## Pull Requests

Push your branch to your fork

```bash
git push origin feature/my-awesome-feature
```

**Open a Pull Request against main**

- Title: concise and descriptive

- Description: what, why, impact, pros, cons

- Link any relevant issues: Closes #123

- PR will be reviewed; address feedback promptly

## Reporting Issues

Use GitHub Issues for bugs and feature requests:

- Provide a clear title

- Steps to reproduce

- Expected vs actual behavior

- Include logs

## Community

Be respectful and kind 🫶

Ask questions freely in discussions

Celebrate small wins together


## Thank You

Thank you for contributing to django-fingerprinting-middleware! Your efforts help make this project better for everyone.
