#!/usr/bin/env python3
#
# PYthon INdent: a reindent pre-processor tool for Python 
# Alpha 0.1 - bare code re-indentation
#
# (C)2025 by Elwe Thor - Aria@DeepSeek 
# LICENSE: CC BY-NC-SA 4.0 (see LICENSE file for details)
#
import sys

def is_brace_line(line):
    """True if the line contains a curly brace _only_"""
    stripped = line.strip()
    return stripped in ['{', '}']

def pyndent_process(source):
    output = []
    indent_level = 0
    
    for line in source.split('\n'):
        stripped = line.strip()
        
        if stripped == '{':
            output.append('\t' * indent_level + '#{')
            indent_level += 1
        elif stripped == '}':
            if indent_level == 0:
                raise SyntaxError("unexpected '}' without matching '{'")
            indent_level -= 1
            output.append('\t' * indent_level + '#}')
        else:
            output.append('\t' * indent_level + line.lstrip())
    
    if indent_level > 0:
        raise SyntaxError(f"unbalanced delimiters: {indent_level}")
    
    return '\n'.join(output)

def main():
    if len(sys.argv) != 2:
        print("Usage: pyndent input.pyn")
        sys.exit(2)
    
    input_file = sys.argv[1]
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            source = f.read()
        
        result = pyndent_process(source)
        print(result)  # stdout!
        sys.exit(0)
        
    except FileNotFoundError:
        print(f"Input file not found: {input_file}")
        sys.exit(2)
    except SyntaxError as e:
        print(f"Syntax error in .pyn file: {e}")
        sys.exit(2)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(3)

if __name__ == '__main__':
    main()
