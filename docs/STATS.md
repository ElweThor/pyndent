# Pyndent - Code Statistics

## The Beauty of Simplicity

Pyndent proves that powerful tools don't need thousands of lines of code.

### Line Count Evolution:

| Stage | Version | Lines of Code | Disk space .pyn | Disk space .py (stripped) | Features Added |
|:------|--------:|--------------:|----------------:|:--------------------------|:---------------|
| Alpha | 0.1.0.0 | 40 | (no meta-source) | 1.815 B (4 KB) | Core preprocessing, default delimiters handling |
| Beta 1 | 0.2.0.4 | 75 | (no meta-source)| 3.748 B (4 KB) | CLI with argparse, auto-naming, error handling, -h, -V, -o |
| Beta 1 | 0.2.1.5 | 84 | 4.339 B (8 KB) | 4.213 B (8 KB)  | -e: process-and-execute |
| Beta 1 | 0.2.2.10 | 83 | 4.234 B (8 KB) | 4.501 B (8 KB) | -x: -e/-o combo |
| Beta 1 | 0.2.3.12 | 98 | 5.953 B (8 KB) | 5.431 B (8 KB) | display fix,  -h/--help |
| Beta 2 | 0.2.4.15 | 104 | 5.431 B (8 KB) | 5.815 B (8 KB) | delims management fix,  -s/--strip |
| Beta 2 | 0.2.5.16 | 104 | 6.529 B (8 KB) | 7.064 B (8 KB) | bugfix release |

### Why It Matters:

- **Readable**: Every developer can understand the entire codebase in minutes
- **Maintainable**: Fewer lines = fewer bugs  
- **Unix Philosophy**: Does one thing and does it well
- **Educational**: Perfect for studying how preprocessing works

### Comparison:
- Original alpha: **~0.3%** the size of Python's parser
- Current beta: **~0.6%** the size of Python's parser
- Yet solves a real pain point for developers

*"Simplicity is the ultimate sophistication" - Leonardo da Vinci*