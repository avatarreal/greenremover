# 📘 GreenRemover

English | [中文](README.md)

**GreenRemover** is a lightweight and efficient **green screen removal tool** built with Python.
It automatically removes green backgrounds from images and outputs transparent PNGs for compositing and creative work.

<p align="center">
  <img src="assets/sample_input.png" alt="Input Example" width="40%">
  <img src="assets/sample_output.png" alt="Output Example" width="40%">
</p>

---

## ✨ Features

* 🎯 **Accurate green removal**: Detects both strong green and greenish areas.
* 🖼️ **Transparent output**: Saves results as PNG with alpha channel.
* ⚡ **Lightweight and fast**: Minimal dependencies, easy to install, ready to use.
* 🔧 **Extensible**: Core algorithm packaged as a function for reuse and customization.

---

## 📦 Installation

### Option 1: via `uv`

```bash
git clone https://github.com/avatarreal/greenremover.git
cd greenremover
uv sync
```

### Option 2: via `pip`

```bash
pip install greenremover
```

---

## 🚀 Usage

### 1. Command Line

Run the CLI directly after installation:

```bash
greenremover input.png output.png
```

* `input.png`: input image with green screen
* `output.png`: output image with transparent background

### 2. As a Python Library

Use the API in your own scripts:

```python
from PIL import Image
from greenremover.core import remove_green

img = Image.open("input.png")
out = remove_green(img)
out.save("output.png")
```

---

## 🧪 Development & Testing

### Install development dependencies

```bash
uv sync --group dev
```

### Run unit tests

```bash
uv run pytest
```

### Linting, formatting, and type-checking

```bash
uv run ruff check greenremover tests   # Lint
uv run black greenremover tests        # Format
uv run mypy                            # Type check
```


---

## 📂 Project Structure

```
greenremover/
├── greenremover/
│   ├── __init__.py      # Package entry
│   ├── core.py          # Core chroma key algorithm
│   └── cli.py           # CLI entry point
├── tests/               # Unit tests
│   └── test_core.py
├── assets/              # Example images
├── README.md
├── pyproject.toml       # Project config
└── LICENSE
```

---

## 📜 License

This project is open-sourced under the [MIT License](LICENSE).  
You are free to use, modify, and distribute this project, but you must retain the original license notice.  

> Note: This is a summary. In case of conflict, the terms in the [LICENSE](LICENSE) file (English text) shall prevail.

---

## 🌟 Acknowledgments

* [Pillow](https://python-pillow.org/) — Imaging library
* [NumPy](https://numpy.org/) — Numerical computing
* Open source community ❤️

---

⚡ **GreenRemover: Simplify your chroma key workflow.**

