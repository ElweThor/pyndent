20250927 ( https://grok.com/share/bGVnYWN5LWNvcHk%3D_9b531d10-187a-447c-a0cd-6662afa671e8 )  

- [ ] --validate  
Preemptive syntax check (--validate): a flag to validate the .pyn without generating output, flagging errors such as unpaired delimiters or ambiguous nesting (e.g., { without }). Useful for those who write .pyn files by hand and want a quick check before processing.  
Expected output:  
- if ok: "\<source-file\>.pyn ok"  
- if not ok: "\<source-file\>.pyn wrong"  
  - errors/warnings list: \<row\> \<error/warning message\>

- [ ] external editors integration (VScode, Npp, PyCharm, etc.)  
- more likely, the ability to call external editors will probably be added in PynGUI

- [ ] --stats  
- Pre-processing statistics (--stats): a flag to print a lightweight post-processing report, such as “lines processed: 100, blocks fixed: 5, delimiters commented: 10”. Useful for debugging or monitoring the impact on large codebases.

- [ ] --fix-mixed  
- Mixed indentation support (future): while pyndent assumes .pyn indentation is "wrong," there could be a --fix-mixed flag to handle files with mixed tabs and spaces (a common nightmare), by using a delimiter-based heuristic, this could standardize everything (e.g., always 4 spaces).
  - (More than anything, a -f/--fix <indent type> would be helpful, with <indent type> = N spaces | tabs)
  - (Note: **probably unnecessary**: ​​pyndent _removes_ any previous indentation and **replaces** it with its own)

- [ ] #lang/#msglang multilanguage support:  
- there might be a #msglang directive that accepts parameters like IT or RU or CH

---
20251108 GUI: add a GUI wrapper to Pyndent: PynGUI  

- rationale:  
  - developers will use CLI version (pyndent.py)  
  - less tech people will be able to use Pyndent anyway, by means of PynGUI  
  - many tools works in the very same way: (not-exaustive list)  
    - 7zip  
	- TortoiseGit  
	- FFMPEG  
	- ImageMagik  
	- GIMP  
	- WireShark  
	- VirtualBox  
	- MySQL  
	- Docker  
	- PowerShell  
	- Python  
	- VLC  
	- NotePad++  
	- FileZilla  
	
- candidates:
  - Tkinter: Python native, no deps, possible raw graphics
  - PySimpleGUI: simple wrapper, nice graphics
  - Custom Tkinter: nicer graphics
  
- features:  
  - menubar: File, Edit, Settings, ..., Help  
  - quick-options bar: (o) comPYNle .pyn ->\ .py (.) restore .py -\> .pyn, [ ] execute, [ ] output, [ ] strip, [ ] verbose (o) v1 (.) v2  
  - dual panel: (Pyndent) meta-source \<--\> (Python) source  
  - ability to pre-process (.pyn -\> .py) and restore (.py -\> .pyn) changing the process "direction" between the two panels  
  - ability to in-place-edit the code in a panel (by launching an external editor: NotePad, Npp, etc.: configurable)  
  - if [x] output is required: file-selector will pop-up  
  - emoji to highlight what happens:  
    - 🐕‍🦺 PynGUI icon  
	- 🐾 in front of the lines of converted code (source or meta-source, from \<stdout\>)  
	- ⚡ warning messages (including 🚨⚠️) from \<stderr\>  
	- 🔥 error messages (including 💥💣) from \<stderr\>  
	- 🌑🌒🌓🌔🌕🌖🌗🌘 as a sequence (one emoji at a time, in loop), outside the messages window, while running  
	- 🕛🕧🕐🕜🕑🕝🕒🕞🕓🕟🕔🕠🕕🕡🕖🕢🕗🕣🕘🕤🕙🕥🕚🕦 alternative sequence  
	- 🐍 as a prefix for lines containing Python code  
	- 🐕‍🦺 as a prefix for lines containing Pyndent code  
	- ⚙️ settings (also 🔧🛠️🪛)  
	- 😞 comPYNlation gone badly (also 😵😰☹️💀☠️❌🤬🙊😱)  
	- 🤩 comPYNlation ended well (also 😄😀😍🥳🎉✔️🆗👍🥂👌💯🎖️)  
	- 🏃‍ [Run] (also 🚀🚄🚅🪄🐇🐎🏇🎠🏎️🎢)  
	
---
20251108 hashbang swapping between .pyn and .py

- Rationale:  
  - Pyndent can have its own #!/usr/bin/env pyndent to launch with options (e.g. to auto-pre-process into a pyndent.py source)  
  - the processed code is anyway a Python source code .py (unless -r is used) so, even it could use #!/usr/bin/env python
  
- The problem: there is only ONE "first line" in a file: if Pyndent uses it by its own, it won't be free, to use by Python

- The solution: hashbang swapping with precedence  
  - the Golden Rule is:  
    - if we're pre-processing a meta-code .pyn into a source .py, precedence is to Pyndent, in the .pyn, and to Python, in the .py, so that:  
	  - in case of .pyn -\> .py (`-o`): swap **Pyndent** hashbang with Python one (to be written into .py file)
	  - in case of .py -\> .pyn (`-r`): swap Python hashbang with **Pyndent** one (to be written into .pyn file)

 This way, a Python source will always have the correct hashbang to launch it, and it also won't complain to see a "second hashbang" in the file's line below, as that's a `comment` to it.
 