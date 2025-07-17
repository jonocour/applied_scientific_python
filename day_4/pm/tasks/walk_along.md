
#Deploying a Simple Python Package to TestPyPI

This guide walks you through packaging a simple Python CLI app and deploying it to [TestPyPI](https://test.pypi.org).

---

##Step 1 — Prepare Your Project Structure

```
your_app/
├── your_package/
│   └── __init__.py
│   └── main.py
├── setup.py
├── pyproject.toml
├── README.md
├── LICENSE
```

---

##Step 2 — Basic `setup.py` Example

```python
from setuptools import setup, find_packages

setup(
    name='your-package-name',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'your-app=your_package.main:main',
        ],
    },
)
```

---

##Step 3 — Write Your `main.py`

```python
def main():
    print("test")

if __name__ == "__main__":
    main()
```

---

##Step 4 — Build the Package

```bash
pip install --upgrade build
python -m build
```

> You’ll get `.whl` and `.tar.gz` in the `dist/` folder

---

##Step 7 — (Optional) Test Your Package Locally

```bash
pip install dist/your_package_name-0.1.0-py3-none-any.whl
your-app
```

---

##Step 8 — Upload to TestPyPI

```bash
pip install --upgrade twine
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

> Use your `TWINE_USERNAME=__token__` and `TWINE_PASSWORD` = your API key

```bash
Over time, you would probably set them as env consts:
export TWINE_USERNAME=__token__
export TWINE_PASSWORD=your_actual_token_here
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
---

##Step 9 — Install from TestPyPI to Verify

```bash
pip install --index-url https://test.pypi.org/simple/ your-package-name
your-app
```

---