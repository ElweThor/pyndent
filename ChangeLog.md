# Changelog

[![Beta](https://img.shields.io/badge/version-0.2.4.15--beta-yellow)]()
[![Status](https://img.shields.io/badge/status-beta-yellow)]()

## 2025-11-09 - v0.2.4.15 (Beta 2)
- .15 `*` **ET+AR**: delimiters are no more hardcoded (only defaults are)
- .14 `!` **ET+AR**: fixed delimiters parsing: pyndent was considering starting spaces/tabs only but Golden Rule tells "every"
- .13 `+` **ET+AR**: -s/--strip/--strip-delims removes every Pyndent meta-code (commented) element from the Python source

## 2025-11-08 - v0.2.3.12 (Beta 1)
- .12 `*` **ET+AR**: -h show a short help (usage), --help: show a full help
- .11 `!` **ET+AR**: pyndent was showing a processed code printout even when `-e`, `-o` or `-x` was given: by default it should show the code when no option is given

## 2025-11-08 - v0.2.2.10 (Beta 1)
- .10 `*` **ET+AR**: Auto-naming output file for `-x` if no explicit output filename is given
- .9 `*` **ET+AR**: Improved help text for clarity, about mutual exclusive options
- .8 `+` **ET+AR**: Mutual exclusivity control between `-x` and `-e`/`-o`: if they're specified together, error exit
- .7 `+` **ET+AR**: `-f/--force` (force overwrite) 
- .6 `+` **ET+AR**: `-x/--execout/--execute-output` combo (output write + execute), same as: pyndent \<input\>.pyn -o \<input\>.py && python \<input\>.py (\<meta\>.py name is auto-generated)

**Patchlevel suggerito:** `0.2.2.5` (5 modifiche principali)



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
