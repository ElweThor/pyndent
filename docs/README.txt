
 Pyndent: Solving Python's Indentation Dilemma

 ___THE_PROBLEM___

 This project, essentially a Python tool: a preprocessor, aims to solve the perennial problem of managing indentation in Python source code.
 The problem is caused, on the one hand, by Python's author, Guido Van Rossum, who mandates indentation (which is a good thing) to the point of factoring it into syntax checking (which is a bad thing, IMHO).
 While indentation is a good thing, and shouldn't be underestimated, we must also be realistic: spending hours debugging a "logically correct" program just because there's a missing tab that modifies the execution logic, "somewhere" among thousands of lines of code, is extremely frustrating (and leads people like me to abandon Python, even though it is an excellent language).
 On the other hand, Python lacks configuration switches that allow you to "not consider indentation mandatory." This makes partial sense, considering it doesn't have "code block delimiters," as almost all languages do (the curly braces of C-like languages, the begin/end blocks of Pascal, and the various while/wend, if/then/else, and do/end constructs of other languages).
 The lack (by design) of the ability to define a "code block" leads directly to the need for stringent indentation. The result: if, for some reason (which happens all too often, especially when copying/pasting text from sources that sometimes use tabs, sometimes spaces, but not necessarily four at a time), a line is displaced, the syntax check fails at best (Python warns), or the execution is "random" at worst (Python executes, but "in its own way").


 ___EXAMPLES___
 
 The following (trivial) code will execute correctly (line nimbers are added for reference only):

1	x = 1
2	if x == 1:
3		print('you won!')
4		print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')

 results:
 
 you won!
 go to the cashier to collect your winnings

 while the following will result in a syntactic indentation error:

1	x = 1
2	if x == 1:
3		print('you won!')
4	   print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')

 results:

    print('go to the cashier to collect your winnings')
													^
IndentationError: unindent does not match any outer indentation level

 due to a missing space on line 4 (which, in a source code with thousands of lines, can be difficult to detect).
 But this is the best case: Python detects the incorrect indentation and flags it.

 If, however, the error was a tab being "lost" or removed (see line 4 again):
 
1	x = 0
2	if x == 1:
3		print('you won!')
4	print('go to the cashier to collect your winnings')
5	if x == 0:
6		print('try again, you will be luckier')

 results:

