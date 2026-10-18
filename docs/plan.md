# Minimal Calculator Packaging and DevOps Plan

## Purpose

This is a small learning repository. The goal is to understand the complete path from Python source code to an installable package, Docker image, and automatic GitHub release. Each step should use the fewest files and tools needed to demonstrate one idea.

Do not add coverage targets, type checking, dependency bots, security scanners, changelog automation, container registries, or complex release approvals yet. They are useful later, but would distract from the core workflow.

## Current state

- The calculator source is in the `app` package and has a `calculator` CLI entry point.
- The existing 12 tests pass locally.
- `setup.py` can package the code, but a small `pyproject.toml` is the current standard and is easier to use with build tools.
- GitHub Actions currently runs pylint and tests on every push.
- A root `.gitignore` now excludes local Python and build artifacts.

## The learning path

### 1. Package the existing code

- [ ] Keep the existing `app` package. Renaming it or switching to a `src/` layout is not necessary for this exercise.
- [ ] Replace `setup.py` with one minimal `pyproject.toml` using `setuptools`.
- [ ] Include only: package name, version, description, supported Python version, package discovery, and the `calculator = "app.cli:main"` console command.
- [ ] Add a short `README.md` with installation and command examples.
- [ ] Add the `build` development dependency.
- [ ] Build the package locally with `python -m build`.
- [ ] Install the resulting wheel in a clean virtual environment and run `calculator add 1 2`.

**What this teaches:** a wheel and source distribution are the files a Python package registry installs.

### 2. Install directly from GitHub

- [ ] Push the project to a GitHub repository.
- [ ] Confirm that the source can be installed without PyPI:

	```powershell
	pip install "git+https://github.com/<owner>/<repository>.git"
	```

- [ ] Add this command to the README.

**What this teaches:** `pip` can install a package directly from a Git repository. This is separate from publishing to PyPI.

### 3. Keep CI small

- [ ] Simplify the existing workflow so it runs on pushes and pull requests.
- [ ] Use one supported Python version, such as Python 3.13.
- [ ] In one job: install the project and test dependencies, run `pytest`, and run `python -m build`.
- [ ] Upload the `dist/` directory as a workflow artifact.

**What this teaches:** CI independently proves that the project tests and packages successfully on GitHub.

### 4. Dockerize the installed package

- [ ] Add `.dockerignore` for `.git`, virtual environments, caches, and `dist/`.
- [ ] Simplify the Dockerfile to copy the project, install it with `pip install .`, and start the `calculator` command.
- [ ] Build and run it locally:

	```powershell
	docker build -t calculator-demo .
	docker run --rm calculator-demo add 1 2
	```

- [ ] Add `docker build` to the CI job. Do not publish the image yet.

**What this teaches:** Docker packages the same installable project with its Python runtime.

### 5. Publish a release

- [ ] Create a PyPI account and choose an available package name. The final name may differ from the repository name because PyPI names must be globally unique.
- [ ] Configure PyPI Trusted Publishing for this GitHub repository. This lets GitHub Actions publish without a stored PyPI token.
- [ ] Add a second workflow that runs only when a tag such as `v0.1.0` is pushed.
- [ ] In that release workflow: build the package, publish it to PyPI, and create a GitHub Release.
- [ ] Verify the release in a fresh virtual environment:

	```powershell
	pip install <published-package-name>
	calculator add 1 2
	```

**What this teaches:** a Git tag can trigger a repeatable CI/CD release that publishes the exact built package.

## Files to end up with

```text
pyproject.toml
README.md
.gitignore
.dockerignore
Dockerfile
.github/workflows/ci.yml
.github/workflows/release.yml
```

## Final success check

After tagging a version, the GitHub release workflow should run tests, build the wheel and source distribution, publish the package to PyPI, and create a GitHub Release. Users should then be able to install either from GitHub or PyPI and run `calculator`.

## Optional next topics

Only after the above works, add formatting/linting, multiple Python versions, TestPyPI, a container registry, code coverage, and security scanning one at a time.