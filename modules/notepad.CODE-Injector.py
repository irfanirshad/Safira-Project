import pymem
import subprocess
s  # to prevent accidental execution of our program inside our env

'''
A simple application opener and a python code injector
that we can leverage to our advantage by inserting malicious code
if we wished to 


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