go to the cashier to collect your winnings'
try again, you will be luckier'

 The indentation and formal python syntax are correct, but the logic is completely distorted, and only because we can't write:
 
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

 (thanks to I'm-always-right-Professor Van Rossum).


 ___THE_CURE___
 
 To (try to) work around this problem, I decided to "add" two code delimiters to the standard Python source code: by default, the delimiters are the C ones, the curly braces "{" and "}" (we'll see later if/how to make them configurable).
 Since I have no intention to modify the language source (fork), I thought a meta-program, written using delimiters, should be pre-processed before being executed by the Python language.
 The logic is as follows:

 1. Write a metaprogram using Python syntax, as always (each line must be, syntactically, pure Python code, barring errors, of course).
 2. When you want to start a code block, insert a "start delimiter" (i.e., "{," unless otherwise configured) on a separate line (i.e., the line can contain _only_ spaces, tabs, or _one_ of the two delimiter characters).
 3. Indentation is optional (but it should be used anyway: it makes the source code more readable).
 
 the meta-source produced _cannot_ be executed by python which, not recognizing the (custom) delimiters, would give an error:
 
 4. Launch the pyndent preprocessor (PYthon INdent) by passing it the meta-source <filename>.pyn
 5. pyndent:
 .1 will count the block opening delimiters (default "{") to determine the indentation level of the code
 .2 will check the (numeric) correspondence with the closing delimiters (default "}"), reaching the end of the meta-code
 .3 Line by line, it will replace each opening delimiter with a comment (i.e., "{" -> "#{") so that the Python syntax remains pure (i.e., without delimiters), but only (i.e., exclusively) on lines whose only characters are: space, tab, or block opening or closing delimiter, nothing else
 .4 will remove any pre-existing indentation (i.e., spaces and/or tabs) by reconstructing it from scratch, thanks to the open/closed block counter
 .5 will also replace the block closing delimiters "}" with the sequence "#}"
 .6 by default, if the "reindentation" was successful, it will write a <filename>.py source
 .7 optional: by passing the -e (--execute) switch, you can launch the Python interpreter, passing it the newly preprocessed code (which, hopefully, will also be correctly indented, or it will fail if the count of the delimiters is odd between open and closed delimiters).


 ___PYNDENT_EXAMPLE___
 
 With pyndent you can write an example.pyn meta-source like this:

- - 8<- - - - 8<- - - - 8<- - 
def example():
{
    if True:
    {
      print("nested block")
    }
}

example() 
- - 8<- - - - 8<- - - - 8<- - 

 then call pyndent to let it re-indent to correct python code for you: pyndent example.pyn
 Pyndent will write this (100% python exacutable code) to your stdout:
 
def example():
#{
    if True:
    #{
        print("nested block")
    #}
#}

example()

 if you then pipe the output to python, this way: pyndent example.pyn | python
 you'll see the following in your terminal/console:
 
nested block 

 and python won't complain 'cause, at the print() line, you didn't indent it as it wanted... 'cause pyndent did it for you!

	
 ___PYNDENT DO'S AND DON'TS___
 
 - it does _not_ check Python syntax, a job that is left to the Python interpreter itself: it is the programmer's responsibility to use a delimiter on a separate line (this is the only constraint, and it was placed for clarity of the meta-source and ease of conversion)
 - since the default delimiters ("{" and "}") are also used by Python, _no_ syntax check is performed, not even "as delimiters": that is, it does not check whether the use of a delimiter in a line containing code can be "a delimiter" or not: everything that appears in a source line that is not solely
	- space
	- tab
	- open/close delimiter
   is considered "Python code": pyndent simply writes it to <stdout>/output (line "skip"), without checking anything, and syntax checking is left to the language at runtime.
 - it only looks for its own opening/closing delimiters for code blocks (the configured delimiters: the defaults, or whatever delimiter the programmer has chosen)
  (Note: If you don't use the defaults, you should add a meta-statement: "#delim" containing the start/stop delimiters, e.g. "#delim < >", at meta-source very start)
 - performs the substitution with comments (so that the resulting code is 100% Python): "{" -> "#{" and "}" -> "#}"
 - removes previous indentation and recreates it from scratch
 
 This way, we hope to help the community, which is divided on the issue: purists will get pure Python code (with some additional comments: consider adding the -s (--strip-delims) switch to get Python code without delimiters, not even as comments). Professional programmers, who are forced to be pragmatic (and fast), will be able to use pyndent and a C-like meta-syntax to define blocks of code, safe in the knowledge that (1) pyndent will never complain about syntax problems (if the number of "{" equals the number of "}") and (2) Python will execute the code correctly even if "badly indented", because the .py source will be indented correctly (it is only the .pyn source that can contain fancy and imprecise indentations).
 
 Community aside, my personal interest would be to be able to use Python without having to worry about errors generated by statement placement (not in 2025, please!), which is why I've never seriously used (and therefore never learned deeply) this excellent language.
 Finally, it's worth noting that a .py source code processed by pyndent is de-processable (the relationship is bijective): thanks to the fact that the code block delimiters remain in the .py source code, having only the latter available will allow you to run pyndent with the -r (or --restore) switch to obtain an editable .pyn source code that can then be pre-processed again into a .py source code. That could help, if you like to publish your code on a web platform where you're not sure tabs will be written correctly in the code.

 Part of this project is due to an analysis of the situation carried out together with "Aria" (DeepSeek's AI), and later verified together with "Ru" (OpenAI's ChatGPT AI): https://chatgpt.com/share/68d49cce-8724-8011-811d-547e3fed4de2

 20250924 Elwe Thor


 ___LICENSE___
 CC BY-NC-SA 4.0
 see LICENSE file for details


 ___DOCUMENT_HISTORY___
 
 20250924 original (italian text)
 20250925 update, after speaking with ChatGPT, translated to english too
 20250925 further update after speaking with Aria
