#!/usr/bin/env python
#
# PYthon INdent: a reindent pre-processor tool for Python 
# (C)2025 by Elwe Thor - Aria@DeepSeek 
# LICENSE: CC BY-NC-SA 4.0 (see LICENSE file for details)
#
"""
Pyndent - Python preprocessor with block delimiters
Beta 1 v0.2.0.4 - 20251004
"""

import sys
import os
import argparse

# Version info
VERSION = "0.2.0.4"
RELEASE = "Beta 1"
BUILD_DATE = "20251004"
LICENSE_INFO = "see LICENSE.md"

def pyndent_process(source_lines):
    """
    Process .pyn source lines into properly indented Python code
    """
    indent_level = 0
    output_lines = []
    delimiter_open = '{'
    delimiter_close = '}'
    
    for line_num, line in enumerate(source_lines, 1):
        stripped = line.strip()
        
        # Handle opening delimiter
        if stripped == delimiter_open:
            output_lines.append('    ' * indent_level + '#' + delimiter_open)
            indent_level += 1
            continue
            
        # Handle closing delimiter  
        if stripped == delimiter_close:
            if indent_level > 0:
                indent_level -= 1
            output_lines.append('    ' * indent_level + '#' + delimiter_close)
            continue
            
        # Regular code line - reindent from scratch
        if stripped:  # Non-empty line
            output_lines.append('    ' * indent_level + line.strip())
        else:
            output_lines.append('')
    
    return output_lines

def main():
    parser = argparse.ArgumentParser(
        description='Pyndent - Python preprocessor with block delimiters',
        epilog=f'Pyndent {VERSION} {RELEASE} ({BUILD_DATE}) - {LICENSE_INFO}'
    )
    
    parser.add_argument('input_file', nargs='?', help='Input .pyn file to process')
    parser.add_argument('-o', '--output', dest='output_file', 
                       nargs='?', const='AUTO',  # here is the magic!
                       help='Output .py file (use without value for auto-name, default: stdout)')
    parser.add_argument('-V', '--version', action='version',
                       version=f'Pyndent {VERSION} {RELEASE} ({BUILD_DATE})')
    
    args = parser.parse_args()
    
    # If no input file is given, show mini-help and version info
    if not args.input_file:
        parser.print_help()
        sys.exit(1)
    
    # Read input file
    try:
        with open(args.input_file, 'r', encoding='utf-8') as f:
            input_lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: Input file '{args.input_file}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Process the code
    try:
        output_lines = pyndent_process(input_lines)
    except Exception as e:
        print(f"Error processing file: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Write output
    try:
        if args.output_file:
            if args.output_file == 'AUTO':
                # Auto-generate output filename: input.pyn → input.py
                output_file = os.path.splitext(args.input_file)[0] + '.py'
            else:
                output_file = args.output_file
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(output_lines))
            print(f"Processed code written to: {output_file}", file=sys.stderr)
        else:
            # Default: stdout
            print('\n'.join(output_lines))
    except Exception as e:
        print(f"Error writing output: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
