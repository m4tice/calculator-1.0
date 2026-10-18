# DevOps Guide

This repository is a small template for learning how application code becomes a tested Python package, a Docker image, and eventually a published release. As a feature developer, normally change only `app/` and `tests/`; the packaging, container, and workflow files are the delivery template.

## What Is Automated Today

| Area | File | Current behavior |
| --- | --- | --- |
| Python package | `pyproject.toml` | Defines the package and the `calculator` command. |
| CI | `.github/workflows/custom.yml` | Runs pylint and pytest for every push. |
| Docker | `Dockerfile` | Runs the calculator CLI in a Python container. |
| Publishing | Not configured | PyPI and container-image publishing are future template steps. |

## Developer Workflow

1. Create a branch and implement a feature in `app/`.
2. Add or update a test in `tests/`.
3. Run the local checks from the repository root:

   ```powershell
   python -m pytest
   python -m app.cli add 1 2
   python -m build
   ```

4. Commit and push the branch. GitHub Actions runs the existing CI workflow.
5. Open a pull request and merge only after the GitHub Actions check passes.

`python -m build` creates a wheel and source distribution in `dist/`. They are ignored by Git because they are generated release artifacts.

## Use It As a Library or CLI

For local development:

```powershell
python -m pip install -e .
calculator multiply 4 5
```

For a quick source-only check, use module mode:

```powershell
python -m app.cli multiply 4 5
```

Do not run `python app/cli.py ...`; the `app` package cannot resolve its own imports that way.

## Docker Workflow

Build and run the calculator locally:

```powershell
docker build -t calculator-demo .
docker run --rm calculator-demo add 1 2
```

The current Dockerfile copies the repository and starts `python -m app.cli`. It demonstrates container execution, but it does not publish an image. Keep container changes small and verify the two commands above before pushing.

## Publishing Flow

There are two ways to install the project after it is hosted on GitHub:

```powershell
pip install "git+https://github.com/<owner>/<repository>.git"
```

This installs directly from Git and needs no release workflow. For a real public package, a template maintainer must first add a tag-triggered release workflow that builds the package, creates a GitHub Release, and publishes to PyPI using Trusted Publishing. Then users install a released version with:

```powershell
pip install <published-package-name>
```

The release workflow should be triggered only by a version tag, for example `v0.1.0`. A developer changes functionality; the release owner increments the version in `pyproject.toml`, pushes a matching tag, and GitHub Actions publishes the already-built package.

## Template Owner Checklist

To make delivery nearly one-click, add these in order:

1. Update CI to run on pull requests, build the package, and upload `dist/` as an artifact.
2. Add `.dockerignore` and make CI build the Docker image.
3. Configure PyPI Trusted Publishing for the GitHub repository.
4. Add a `release.yml` workflow triggered by `v*` tags to build, publish to PyPI, and create a GitHub Release.

Keep one responsibility per workflow: CI validates changes; release publishing happens only from a deliberate version tag.
