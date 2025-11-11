
# Pyndent: Solving Python's Indentation Dilemma

 - [The Problem](#problem) ([examples](#problemxamp))
 - [The Cure](#cure)
 - [Pyndent example](#pynxamp)
 - [Pyndent Do's and Don'ts](#dodonts)
 - [Closure](#closure)

<br>

 ## The Problem<a name="problem"></a>

 This project, which could be **language agnostic** but, essentially, a Python tool (a preprocessor), aims to solve the perennial problem of managing indentation (<ins>as part of the syntax</ins>) in Python source code.  
 The **problem** is caused, on the one hand, by Python's author himself, Guido Van Rossum, who **mandates indentation** (which is a **good** thing) to the point of _factoring it into syntax checking_ (which is a **bad** thing, IMHO).
 
 While indentation is a good thing, and _shouldn't be underestimated_, we must also be **realistic**: spending hours debugging a "_logically correct_" program just because there's a missing tab that modifies the execution logic, "somewhere" _among thousands of lines of code_, is extremely frustrating (and leads people like me to **abandon Python**, even though it definitely is an _excellent language_).  
 
 On the other hand, Python lacks configuration switches that allow you to "_not consider indentation mandatory_" as indentation is a **core feature**, mandatory part of the syntax. This makes partial sense, considering it doesn't have "**code block delimiters**", like almost all languages do (the _curly braces_ of C-like languages, the _begin/end_ blocks of Pascal, and the various _while/wend_, _if/then/else/endif_, and _do/end_ constructs of many languages).
 
 The lack (_by design_) of the ability to define a "**code block**" leads directly to the need for _**stringent indentation**_.  
 The result: if, for any reason (which happens too often, especially when copying/pasting text from sources that sometimes use tabs, sometimes spaces, but not necessarily four at a time), a line is _displaced_, the syntax check **fails** at best (_Python warns!_), or the execution is "**random**" at worst (Python executes, but "_in its own way_" following the indentation "blocks" logic).
 
 ### Note
 I'm not naive: I **know** that, if you just tell "_indentation is a good thing and everyone should use it_", you'll end with a great amount of messy indented code: the reasons why Prof. Van Rossum made indentation mandatory, at the point a program won't execute or execute "with random logic", is **clear** to me.  
 I also can bear with Python telling me "_blablabla you indented your source in a wrong way_" (like the way I accept a C compiler telling me it can't find a "`;`" at statements' end: I'm always tempted to shout "**SO, WHY NOT ADDING IT BY YOUR OWN?!??**" but <ins>I know why</ins> it happens, so ok, it's _normal_).  
 What I really (REALLY!!!) can't bear with, when indentation enters in the syntax **and** execution logic game, is a program I "can see" it's _correct_, **executes randomly** only 'cause of a misplaced/lost/added `TAB`!  
 And that stopped me to learn Python, but I **wanted** to learn it so... this is **my way**, Professor.

<br>

 ### Examples<a name="problemxamp"></a>
 
 The following (trivial) code will _execute correctly_ (line numbers are added _for reference only_):
 
```python
1	x = 1
2	if x == 1:
3		print('you won!')
4		print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')
```

 results:
 
 `you won!`  
 `go to the cashier to collect your winnings`

 while the following will result in a **syntactic indentation error** (look at line `4`):

```python
1	x = 1
2	if x == 1:
3		print('you won!')
4	   print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')
```  

 results:
```python
    print('go to the cashier to collect your winnings')  
													^  
IndentationError: unindent does not match any outer indentation level
```  
 due to a _missing space_ on line `4` (which, in a source code with _thousands of lines_, can be difficult to visually detect).  
 But this is the <ins>**best** case</ins>: Python _detects_ the incorrect indentation and _flags it_.

 If, however, the error was a **tab** being "_lost_" or removed (see line `4` again):

```python
1	x = 0
2	if x == 1:
3		print('you won!')
4	print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')
```

 results:

`go to the cashier to collect your winnings'`  
`try again, you will be luckier'`

 The indentation and formal python syntax are _correct_, but the logic **makes no sense**, and that only because we can't write:

```python
1	x = 0
2	if x == 1:
	{
3		print('you won!')
4	print('go to the cashier to collect your winnings')
	}
5	if x == 0:
	{
6		print('try again, you will be luckier')
	}
```

 (thanks to I'm-always-right-Professor Van Rossum).

<br>

 ## The Cure<a name="cure"></a>
 
 To (try to) _work around_ this problem, I decided to "_add_" two **code delimiters** to the standard Python source code: by default, the delimiters are the C ones, the curly braces "`{`" and "`}`" (we'll see later if/how to make them configurable: have a look at the [ROADMAP](ROADMAP.md)).  
 Since _**I have no intention to modify the language source**_ (fork), I thought a _meta-program_, written by using delimiters, should be **pre-processed** before being executed by the Python language: **Pyndent** is that _pre-processor_.
 
 The logic works as follows:

 1. Write a _meta-program_ <ins>using Python syntax</ins>, as always (each line must be, syntactically, **pure Python code**, barring errors, of course).
 2. When you want to start a _**code block**_, insert a "_start delimiter_" (i.e., "`{`", unless otherwise configured) on a **separate line** (i.e., the line can contain _**only**_ `spaces`, `tabs`, or _**one**_ of the two _delimiter characters_).
 3. Indentation is _**optional**_ (but it should be used anyway, even in the meta-source: it makes the source code **more readable** and I'll never stop remarking it).
 
 the produced meta-source _**cannot**_ be directly executed by Python which, _not recognizing the_ (custom) _delimiters_, would give an error, so:
 
 4. Launch the **Pyndent** preprocessor (PYthon INdent) by passing it the _\<filename\>.**pyn**_ meta-source.
 5. Pyndent:
	- will _count the block opening delimiters_ (default "`{`") to determine the code _indentation level_
	- will _check the (numeric) correspondence_ with the closing delimiters (default "`}`"), reaching the meta-code end
	- line by line, it will **replace** each _opening delimiter_ with a comment (i.e., "`{`" -> "`#{`") so that the <ins>Python syntax remains pure</ins> (i.e., without delimiters), but only (_exclusively_) on lines whose **only characters** are: `space`, `tab`, or `block opening or closing delimiter`, **<ins>nothing else</ins>**
	- will **remove** any _pre-existing indentation_ (i.e., `spaces` and/or `tabs`) by _**reconstructing** it from scratch_, thanks to the open/closed block counter
	- will also **replace** the _block closing delimiters_ "`}`" with the "`#}`" sequence
	- by default, if the "_reindentation_" was successful, it will write Python source code to console's **\<stdout\>** stream (this is <ins>Python executable</ins>, with correct indentation), or a _\<filename\>.**py**_ file, if you used the `-o`/`--output` switch
	- _optional_: by passing the `-e` (`--execute`) switch, you can _launch the Python interpreter_, passing it the newly preprocessed code (which, hopefully, will also be correctly indented, or _it will fail_ if the count of the delimiters is **odd** between _open_ and _closed_ delimiters).

<br>

 ## Pyndent Example<a name="pynxamp"></a>
 
 With Pyndent you can write an example.pyn meta-source like this:

```python
def example():
{
	if True:
	{
	print("nested block")
	}
}

example() 
```

 then call **Pyndent** to let it re-indent the meta-source to correct python code for you: `pyndent example.pyn`  
 Pyndent will write this (100% python exacutable code) to your stdout:

```python
def example():
#{
    if True:
    #{
        print("nested block")
    #}
#}

example()
```

 if you then **pipe** the output to python, this way: `pyndent example.pyn | python` (or even give `pyndent example-pyn -e`)  
 you'll see the following in your terminal/console:
 
`nested block`

 and python **won't complain** 'cause, at the print() line, you didn't indent it as it wanted... 'cause _**Pyndent did it for you!**_

 #### note about the above examples
 they are of course <ins>extremely trivial</ins>, to allow everyone to see **how** Pyndent works and **why**...  
 ...but try wonder if your boss asked you the usual "solution _for yesterday_" (which is an everyday thing, in the real world) and you're trying your best to accomplish, by putting together your code, pieces of code found in the internet, nowadays even pieces given by AIs, thousand of code lines you mostly just hope they work (as, if you had the <ins>time</ins> to write the whole thing by your own, you indented and double-checked all far better), and <ins>the indentation is screwed</ins> a lot by the many different platforms in the net: I'm sure you'll agree with me that _"losing" a few minutes_ to find every ":" (_def function():_, _for a in mylist:_, _if b == result:_, etc.) and including the related code into a simple couple of delimiters, then pre-process the whole thing to get executable Python code **can be a value** (to the very least you won't be fired!).

<br>

 ## Pyndent Do's and Don'ts<a name="dodonts"></a>
 
 - it does <ins>**not** _check Python syntax_</ins>, a job left to the Python interpreter itself: it is the _programmer's responsibility_ to **use a delimiter on a separate line** (this is the **ONLY** Pyndent requirement, and it was placed for meta-source clarity and ease of conversion)  
 - since the default delimiters ("`{`" and "`}`") are also _used by Python_, _**no** syntax check is performed_, not even "_as delimiters_": that is, it does not check whether the use of a delimiter in a line containing code can be "_a delimiter_" or not: everything that appears in a source line that is **not** solely
	- `space`
	- `tab`
	- `open`/`close` `delimiter`
   is considered "**Python code**": Pyndent simply _writes it to \<stdout\>/output_ (line "_skip_"), **without checking anything**, and syntax checking is left to the language at runtime.  
 - it <ins>**ONLY**</ins> looks for its own opening/closing delimiters for **code blocks** (the configured delimiters: the defaults, _or whatever delimiter the programmer has chosen_)  
  (**Note**: If you don't use the defaults, _you should add a meta-statement_: "**#delim**" containing the start/stop delimiters, e.g. "**#delim `<` `>`**", at meta-source very start)  
 - performs the substitution with _comments_ (so that the resulting code is <ins>**100% Python**</ins>): "`{`" -> "`#{`" and "`}`" -> "`#}`"
 - _removes_ previous indentation and **recreates** it from scratch


 ### Notes
 
 _**I know**_ python uses "`{`" and "`}`" by its own (to define **sets** and **dictionaries**). If they're used as Pyndent delimiters (default ones) we must remark the _Pyndent's **golden rule**_: "<ins>_a delimited **by its own on a line** is a Pyndent element, not a Python one_</ins>".  
 This means that, if you're used to define a _dictionary_ this way:
 
_my_dict = {  
"brand": "Ford",  
"model": "Mustang",  
"year": 1964  
`}`_
 
 you better define it this way, instead (_if you're writing a **.pyn** meta-source_):
 
_my_dict = {  
"brand": "Ford",  
"model": "Mustang",  
"year": 1964 `}`_

 or the `}` will be counted as a _**Pyndent clode-block closer** delimiter_, resulting into an "_unbalanced delimiters error_".  
 Of course, if you override the defaults, by defining your own delimiters (e.g. **#delim `begin` `end`**) you _bypass this problem completely_... maybe falling into other problems too, as we don't force you to use predefined delimiters: it's **up to you** not to use Python's _**reserved words**_ as delimiters.  

 I didn't mention **sets** 'cause they're usually defined this way:
 
_my_set = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}_
 
 and it's unusual to see them this way:
 
_my_set = {  
'apple', 'orange', 'apple', 'pear', 'orange', 'banana'  
`}`_
 
 or even this way:
 
_my_set = {  
'apple',  
'orange',  
'apple',  
'pear',  
'orange',  
'banana'  
`}`_

 but Pyndent **golden rule** applies to them too (to whichever (Pyndent's) _**delimiter-on-a-single-line**_, as a matter of fact).
 
<br>

 ## Closure<a name="closure"></a>
 
 This way, we hope to _**help the community**_, which is divided on the issue: _purists_ will get _**pure Python code**_ (with some additional comments: consider adding the `-s` (`--strip-delims`) switch to get Python code without delimiters, not even as comments, out of a Pyndent meta-source).  
 
 _Professional programmers_, who are forced to be _pragmatic_ (and _fast_), will be able to use Pyndent and a _C-like [meta-syntax](meta-syntax.md)_ to define **code blocks**, _safe_ in the knowledge that **`1`** Pyndent will _never complain about indentation-driven syntax problems_ (if the **number** of "`{`" equals the number of "`}`") and **`2`** Python will _execute the code correctly_ even if "_badly indented_", because the **.py** source _will be indented correctly_ (it is only the **.pyn** _meta-source_ that _can contain fancy and imprecise indentations_).
 
 Community aside, my **personal interest** would be to _be able to use Python **without having to worry** about errors generated by statement **placement**_ (`not in 2025, please!`), which is why I've never seriously used (and therefore never learned deeply) this excellent language.
 
 Finally, it's worth noting that _a **.py** source code processed by Pyndent is **de-processable**_ (the relationship is biunivocal): thanks to the fact that the code block delimiters remain in the **.py** source code (unless wild purists strips them), having only the latter available will allow you to run Pyndent with the `-r` (or `--restore`) switch to obtain an _editable **.pyn** meta-source code_ that can then be pre-processed again into a **.py** source code (e.g. to change default delimiters with custom ones, if you need that). That could help, if you like to _publish your code_ on a web platform where you're _not sure tabs will be correctly written_ in the code.
 
 Part of this project is due to a (persistent) rant of me ('cause I was "_unable to use Python_": yes, _mandatory indentation_ which **reflects on syntax** gives me a rash, I'm sorry, Guido), and to an _analysis of the situation_ carried out together with "**Aria**" (DeepSeek's AI), and later verified together with "**Ru**" (OpenAI's ChatGPT AI): https://chatgpt.com/share/68d49cce-8724-8011-811d-547e3fed4de2 (ITalian chat)

 _20250924 Elwe Thor_

<hr>

 ### Document History
 
 - 20250924 original (italian text)
 - 20250925 update, after speaking with ChatGPT, translated to english too
 - 20250925 further update after speaking with Aria
 - 20251102 translated to markdown
