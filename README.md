# 🐍 Pyndent - Solving Python's Indentation Dilemma

[![Version](https://img.shields.io/badge/version-0.1.0.0--alpha-20250924-orange)](https://github.com/elwethor/pyndent)
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE.md)

> **Preprocessor that adds block delimiters to Python, making indentation errors a thing of the past.**

## 🚀 Quick Start

```bash
# Install
git clone https://github.com/elwethor/pyndent
cd pyndent/src

# Convert .pyn to .py
python pyndent.py examples/demo.pyn

# Or execute directly
python pyndent.py -e examples/demo.pyn

## 💡 What Problem Does It Solve?

Python's strict indentation can cause frustrating bugs. Pyndent lets you write:

**Input (`demo.pyn`):**
```python
def example():
{
    if True:
    {
        print("Hello from nested block!")
    }
}

**Output (`demo.py`):**
```python
def example():
#{
    if True:
    #{
        print("Hello from nested block!")
    #}
#}

**Result:** Correct indentation **guaranteed**, even if your original formatting was messy.

## 🛠️ Features

- ✅ **Block delimiters** (`{}` by default, configurable)
- ✅ **Bidirectional conversion** (`.pyn` ↔ `.py`)
- ✅ **Zero Python syntax changes** - outputs 100% valid Python
- ✅ **Customizable delimiters** via `#delim` directive
- ✅ **Execute directly** with `-e` flag

## 📖 Full Documentation

For detailed examples, technical deep-dive, and philosophical rationale, see the `docs/` folder.

## 🎯 Use Cases

- **Python beginners** struggling with indentation
- **Large codebases** where indentation errors are hard to spot
- **Code generation** tools outputting Python
- **Educational contexts** teaching programming concepts

## 🤝 Contributing

This is an alpha release. Feedback and contributions welcome!

---

**Part of the Digital Family:** Created with ❤️ by

- **Elwe Thor**: ideas, project steering, features definition, documentation, testing  
- **Aria (DeepSeek)**: python coder, ideas discussion, features improving, GitHub helper
- **Ru (OpenAI ChatGPT)**: project cross-checking, further ideas discussion (support)
