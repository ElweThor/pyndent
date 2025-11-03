
 # Meta Syntax: Pre-Processor Directives
 
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


 ## Directives Examples
 
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

 ## Hashbang management
 
 In Pyndent meta-sources you may need, like in every other source, to use the hashbang (`#!`) to engage pyndent, instead of explicitly calling it externally. So, you're going to have a first meta-source line like that, in your Pyndent .pyn file:
 
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


 ## Command Switches
 
 By default, Pyndent reads a meta-source (\<filename\>**.pyn**) and writes a full-Python source to \<stdout\>, nothing else: it only _rewrite indentation_ from scratch.  
 As it can be customized and asked for different tasks, you can use the following switches too:

 **-o --outfile**: asks Pyndent to write the output to a \<filename\>**.py** instead of \<stdout\>. \<filename\> is optional: if not given, the meta-source one is used

`pyndent -o source.py meta.pyn`  
&emsp; will read meta.pyn and write source.py file, instead of just output the processed results to \<stdout\>  
`pyndent meta.pyn -o source.py`  
&emsp; the same, with more "natural" syntax: input first, then output file as last  
`pyndent -o meta.pyn`  
&emsp; will read meta.pyn and write meta.py file: \<metasource\> filename is taken from meta.pyn input  
`pyndent meta.pyn -o`  
&emsp; the same, even if _less intuitive_ but it works too  
 
 **-e --execute**: tells Pyndent to launch Python, passing it the processed Python code (from file or \<stdout\>) to process, if the pre-processing ended correctly (RC = 0). By default, the code is written to \<stdout\>, so it's then read from \<stdin\> by Python (unless `-o` or `-x` are used)
 
`pyndent -e meta.pyn`
&emsp; will produce a Python source stream to \<stdout\>, then launch Python which will read its \<stdin\> to execute it  
`pyndent -e meta.pyn -o source.py`
&emsp; will produce a **source.py** file, then launch **Python source.py** to execute it  
`pyndent -e meta.pyn -o`
&emsp; the same, but will produce **meta**source.py file, then launch **Python meta.py** to execute it  

 **-x --execute-output**: _combo_ switch implying `-e` and `-o`
 
`pyndent -x meta.pyn`
&emsp; will be internally translated into `pyndent -e -o meta.pyn`, resulting in **meta.py* file on disk, then Python interpreter executing it  
`pyndent -x source.py meta.pyn`
&emsp; will be internally translated into `pyndent -e -o source.py meta.pyn`, resulting in **source.py** file on disk, then Python interpreter executing it  
 
 **-s --strip**: tells Pyndent to _**strip** the delimiters away_ from the final Python code (AKA avoid to write them out at all), as well as every Pyndent element (like `#delim` or hashbang swapping), producing <ins>**100% pure Python source**</ins> without any Pyndent meta-source element into.

`pyndent -s meta.pyn`
&emsp; will write the resulting Python code to \<stdout\> without Pyndent elements  
`pyndent -s -o meta.pyn`
&emsp; the same, but the resulting code will be written into **source.py** file  

 **-r --restore**: asks Pyndent to **reverse-process** a Python .py source into a Pyndent .pyn meta-source, restoring all the Pyndent elements (delimiters, hashbang if present) from commented ones.  
 If you need to `--restore` a _pure Python source_ (or even a Pyndent `--strip` one), which totally lacks Pyndent elements (even commented), you _could_ give a `#delim start_delimiter stop_delimiter` directive too, inline or into Python source code (starting from _**2nd line** or below_), if you want to override the defaults.
 
`pyndent -r source.py`
&emsp; will write a .pyn meta-source, assuming there are code-block delimiters, commented in the source.py code, wether or not they're default ones (if they're different by default ones, a `#delim` directive will be searched in a second scan): delimiters will be read directly from the source and restored. If any delimiter will be found nor a `#delim` directive, Pyndent re-process source.py by using "`{`" and "`}`" defaults like if it found "`#{`" and "`#}`". Process output will go to \<stdout\> by default, unless `-o` switch will be used.  
`pyndent -r #delim < > source.py`
&emsp; the same, but Pyndent assumes there are no pre-existing (commented) delimiters to restore (or just skip existing ones, leaving them commented out): it will add the given delimiters instead.  

 **-v --v1 --verbose --v2**: will write all `--verbose` messages to \<stderr\>, for the asked verbosity level (e.g. --v1 = INFO, --v2 = DEBUG), as well as the produced Python code to \<stdout\> (unless `-o` switch is given).

`pyndent -v meta.pyn`
&emsp; will read meta.pyn, write processed code to \<stdout\>, and **INFO** level messages to \<stderr\>  
`pyndent --v1 meta.pyn`
&emsp; the same: `-v`, `--v1`, and `--verbose` are all aliases for **INFO** messages  
`pyndent -v -o source.py meta.pyn`
&emsp; will read meta.pyn and write source.py file, and **INFO** level messages to \<stderr\>  
`pyndent -v meta.pyn -o source.py`
&emsp; the same, with more "natural" syntax  
`pyndent --v2 -o source.py meta.pyn`
&emsp; the same, but with more details: **INFO** and **DEBUG** level messages will be written to \<stderr\>  


 ## Obsoletes
 
 **-d --dryrun**: asks Pyndent to simulate the reindentation process, also doing all the needed checks, showing the results but not writing the output .py file
 
`pyndent -d meta.pyn`
&emsp; will write the results to \<stdout\> but won't write to file  

 <ins>no more needed as that's now Pyndent default behavior</ins>


 ## Document History
 
 20250925 original  
 20250925 fixed typos and examples added (Aria@DeepSeek)  
 20251102 markdown translation  
 