
 # Meta Syntax

 - [Pre-Processor Directives](#preprocdir) ([examples](#preprocdirxamp))
 - [Hashbang management](#hashbang)
 - [Syntax scheme](#syntax)
 - [Options](#options)
 - [Options in detail](#optdetails)
 - [Obsoletes](#obsol)

<br>

 ## Pre-Processor Directives<a name="preprocdir"></a>
 
 Pyndent code syntax is <ins>**100% pure Python**</ins>, as it must be. The _meta-syntax_, used by Pyndent pre-processor to rewrite the (Python) code indentation, uses a couple of "_**code-block delimiters**_" (by default C-like ones: "`{`" and "`}`", but they can be customized) and a few _**meta-statement**_ (AKA _pre-processor directives_):
 
 **#delim \<start_delimiter\> \<stop_delimiter\>**
 
 where **`<start_delimiter>`** and **`<stop_delimiter>`** can be _single characters_ (usually in pairs: "`{`" "`}`", "`<`" "`>`", "`[`" "`]`", but they can be _litterally **everything**_, as far as you follow Pyndent meta-syntax: "`/`" "`\`", "`->`" "`<-`", etc.) or even _single **words**_ (e.g. "`begin`" "`end`", "`block_start`" "`block_end`", "`apples`" "`bananas`"). Multiple words are currently <ins>not accepted</ins>.  
 
 The only <ins>**unusable** character</ins> is "`#`" as it's both _reserved for pre-processor directives_, and will be used to _comment out_ the delimiters in \<source\>.py output files (which also means "`##`" can't be a valid delimiter too).  
 You need to use `#delim` directive as soon as you like/need to use non-standard _**custom** delimiters_, as Pyndent needs to know how you (custom) delimited your **code blocks**, to be able to re-indent them.  
 Like all Pyndent pre-processor directives, `#delim` must appear at meta-source **top** (but **NOT** as the very first line, to avoid confusion with hashbang `#!`), for it to be used.
 
 **NOTE**: in _Linux environments_, an `#!` (also called hashbang) is used to tell the shell which "processor" to call, to manage the "text" (source code) the shell is reading: that's why a `#delim` directive must <ins>**avoid**</ins> to be written in the first row: writing it starting in the _second or further_ rows is considered correct: only important thing is <ins>a directive appears **before** the first place it need to be used</ins>. If you need to customize your delimiters, you can't add a `#delim` **after** the very first line where (default) delimiters are written, as that behavior will be flagged as inappropriate and made clear with a warning:
 
 The following syntax **works**: `#delim {{ }}` is written **before** the line where `{{` or `}}` appears for the first time:
 
```python
#delim {{ }}
import sys

def example():
{{
print("example!")
}}
```
 
 The following **doesn't work**: `#delim {{ }}` is written **after** the the first `{{`: pyndent will read `{{`, will recognize it's different from its default `{` and will just write `{{` to \<stdout\> (or file, if you'll use -o switch), then Python will complain with you 'cause the brackets it's not managing correctly will more probably create syntax errors somewhere else, in (correct) Python code
 
```python
import sys

def example():
{{
#delim {{ }}
print("example!")
}}
```

 The rule is: when Pyndent will start **using** a delimiter (its own defaults or your custom ones) it won't accept to _change_ it later (it will emit a warning like "_**WARNING [mixed-delimiters]**: #delim directive used after first delimiter is used_"): <ins>midex-delimiters are **not** allowed</ins>.

<br>

 ## Directives Examples<a name="preprocdirxamp"></a>
 
 #delim example 1:

```python
#delim begin end
def example():
begin
    if True:
    begin
    print("nested")
    end
end
```
 
 #delim example 2:

```python
#delim < >
def example():
<
    if True:
    <
    print("nested")
    >
>
```

<br>

 ## Hashbang management<a name="hashbang"></a>
 
 In Pyndent meta-sources you may need, like in every other source, to use the hashbang (`#!`) to engage Pyndent, instead of explicitly calling it externally. So, you're going to have a first meta-source line like that, in your Pyndent .pyn file:
 
```python
#!/usr/bin/pyndent <options> <filename>
(Python code here)
```

 At the same time, a Python programmer, _even if using Pyndent to pre-process his code_, would like to **use the hashbang** to call the Python interpreter, in his final .py source.  
 How to achieve it?  
 
 It can be achieved by using a simple rule of hashbangs co-existence: Pyndent's hashbang **precedes** Python's one, in **.pyn** meta-sources, as well as Python's hashbang will **precede** Pyndent's one in **.py** sources: the swap will be done by Pyndent this way:

(Pyndent meta-source: _example.pyn_)

```python
#!/usr/bin/pyndent -o example.py
#!/usr/bin/env python3
#delim {{ }}

import sys

def example():
{{
print("example!")
}}

example()
```

 The above meta-source will be processed this way by Pyndent:
 
(Python source: _example.py_)

```python
#!/usr/bin/env python3
#!/usr/bin/pyndent -o example.py
#delim {{ }}

import sys

def example():
#{{
	print("example!")
#}}

example()
```

 Python won't complain, if finding the `#!/usr/bin/pyndent -o example.py` as **second** line: it will manage it as a _normal comment_. The result will be 100% Python code (with Pyndent source hashbang, directive(s), and (custom) delimiters **retained**).  
 This way, if anyone will need to `--restore` .py code to the original meta-code, Pyndent will be able to read its own **original hashbang** (if present, it will re-swap it with Python's one), the **directives** (`#delim` in our case) are untouched and don't need to be "restored", all **delimiters** are still there, even commented (`#{{`, `#}}`) and can be easily brought back: `{{`, `}}` (also considering `#delim` contents, if in doubt).

<br>

 ## Syntax scheme<a name="syntax"></a>
 
 **pyndent [option]... \<meta\>.pyn [\<source\>.py]**  
 for [options]: [-o][-e][-x][-s][-f][-i][-v]  
 
 **pyndent \<source\>.py [option]... [\<meta\>.pyn]**  
 for [options]: [-r][-f][-i][-v]  
 
 **pyndent [option]...**  
 for [options]: [-h][-V]  

 **pyndent**  
 is equivalent to **pyndent --help**

<!-- pyndent \<meta\>.pyn [-o [-f] \<source\>.py] [-s][-v]  
					  [-e]  
					  [-x] [-f] \<source\>.py] [-s][-v]  
 pyndent \<source\>.pyn [-r][-o [-f] \<meta\>.py] -->
 
 If no option is given, Pyndent default behavior is to read a meta-source .pyn file, translate it into a re-indented Python source code writing it to \<stdout\>. In this case the meta-source .pyn file is a mandatory argument.  

<br>

 ### Options are<a name="options"></a>
 
 | Simple | Extended | Description |
 |:-------|:---------|:------------|
 | [-e](#optdet_e) | [--exec<br>--execute](#optdet_e) | tells Pyndent to launch Python, to _execute_ the processed code (from \<file\>.py or \<stdout\>), if the pre-processing ended correctly (RC = 0).<br>By default, the code is written to \<stdout\>, so it's then read from \<stdin\> by Python (unless `-o` or `-x` are used) |
 | [-o](#optdet_o) | [--outfile](#optdet_o) | asks Pyndent to write the output to a \<filename\>**.py** instead of \<stdout\>.<br>\<filename\> is optional: if not given, the meta-source one is used |
 | [-x](#optdet_x) | [--execout<br>--execute-output](#optdet_x) | _combo_ switch implying `-e` and `-o`: everything valid for `-e` and `-o` is valid for `-x` too<br>(`-x` and `-e`/`-o` are of course <ins>mutually exclusive</ins>) |
 | [-f](#optdet_f) | [--force](#optdet_f) | allows to _silently overwrite_ the output file if already present: if not given and Pyndent finds the output file when going to write it, an **error** is emitted and the original target file is <ins>not overwritten</ins><br>**Force** is an option to `-o`, `-x` and `-r` |
 | [-i](#optdet_i) | [--interactive](#optdet_i) | _prompts_ to replace an output target file, if found, instead of exit in error |
 | [-s](#optdet_s) | [--strip<br>--strip-delims](#optdet_s) | _**strips** the delimiters away_ from the final Python code (AKA avoid to write them out at all), as well as every Pyndent element (like `#delim` or hashbang swapping), producing <ins>**100% pure Python source**</ins> without any Pyndent meta-source element into. |
 | [-r](#optdet_r) | [--restore](#optdet_r) | asks Pyndent to _restore_ (de-process) a meta-source from a Python .py source (mandatory), restoring all the Pyndent elements (delimiters, hashbang if present) from commented ones<br>having Pyndent elements commented in the source .py file is not mandatory <ins>if the source correctly executes</ins> in Python<br>(a .pyn file will be written, if using `-o` switch)<br>(disables `-e` and `-x` option) |
 | [-v](#optdet_v) | [--verbose<br>--v1<br>--v2](#optdet_v) | will write all `--verbose` messages to \<stderr\>, for the asked verbosity level (where -v/--v1 = **INFO**, --v2 = **DEBUG**), as well as the produced Python code to \<stdout\> (unless `-o` switch is given). |  
 | [-h](#optdet_h) | [--help](#optdet_h) | shows simpler usage (`-h`) or full help (`--help`) |
 | [-V](#optdet_V) | [--version](#optdet_V) | shows the current Pyndent version |
 
 _note: always check the [ROADMAP](ROADMAP.md) to see which options are available already._

<br>
 
 ## Options in detail<a name="optdetails"></a>
 
 By default, Pyndent reads a meta-source (\<filename\>**.pyn**) and writes a full-Python source to \<stdout\>, nothing else: it only _rewrite indentation_ from scratch.  
 As it can be customized to perform different tasks, you can use the following switches too:

<hr>
 
 ### `-e` `--execute`<a name="optdet_e"></a>
 Tells Pyndent to launch Python, passing it the processed Python code (from file or \<stdout\>) to process, if the pre-processing ended correctly (RC = 0). By default, the code is written to \<stdout\>, so it's then read from \<stdin\> by Python (unless `-o` or `-x` are used)
 
`pyndent -e meta.pyn`  
- will produce a Python source stream to \<stdout\>, then launch Python which will read its \<stdin\> to execute it  

`pyndent -e meta.pyn -o source.py`  
- will produce a **source.py** file, then launch **Python source.py** to execute it  

`pyndent -e meta.pyn -o`  
- the same, but will produce **meta**.py file, then launch **Python meta.py** to execute it  

<hr>

 ### `-o` `--outfile`<a name="optdet_o"></a>
 Asks Pyndent to write the output to a \<filename\>**.py** instead of \<stdout\>. \<filename\> is optional: if not given, the meta-source one is used

`pyndent -o source.py meta.pyn`  
- will read meta.pyn and write source.py file, instead of just output the processed results to \<stdout\>  

`pyndent meta.pyn -o source.py`  
- the same, with more "natural" syntax: input first, then output file as last  

`pyndent -o meta.pyn`  
- will read meta.pyn and write meta.py file: \<metasource\> filename is taken from meta.pyn input  

`pyndent meta.pyn -o`  
- the same, even if _less intuitive_ but it works too  

<hr>

 ### `-x` `--execute-output`<a name="optdet_x"></a>
 _Combo_ switch implying `-e` and `-o`
 
`pyndent -x meta.pyn`  
- will be internally translated into `pyndent -e -o meta.pyn`, resulting in **meta.py** file on disk, then Python interpreter executing it  

`pyndent -x source.py meta.pyn`  
- will be internally translated into `pyndent -e -o source.py meta.pyn`, resulting in **source.py** file written to disk, then Python interpreter is called to execute the created file  

|    |
|:---|
| be warned that, despite obvious, `-x` and `-e`/`-o` options are **<ins>mutually exclusive</ins>**|

<!-- > be warned that, despite obvious, `-x` and `-e`/`-o` options are **<ins>mutually exclusive</ins>** -->

<hr>

 ### `-f` `--force`<a name="optdet_f"></a>
 Asks Pyndent to overwrite the output without asking, if a target file is found

`pyndent -o source.py meta.pyn` or `pyndent meta.pyn -o source.py`  
- will exit in **error** if \<source\>.py is present already  
`pyndent -o source.py meta.pyn -f` or `pyndent meta.pyn -f -o source.py`  
`pyndent -x source.py meta.pyn -f` or `pyndent meta.pyn -f -x source.py`  
- will overwrite \<source\>.py if found

`pyndent meta.pyn -o`  
- will exit in **error** if \<meta\>.py is present already
`pyndent meta.pyn -o -f`  
`pyndent -x meta.pyn -f`  
- will overwrite \<meta\>.py if found

`pyndent -r source.py meta.pyn -f`  
- will overwrite \<source\>.py if found

`pyndent meta.pyn -r -f`  
- will overwrite \<meta\>.py if found

`pyndent meta.pyn -o source.py`  
- the same, with more "natural" syntax: input first, then output file as last  

`pyndent -o meta.pyn`  
- will read meta.pyn and write meta.py file: \<metasource\> filename is taken from meta.pyn input  

`pyndent meta.pyn -o`  
- the same, even if _less intuitive_ but it works too  

<hr>
 
 ### -s --strip<a name="optdet_s"></a>
 Asks Pyndent to _**strip** the delimiters away_ from the final Python code (AKA avoid to write them out at all), as well as every Pyndent element (like `#delim` or hashbang swapping), producing <ins>**100% pure Python source**</ins> without any Pyndent meta-source element into.

`pyndent -s meta.pyn`  
- will write the resulting Python code to \<stdout\> without any of the Pyndent elements  

`pyndent -s -o meta.pyn`  
- the same, but the resulting code will be written into **meta.py** file  

<hr>

 ### -r --restore<a name="optdet_r"></a>
 Asks Pyndent to **reverse-process** (de-process) a Python .py source into a Pyndent meta-source, restoring all the Pyndent elements (delimiters, hashbang if present) from commented ones (a .pyn file will be written, if using `-o` switch).  
 If you need to `--restore` a _pure Python source_ (or even a Pyndent `--strip` one), which <ins>totally lacks Pyndent elements</ins> (even commented), you _could_ give a `#delim <start_delimiter> <stop_delimiter>` directive too, **inline** or into Python source code (starting from _**2nd line** or below_), if you want to override the defaults.
 
`pyndent -r source.py`  
- will write a Pyndent meta-source to \<stdout\>, honoring the inline `#delim` if given, then seasrching for an embedded `#delim` directive in the source file, if lacking the inline one, then falling back to defaults if no directive is found (precedence rule: inline -> embedded -> defaults).  

`pyndent -r #delim {{ }} source.py`  
- the same, but Pyndent assumes there are no pre-existing (commented) delimiters to restore (just skipping existing ones, leaving them commented out): it will add the given delimiters instead.  

<hr>

 ### -v --v1 --verbose --v2<a name="optdet_v"></a>
 Will write all `--verbose` messages to \<stderr\>, for the asked verbosity level (where --v1 = **INFO**, --v2 = **DEBUG**), as well as the produced Python code to \<stdout\> (unless `-o` switch is given).

`pyndent -v meta.pyn`  
- will read meta.pyn, write processed code to \<stdout\>, and **INFO** level messages to \<stderr\>  

`pyndent --v1 meta.pyn`  
- the same: `-v`, `--v1`, and `--verbose` are all _aliases_ for **INFO** messages level  

`pyndent -v -o source.py meta.pyn`  
- will read meta.pyn and write source.py file, and **INFO** level messages to \<stderr\>  

`pyndent -v meta.pyn -o source.py`  
- the same, with more "natural" syntax  

`pyndent --v2 -o source.py meta.pyn`  
- the same, but with more details: **INFO** and **DEBUG** level messages will be written to \<stderr\>  

<hr>

 ### -V --version<a name="optdet_V"></a>
 Shows the current Pyndent version.

<hr>

 ### -h --help<a name="optdet_h"></a>
 Shows simpler usage (`-h`) or full help (`--help`).

<br>

 ## Obsoletes<a name="obsol"></a>
 
 ### -d --dryrun
 Asks Pyndent to simulate the reindentation process, also doing all the needed checks, showing the results to \<stdout\>, not writing the output .py file
 
`pyndent -d meta.pyn`  
- will write the results to \<stdout\> but won't write to file  

 <ins>no more needed as that's now Pyndent default behavior</ins>

<br>

 ## Document History<a name="history"></a>
 
 20250925 original  
 20250925 fixed typos and examples added (Aria@DeepSeek)  
 20251102 markdown translation  
 