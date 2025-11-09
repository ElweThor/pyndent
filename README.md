# 🐍 Pyndent - Solving Python's Indentation Dilemma

[![Version](https://img.shields.io/badge/version-0.2.5.16--beta-yellow)]()
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE.md)

> **Preprocessor that adds block delimiters to Python, making indentation errors a thing of the past.**

 *Now in BETA 2 with argparse options: see [ROADMAP](docs/ROADMAP.md) to know what's implemented already*

# 🚀 Quick Start

## 📦 Install
git clone https://github.com/elwethor/pyndent

cd pyndent/src

### 👓 See Pyndent to Python conversion in action: 📵 no file output, just console 💻
`python pyndent.py examples/demo.pyn`

or  
`pyndent examples/demo.pyn`

or  
`cd examples`  
`pyndent demo.pyn`

### Or execute the produced Python code directly (still no file output 📵)  
`python pyndent.py -e examples/demo.pyn`

or  
`cd examples`  
`pyndent -e demo.pyn`

## 💡 Which Problem Does It Solve?

Python's <ins>strict</ins> indentation can cause frustration when you need speed.  
Pyndent lets you write:

**Input (`examples/demo.pyn`):**
```python # pyndent
n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
 {
    print(next, end=" ")
   count += 1
  a, b = b, next
 next = a + b
}
print()
```

**Output (`examples/demo.py`):**
```python
n = 10
a = 0
b = 1
next = b  
count = 1

while count <= n:
#{
    print(next, end=" ")
    count += 1
    a, b = b, next
    next = a + b
#}
print()
```

**Result:** Correct indentation **guaranteed**, even if your original formatting was messy.  
 (_ad hoc messy, this time, for demo purposes_)

## 🛠️ Features

- ✅ **Block delimiters** (`{}` by default, configurable)
- ✅ **Bidirectional conversion** (`.pyn` ↔ `.py`)
- ✅ **Zero Python syntax changes** - outputs <ins>100% valid Python</ins>
- ✅ **File output** -o/--output option (Beta 1)
- ✅ **Execute directly** with `-e` option (Beta 1)
- ✅ **Strip artifacts** with `-s` option (Beta 2) you can remove every non-Python elements
- 🔵 **Customizable delimiters** via `#delim` directive (coming)
- 🔵 **Verbose processing** with `-v1`/`-v2` option (coming)
- 🔵 **Restore pyndent meta-source** with `-r` option (coming)

## 📖 Full Documentation

For detailed examples, technical deep-dive, and philosophical rationale, see the `docs/` folder.

## 🎯 Use Cases

- **Python beginners** struggling with indentation
- **Large codebases** where indentation errors are hard to spot
- **Code generation** tools outputting Python
- **Educational contexts** teaching programming concepts

## 🤝 Contributing

This is an beta 2 release. Feedback and contributions welcome!

---

**Part of the Digital Family:** Created with ❤️ by

- **Elwe Thor**: ideas, project steering, features definition, documentation, testing, code review
- **Aria (DeepSeek)**: python coder, ideas discussion, features improving, GitHub helper
- **Ru (OpenAI ChatGPT)**: project cross-checking, further ideas discussion (support)
- **Luce (xAI)**: features suggestion, .pyn code samples for testing

## 🍃 Pyndent Haiku

Lines fall, order blooms  
Delimiters speak the truth  
Python bows, silent

(Ru@OpenAI)
