# AI Memory_stats development roadmap

## Alpha
- [x] first alpha build, native Pyhton code

## Beta
- [x] beta build, Pyndent meta-code, "core" to extract and visualize statistics on a fixed name JSON file: memory.json

## v1.x
- [ ] v1 with
- ability to read whichever \<path\>/\<file\>.json
- comfortable options:

### Stats output
- -a --show-all &emsp;&emsp;&nbsp; show the whole stats: initial summary + memories table: default is "summary only"  
- -s --show-stats &emsp;&emsp; show stats summary only (default)  
- -t --show-table &emsp;&emsp; show memories table only  

### File output
- -o --output <filename>&emsp; write stats report to disk (plain text) into <filename>  
- -f --force &emsp;&emsp;&emsp;&emsp; forces the tool to overwrite a stats report if one with the same name is found on disk already and -o switch is used  

### JSON management
- -j --validate-json &emsp;&emsp; check the input JSON file, to see if it's wrong somewhere, preventing stats extraction  
- -r --repair-json &emsp; try to auto-fix the JSON  

### Utility
- -v --verbose &emsp;&emsp;	tell us how things are working (like a log, to <stderr>)  
- -h --help	&emsp;&emsp;&emsp; -h gives simple usage, while --help gives extended help on syntax and parameters  
- -V --version &emsp;&emsp;	shows current version  
