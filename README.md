# pythone

python + one 代码库 - A reusable Python utility library

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/lixianmin/pythone.git
pip install git+https://github.com/lixianmin/pythone.git@dev
pip install git+https://github.com/lixianmin/pythone.git@v0.1.0
```

## Usage

After installation, you can import and use the utilities:

```python
from pythone.logo import logo

logo.info(f"hello")
```

## Development

To set up for local development:

```bash
# Clone the repository
git clone https://github.com/lixianmin/pythone.git
cd pythone

# Install in editable mode
pip install -e .
```

## Project Structure

```
pythone/
├── src/
│   └── pythone/
│       ├── __init__.py
│       └── logo.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Requirements

- Python 3.8 or higher

## License

Apache License
