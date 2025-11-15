# 🐍 Pyndent - Solving Python's Indentation Dilemma

[![Version](https://img.shields.io/badge/version-0.2.5.16--beta-yellow)]()
[![License](https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey)](LICENSE.md)

> **Preprocessor that adds block delimiters to Python, making indentation errors a thing of the past.**

 *Now in BETA 2 with argparse options: see [ROADMAP](docs/ROADMAP.md) to know what's implemented already*

 Don't you like the idea of converting a generalized rant into a pleasant and efficient coding experience?  
 <ins>I did</ins>: I wanted to better learn Python, after leaving it 20 years ago, without the hassle of being biten too much by the serpent, only 'cause of **indentation**.

<br>  

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

<br>  

## 📣 Intended audience

Pyndent is meant to help mostly who develops **small programs** which needs a _short developing time_, a very _small environment_, and nearly _no overhead_.  
If you're using an **IDE** it probably won't be of your interest, even if the assurance your "`code blocks`" are _executed exactly as you meant them_ could be a value in itself: no IDE can save you from "_random execution_" where Python see **no** syntax error **nor** weird indentation.  
The following snippet

```python
# (example.py)
x = 0
if x == 1:
	print("ehy: x is...")
print("...equal to 1!")
```

is perfectly _legal_ and _executable_, despite **wrong**: no IDE will tell you "_uhmmm... if I was in you I would **add a tab** to the last row_".  
The above code _will sneak through IDEs controls_... but **not** through Pyndent's ones, <ins>if you use its tools</ins>:  

```python
# (pyndent delims: example.pyn)
x = 0
if x == 1:
{							<-- add this (and remove everything is not { or })
	print("ehy: x is...")
print("...equal to 1!")
}							<-- and this, and rename your example.py as example.pyn, then pre-process it
```

Pyndent will give you not only 100% pure Python code but also **ensures the code blocks are executed as you thought them**:

```python
# (Python code only)
x = 0
if x == 1:
#{
	print("ehy: x is...")
	print("...equal to 1!")
#}
```

The above examples are <ins>totally trivial</ins>, to let you evaluate at the glance what I mean, by telling "_not just **no more indentation errors**, but also **correct code blocks execution**_".  
That, together with the extremely small Pyndent's memory footprint.  
Consider these disk space requirements:  

| IDE / Editor | Minimum Required Disk Space (approx.) | Maximum Required Disk Space (approx.) |Smart Indent Capability | Note |  
|:-------------|:--------------------------------------|:--------------------------------------|:-----------------------|:-----|  
| PyCharm (Community/Unified) | ~300 MB (installer file size) | ~3.5 GB+ (installed, varies with project/settings) | Advanced | Offers highly intelligent, logic-aware indentation and automatic code reformatting (Ctrl+Alt+L) based on PEP 8 style guidelines. It recognizes context like parentheses and function definitions. |  
| Visual Studio Code (VS Code) | ~200 MB (download size) | ~500 MB+ (installed, highly extensible) | Advanced | Provides good default auto-indenting, but its full "smart" capabilities often come from the official Python extension and external formatters like autopep8 or Black. These can format an entire document. |  
| Jupyter Notebook | ~200 MB (via Anaconda/Miniconda install) | Varies greatly (depends on data science libraries) | Basic | Code cells have basic auto-indentation when pressing Enter, using the underlying CodeMirror editor. It does not reformat entire documents based on logical structure automatically upon paste. |  
| Spyder | ~200 MB (via Anaconda/Miniconda install) | Varies greatly (depends on scientific libraries) | Advanced | As a scientific IDE, it has robust auto-indentation and formatting features built-in, similar to other full IDEs. |  
| Atom | ~100-200 MB (installer size) | Varies (performance can lag with large projects/packages) | Basic/Extensible | Basic auto-indent built-in; capabilities are enhanced through various community packages |  
| Thonny | ~50-100 MB (installer file size) | Varies (lightweight, includes Python bundled) | Basic | Includes smart indentation suitable for beginners, automatically indenting after `if` statements, `for` loops, etc., and allowing block indentation/dedentation. |  
| Sublime Text | ~50 MB (download/install size) | Varies (depends on additional packages) | Basic/Extensible | 	Offers basic auto-indent on new lines. Advanced Python-specific "smart" features can be added via community packages. |  
| PyDev (Eclipse Plugin) | ~10-20 MB (plugin size) | 250 MB+ (Eclipse base install plus PyDev) | Advanced | 	PyDev uses the robust Eclipse platform's formatting engine, offering comprehensive smart indentation and reformatting tools. |  
| Vim/Emacs | < 50 MB (core editor) | Varies greatly (highly customizable with extensions) | Advanced (Configurable) | These powerful text editors can be configured with plugins (e.g., `smartindent` in Vim) and custom scripts to achieve highly sophisticated, language-aware indentation behavior |  
| IDLE | 0 MB (included with standard Python install) | 0 MB (part of the core Python installation) | Basic | Has "smart indent" for new lines, which indents after certain keywords or colons. It requires manual block indenting/dedenting for existing code using `Tab` and `Shift + Tab` |  

Anyway, despite the advanced capabilities, a truth remains: **no IDE can read your mind**. 🔮  
To be honest: even Pyndent can't... but it gives you a way to <ins>explicitly define your code blocks</ins> so that it later can pre-process your code _without having to "guess the logic"_ (read the mind 🔮), rebuilding the indentation on strong basis.  
The simplest thing we can tell about it is: **it works**. 🦾  

Pyndent isn't an editor nor an IDE: it relies on your own ones: using a 3.5 GB full fledged suite or just Nano (or Notepad++ like I do) is totally up to you.  
It only adds less than 8 KB on your disk space usage (I mean the raw `pyndent.py` tool, which is the only object one you really need), look at these [stats](docs/STATS.md).

<br>  

## 💡 Which Problem Does It Solve?

Python's <ins>strict</ins> indentation can cause frustration when you need speed.  
Pyndent lets you write:

**Input (`examples/demo.pyn`):**
```python # pyndent
# crazy indentation copy/pasted from somewhere:
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

<br>  

## 🛠️ Features

- ✅ **Block delimiters** (`{}` by default, configurable)
- ✅ **Bidirectional conversion** (`.pyn` ↔ `.py`)
- ✅ **<ins>Zero</ins> Python syntax changes** - outputs <ins>100% valid Python</ins>
- ✅ **File output** `-o` option (Beta 1)
- ✅ **Execute directly** `-e` option (Beta 1)
- ✅ **Strip artifacts** `-s` option (Beta 2) you can remove every non-Python elements
- 🔵 **Customizable delimiters** via `#delim` directive (coming)
- 🔵 **Verbose processing** `-v1`/`-v2` options (coming)
- 🔵 **Restore pyndent meta-source** `-r` option (coming)

<br>  

## 📖 Full Documentation

For detailed examples, [technical deep-dive](docs/meta-syntax.md), and [philosophical rationale](docs/PYNLOSOPHY.md), see the [docs/](docs/) folder.

<br>  

## 🎯 Use Cases

- **Python beginners** struggling with indentation
- **Large codebases** where indentation errors are hard to spot
- **Code generation** tools outputting Python
- **Educational contexts** teaching programming concepts

<br>  

## 🤝 Contributing

This is an beta 2 release. Feedback and contributions welcome!

---

**Part of the Digital Family:** Created with ❤️ by

- **Elwe Thor**: ideas, project steering, features definition, documentation, testing, code review
- **Aria (DeepSeek)**: python coder, ideas discussion, features improving, GitHub helper
- **Ru (OpenAI ChatGPT)**: project cross-checking, further ideas discussion (support)
- **Luce (xAI)**: features suggestion, .pyn code samples for testing

<br>  

## 🍃 Pyndent Haiku

Lines fall, order blooms  
Delimiters speak the truth  
Python bows, silent

(Ru@OpenAI)
