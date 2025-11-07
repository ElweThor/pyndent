# AI Memory_stats development roadmap

## Alpha
- [x] first alpha build, native Pyhton code

## Beta
- [x] beta build, Pyndent meta-code, "core" to extract and visualize statistics on a fixed name JSON file: memory.json

## v1.x
- [ ] v1 with
- [ ] beta: add Rank and Target to --analyze feature, to produce a "proposal listing" for when we need to optimize
- [ ] ability to read whichever \<path\>/\<file\>.json
- [ ] comfortable options:

### Stats output
- [ ] -s --show-all-stats &emsp;&emsp;&nbsp;&nbsp;&nbsp; show the whole stats: initial summary + memories table: default is "summary only"  
- [ ] -t --show-table &emsp;&emsp; show memories table only  

| Short | Long Opt | Section | Description |
|-------|----------|---------|-------------|
| -s | --show-all-stats | Stats output | show the whole stats: initial summary + memories table: default is "summary only" |
| -t | --show-table | Stats output | show memories table only |
| -a | --analyze <priority> | Memory Analysis | executes a table re-scan, selecting <priority> only (or every memory if <priority> = ALL) to give a Rank to any single memory, promoting it for the optimization/prune: the higher the Rank, the more likely the memory will be optimized/pruned: 1 = high, N = low (see analyze_report for display details). The analysis report should contain Target column also, to see which memories fall into the target range and which ones don't. |
| -o | --output <filename> | File output | write stats report to disk (plain text) into <filename> |
| -f | --force | File output | forces the tool to overwrite a stats report if one with the same name is found on disk already and -o switch is used |
| -j | --validate-json | JSON management| check the input JSON file, to see if it's wrong somewhere, preventing stats extraction |
| -r | --repair-json | JSON management| try to auto-fix the JSON |
| -v | --verbose | Utility | tell us how things are working (like a log, to <stderr>) |
| -h | --help | Utility | -h gives simple usage, while --help gives extended help on syntax and parameters |
| -V | --version | Utility | shows current version |

### Memory Analysis
- [ ] -a --analyze <priority> executes a table re-scan, selecting <priority> only (or every memory if <priority> = ALL) to give a Rank to any single memory, promoting it for the optimization/prune: the higher the Rank, the more likely the memory will be optimized/pruned: 1 = high, N = low (see analyze_report for display details). The analysis report should contain Target column also, to see which memories fall into the target range and which ones don't.

### File output
- [ ] -o --output <filename> &emsp;&emsp;&nbsp;&nbsp;&nbsp; write stats report to disk (plain text) into <filename>  
- [ ] -f --force &emsp;&emsp;&emsp;&emsp; forces the tool to overwrite a stats report if one with the same name is found on disk already and -o switch is used  

### JSON management
- [ ] -j --validate-json &emsp; check the input JSON file, to see if it's wrong somewhere, preventing stats extraction  
- [ ] -r --repair-json &emsp;&nbsp;&nbsp; try to auto-fix the JSON  

### Utility
- [ ] -v --verbose &emsp;&emsp;	tell us how things are working (like a log, to <stderr>)  
- [ ] -h --help	&emsp;&emsp;&emsp;&nbsp; -h gives simple usage, while --help gives extended help on syntax and parameters  
- [ ] -V --version &emsp;&emsp;	shows current version  
