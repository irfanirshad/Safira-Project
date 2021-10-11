

GARAGE PROJECT: Writing a Windows Malware in Python3 with dynamic functionalities...

~ OBJECTIVE:
Stage I :: Write a Python malware that is small in size and can compile and execute in an env where
Python/Python3 is not installed (Can run in default out of the box Windows OS) .

Stage II :: Write the Mainprogram.py wherein we will be taking WebCam shots, Screenshots and performing Web Requests while
trying to attempt escalating user privileges . The Database of our choice is SQLite.

Stage III :: Using Nuitka convert to a Linux ELF x86-64(C program executable). Obfuscation to be done at this stage
or after the translation into Compiled code.

Stage IV(Future): Import an Nmap Module with it (or a Lua Based Lib) for dynamically scanning ports on the run
and report to the Command Center(Me/our host server) . IP addresses and port scanner tools needed..


~ THEORY:
Write the program in python and then using tools , translate into C program which will translate
the python module into a C program . This will then essentially make our program run in any native OS
system . Thus bypassing all dependencies of having any external libraries for our Malware to
execute.
Save all of our data db files in SQLite.
GL HF!


~Technical-ToolBox(Modules, External Tools etc) :

*Modules:
    0) sys -

    1) os - routines for NT or Posix depending on what system we're on

    2) logging(?) - for escalating privileges

    3) python-mss - For taking screenshots

    4) request - making web requests

    5) httpx -  HTTP client library. Supports both HTTP(1.1 & 2.2) protocols. Supports sync and async APIs

    6) TBD -- Nmap module for port scanning and IP support.

    7) time - Time module

    x) --(TBD) ->{ add any other if needed . Find motivation if needed . Design structures of malware }

External Tools:

    1) Any standard Python Obfuscator Tool - Harder to Reverse Engineer our malware

    2) Nuitka -  Provides Obfuscation within as well.

    3) UPX - Compression. Ultimate Packer for Executables for most OS environments. Read Wiki4more.

    4)
