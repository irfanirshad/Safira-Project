import os
import subprocess
import pymem
s


mem = pymem.Pymem("notepad.exe")
mem.inject_python_interpreter()

code = """
    import tkinter as tk

    win 

"""
