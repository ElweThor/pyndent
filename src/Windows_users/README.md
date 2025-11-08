# Windows users

 As Windows lacks aliases, as well as real symlinks/hardlinks (and I already checked this behavior <ins>can't</ins> be carried out by Windows' links), to be able to launch Pyndent wherever you are in your filesystem you have some alternatives:
 
1. add the path to your Pyndent executable (pyndent.py) to the system PATH: that's the usual way

2. use a batch file (pyndent.bat) to launch Pyndent executable:  that works if you use Windows DOS shell  
   - the batch file needs to be placed in a directory included in the system PATH  
   - it needs to point to Pyndent executable  
    (this way it works like Linux aliases)
   
3. use a shell able to define aliases:  
   - the shell I'm using to interface with GitHub via CLI (MINGW64 bash), while I'm developing Pyndent, works exactly like Linux Bash
     - it have its own .bash_profile, .bashrc, Linux commands, etc.

The launch works this way: when you're using Windows shell (DOS cmd), being in whichever directory you have your source/meta-source to process

```python
> pyndent .\mymeta.pyn -o .\mysource.py
```

 launches \<Python launcher directory\>\pyndent.bat \<parameters\> --> \<Pyndent directory\>\src\pyndent.bat \<parameters\> --> \<Pyndent directory\>\src\pyndent.py \<parameters\>
 
 This works the same as you:  
 1. added \<Pyndent directory\>\src\ to Windows PATH  
 2. used a Linux/Linux-like bash to setup an alias like pyndent='\<Pyndent directory\>\src\pyndent.py'  
 3. set up a symlink/hardlink to \<Pyndent directory\>\src\pyndent.py in a directory included in the system PATH  
 