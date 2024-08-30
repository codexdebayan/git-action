## GitHub Actions CI Pipeline

This repository is equipped with a Continuous Integration (CI) pipeline powered by GitHub Actions. The pipeline automatically builds and tests the project whenever changes are pushed to the `main` branch or a pull request is opened.

### Workflow Overview

1. **Triggers:**
   - The pipeline triggers on pushes and pull requests to the `main` branch.

2. **Environment Setup:**
   - The workflow sets up a Python environment using Python 3.9.

3. **Dependencies:**
   - Dependencies are installed from `requirements.txt`, and caching is used to speed up subsequent builds.

4. **Testing:**
   - Tests are run using `pytest`. The workflow stops after 5 test failures to minimize resource usage.

### How to Contribute

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.
4. Ensure all tests pass before merging.
