## 2025-11-14 - v0.2.4.12 (Beta)
.12 `+` **ET/AR**: -o/--output option: output to file, with automatic filename (format: yyyymmdd-hhmm_stats.txt) if not explicitly given
.11 `+` **ET/AR**: -j/-json option: JSON validation
.10 `+` **ET/AR**: -h/--help option: help
.9 `+` **ET/AR**: -V/--version option: versioning

## 2025-11-07 - v0.2.3.8 (Beta)
.8 `!` **ET/AR**: parser fix: memories without priority won't receive "medium" default more: default is now "missing", to immediately see them in the report  

## 2025-11-05 - v0.2.2.7 (Beta)
.7 `+` **ET/AR**: stats double metrics: 1st metric (green/orange/red) on totals, 2nd metric on active memories only  
.6 `*` **ET/AR**: stats display fixed: priority table have different priorities separated, for better display  
.5 `*` **ET/AR**: stats display fixed: table's numbers are now zero-left-padded  

## 2025-11-05 - v0.2.1.4 (Beta)
.4 `*` **ET/AR**: stats display fixed: more meaningful, percentages formats adjusted, Active memory percentage recalc towards grandototal (max_entries)  

## 2025-11-05 - v0.2.0.3 (Beta)
.3 `*` **ET/AR**: priority_system better check (with JSON format fix) and example added, for JSONs lacking the section  
.2 `*` **ET/AR**: priority dynamic management, by using a priority_system entri in JSON meta where to define a priority scale (enum)  

## 2025-11-05 - v0.1.1.1 (Alpha)
.1 `*` **ET**: tabs fixed by means of pyndent  

## 2025-11-05 - v0.1.0.0 (Alpha)
.0 `+` **ET+AR**: Initial alpha build, just read the source file, process, and write results to `<stdout>`  

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
