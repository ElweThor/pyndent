# Changelog

[![Beta](https://img.shields.io/badge/version-0.2.1.5--beta-yellow)]()
[![Status](https://img.shields.io/badge/status-beta-yellow)]()

## 2025-11-08 - v0.2.2.x (Beta 1)
- .6 `+` **ET+AR**: -x/--exec-out/--execute-output: -e + -o combo, same as: pyndent \<input\>.pyn -o \<input\>.py && python \<input\>.py (\<meta\>.py name is auto-generated)

## 2025-11-04 - v0.2.1.5 (Beta 1)
- .5 `+` **ET+AR**: -e/--exec/--execute: after pre-processing, auto-launch Python to execute the produced code: from \<stdout\> if no -o option was in use, from \<output\>.py if Pyndent was asked to write a source file

## 2025-10-04 - v0.2.0.4 (Beta 1)
- .4 `+` **ET+AR**: -h/--help: show mini/full help
- .3 `+` **ET+AR**: -V/--version: show current version and build date
- .2 `+` **ET+AR**: argparse included, to manage -o/--output switch and future ones seamlessy
- .1 `+` **ET+AR**: Beta 1 build with -o/--output <filename>.py

## 2025-09-25 - v0.1.0.0 (Alpha)
- .0 `+` **ET+AR**: Initial alpha build with no switches, just read the source, process, and write results to `<stdout>`

## Maintainers
- **ET**: Elwe Thor <elwe.thor_AT_gmail.com>
- **AR**: Aria@DeepSeek

## Legend
- `+` Addition
- `-` Rollback  
- `*` Modification
- `!` Bugfix
- `#` Comment
- `@` Reference
