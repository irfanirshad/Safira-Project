import pymem
import subprocess
s  # to prevent accidental execution of our program inside our env


'''
A simple application opener and a python code injector
that we can leverage to our advantage by inserting malicious code
that executes itself on victim's system.



Pending :: =>
1) Replace or add a class that takes in the 'cmd.exe' and executes code on it itself thereby essentially
    giving us a whole shell to work with instead of a boring notepad.

2) Leverage: PowerShell allows us to tap into the system thereby allowing us to inject & save vulnerable
    libraries and inturn their exploits which will result in us escalating privilegs to hopefully the r00t.


'''


# We try to read the memory of the NotePad's process
try:
    mem = pymem.Pymem("notepad.exe")
except:
    # If not found we force open it ourselves
    subprocess.Popen("notepad.exe")
    mem = pymem.Pymem("notepad.exe")

mem.inject_python_interpreter()

# Here lies the code in python we wish to inject inside the notepad
code = """
    import tkinter as tk

    win = tk.Tk()
    win.mainloop()

"""

mem.inject_python_shell(code)
