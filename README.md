# pythone

python + one 代码库 - A reusable Python utility library

## Installation

You can install this package directly from GitHub:

```bash
pip install git+https://github.com/USERNAME/pythone.git
```

To install a specific branch:

```bash
pip install git+https://github.com/USERNAME/pythone.git@dev
```

To install a specific version tag:

```bash
pip install git+https://github.com/USERNAME/pythone.git@v0.1.0
```

## Usage

After installation, you can import and use the utilities:

```python
from pythone.utils import example_function, safe_divide

# Example 1: Using example_function
result = example_function("hello")
print(result)  # Output: Hello, from pythone!

# Example 2: Safe division
result = safe_divide(10, 2)
print(result)  # Output: 5.0

result = safe_divide(10, 0, default=-1)
print(result)  # Output: -1
```

## Development

To set up for local development:

```bash
# Clone the repository
git clone https://github.com/USERNAME/pythone.git
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
│       └── utils.py
├── pyproject.toml
├── README.md
└── LICENSE
```

## Requirements

- Python 3.8 or higher

## License

MIT License
