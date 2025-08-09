# PyDWG Packaging and PyPI Publishing Guide

This guide will walk you through the process of packaging your PyDWG project and publishing it to PyPI.

## Prerequisites

1. **Python 3.7+** installed
2. **Git** installed and configured
3. **PyPI account** created at https://pypi.org/account/register/
4. **TestPyPI account** created at https://test.pypi.org/account/register/

## Step 1: Update Package Information

Before packaging, update the following files with your information:

### 1.1 Update `setup.py`
```python
# Replace these placeholders:
author="Your Name",
author_email="your.email@example.com",
url="https://github.com/yourusername/pydwg",
```

### 1.2 Update `pyproject.toml`
```toml
# Replace these placeholders:
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
maintainers = [
    {name = "Your Name", email = "your.email@example.com"}
]

[project.urls]
Homepage = "https://github.com/yourusername/pydwg"
Documentation = "https://github.com/yourusername/pydwg#readme"
Repository = "https://github.com/yourusername/pydwg"
"Bug Tracker" = "https://github.com/yourusername/pydwg/issues"
```

### 1.3 Update `pydwg/__init__.py`
```python
__author__ = "Your Name"
__email__ = "your.email@example.com"
```

### 1.4 Update `LICENSE`
```text
Copyright (c) 2024 Your Name
```

## Step 2: Install Build Tools

```bash
pip install --upgrade pip
pip install build twine
```

## Step 3: Build the Package

### 3.1 Clean previous builds
```bash
# Remove previous build artifacts
rm -rf build/ dist/ *.egg-info/
```

### 3.2 Build the package
```bash
python -m build
```

This will create:
- `dist/pydwg-1.0.0.tar.gz` (source distribution)
- `dist/pydwg-1.0.0-py3-none-any.whl` (wheel distribution)

## Step 4: Test the Package Locally

### 4.1 Install in development mode
```bash
pip install -e .
```

### 4.2 Test the command-line interface
```bash
pydwg --help
```

### 4.3 Test the Python API
```python
from pydwg import FourSectionCutGenerator
print("Package imported successfully!")
```

## Step 5: Upload to TestPyPI (Recommended)

### 5.1 Upload to TestPyPI
```bash
python -m twine upload --repository testpypi dist/*
```

You'll be prompted for your TestPyPI credentials.

### 5.2 Test installation from TestPyPI
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ pydwg
```

### 5.3 Test the installed package
```bash
pydwg --help
```

## Step 6: Upload to PyPI

### 6.1 Upload to PyPI
```bash
python -m twine upload dist/*
```

You'll be prompted for your PyPI credentials.

### 6.2 Verify the upload
Visit https://pypi.org/project/pydwg/ to see your package.

## Step 7: Install and Test

### 7.1 Install from PyPI
```bash
pip install pydwg
```

### 7.2 Test the installation
```bash
pydwg --help
```

## Step 8: Version Management

### 8.1 Update version numbers
When releasing a new version, update these files:

1. `setup.py`: `version="1.0.1"`
2. `pyproject.toml`: `version = "1.0.1"`
3. `pydwg/_version.py`: `__version__ = "1.0.1"`

### 8.2 Create a new release
```bash
# Clean and rebuild
rm -rf build/ dist/ *.egg-info/
python -m build
python -m twine upload dist/*
```

## Troubleshooting

### Common Issues

1. **"Package name already exists"**
   - Check if the name "pydwg" is available on PyPI
   - Consider using a different name like "pydwg-drilling" or "pydwg-tunnel"

2. **Import errors during testing**
   - Ensure all dependencies are installed
   - Check that AutoCAD is running if testing AutoCAD integration

3. **Build errors**
   - Ensure all required files are present
   - Check that `MANIFEST.in` includes all necessary files

### Testing Checklist

- [ ] Package builds without errors
- [ ] Package installs correctly
- [ ] Command-line interface works
- [ ] Python API imports correctly
- [ ] All dependencies are properly specified
- [ ] Documentation is up to date

## Additional Resources

- [PyPI Packaging Guide](https://packaging.python.org/tutorials/packaging-projects/)
- [Python Packaging User Guide](https://packaging.python.org/guides/)
- [Twine Documentation](https://twine.readthedocs.io/)

## Security Notes

- Never commit API keys or credentials to version control
- Use environment variables for sensitive information
- Consider using API tokens instead of passwords for PyPI uploads

## Next Steps

After successful publication:

1. **Create a GitHub repository** for your project
2. **Add documentation** and examples
3. **Set up CI/CD** for automated testing and deployment
4. **Add badges** to your README (build status, PyPI version, etc.)
5. **Create releases** on GitHub for each PyPI version 