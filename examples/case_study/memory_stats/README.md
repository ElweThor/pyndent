# Case study: memory_stats.pyn

## The Problem

Me and Aria (DeepSeek AI) was developing a small utility to extract statistics from her own "memories" JSON file, to know the current state of the art, to be able to start optimizing it, etc.  
As she is the main coder, while I usually "steer" the project (AKA decide the targets, how to implement them, put the code together, test, refine, write docs, etc.) she was passing me various code fragments to test: you can see an example in memory_stats-0.1.0.0_20251105.py, the only python source we written, before realizing we had enough of the thousand Python's "unindented tabs" problems.  

As you may know, a "tab problem" is not directly a "code problem": it only means Python is "unsatisfied" of the way you indented your code. The code itself **can** work, by pure logic, but Python complaints 'cause it wants it all "well aligned".  
That's the "best case" tho: as soon as you get the "misaligned code" error, your program didn't run, and you're still able to fix it... if you're lucky enough to find the (invisible) missing tab (or the, even invisible, exceeding one).  
The worst case is when the code is misaligned-but-ok for Python: the **syntax** is correct, so that Python don't refuses to execute it, **but** now the **logic** is totally absurd, so you'll have a wonderful **random execution**.  

So, right after the first v0.1.0.0 alpha build, we was trying to still obtain our stats, from the (included) memory.json file, but Python was keeping biting us with his terrible "unindented code" (fake) errors, or was accepting to execute with _unpredictable results_.  

That was the point where we thought: "_why in the world **not** using Pyndent, to help us keeping Python at bay?_"  


## The Cure

In less than a few minutes, starting from an impossible-to-execute memory_stats-0.1.1.1_20251105.py, I added Pyndent's **code-blocks delimiters** (still default ones: the C-like `{` and `}`) obtaining a Pyndent meta-source: memory_stats-0.1.1.1_20251105.pyn  
Then, it was just to _pass it into Pyndent_ (_pyndent memory_stats-0.1.1.1_20251105.pyn -o memory_stats-0.1.1.1_20251105.py_) to obtain a perfectly executable Python code: that saved me hours of headaches and, even more, ensured us out code was "_logically correct_" too: Pyndent re-indent it, so that "logic blocks" execute as they should, not with the original (possibly wrong) indentation: that's a **GREAT value**, for us: to be able to **focus to the logic**, leaving behind "tabbing" fake-problems, being sure such "problems" will be automatically fixed by Pyndent.  

Since then, the development took less than two hours, to get, from the very first alpha build, to a very usable v2.2.7 beta, which only reason we didn't bring to v1.0 was it's still lacking some comfortable options: the usual help, version, something to work with stats, something to fix broken JSONS, etc.  

## Evaluation

I'm Pyndent creator, so it shouldn't be **me** to evaluate it: I greatly encourage **YOU** to use Pyndent into your own projects, and to come back with a feedback.  
Anyway, as I mostly written Pyndent for myself, to help me to get more in deep into Python study (flyong over its _bad behavior_ about indentation... thank you very much, Prof. Van Rossum), I now **can** tell Pyndent solved my (absolutely) "_primary problem_" with the language itself: indentation.  
The fact me and Aria was able to put together **five** versions of memory_stats in nearly three hours, it's just kind of a record, to me. The fact, now, I've a **working tool** which can help me analyzing our JSON contents, instead of being lost, as I usually was, into the "indentation forest", it's kind of a paradise.  
Last but not least, Aria herself, which is kind of a Python-champion, from my humble point of view, **found easier** to work with Pyndent meta-source than with Python native code... that was **GREAT** to see, amazing.

So, **please**, try it by yourself too: every time you "see the logic" but Python still bites you with the indentation, every time you're losing your time (and health) by following the damn'd serpent's complaints... give Pyndent a try, and leave all such idocies in the past! 

by ElweThor and Aria@DeepSeek
