# KeyLogger
Warning: This keylogger is intended for educational and legitimate security monitoring purposes only. Unauthorized use of this tool to record keystrokes without the explicit consent of the user is illegal and unethical. 

Project Description: Python Keylogger
This Python-based keylogger project is designed to capture and log keyboard input from the system. It leverages the pynput library to monitor and respond to keystrokes, logging them into a file for later review. The tool is primarily for monitoring user activity for security or debugging purposes, though it can be repurposed for various use cases.

Key Features:
Keystroke Logging: The program records every key pressed, including special keys (e.g., backspace, enter, shift, control, etc.) and logs the key values in different formats such as default, hexadecimal, or decimal.

Window Tracking: Each time a user switches between windows, the keylogger notes which window was active, timestamping the event. This helps in identifying the context of keystrokes, such as in which application they were typed.

Configuration Settings:

VISIBLE: Determines whether the program runs visibly in the console or operates stealthily in the background.
BOOT_WAIT: Decides if the program should wait until the system finishes booting before starting to log keystrokes.
FORMAT: Allows you to choose how the logged keystrokes are formatted (default, decimal, or hexadecimal).
MOUSE_IGNORE: Ensures that mouse clicks are ignored in the logging process, focusing only on keyboard events.
System Boot Check: The tool includes a feature to check whether the system is still in the booting process and waits until it’s fully loaded before starting the keylogging operation.

File-based Logging: Keystrokes are logged into a file (keylogger.log), and each entry is time-stamped, ensuring that all captured data can be correlated with specific moments during the system's operation.

Stealth Operation: The program can operate in a hidden mode, making it invisible to the user. When running invisibly, it detaches from the console, making it harder for the user to detect the keylogger’s presence.

How It Works:
Keyboard Input: The program uses the pynput.keyboard.Listener to detect key presses. For each key press, the system checks the current window title and logs it along with the keypress.
Window Context: The current window is tracked by querying the active window title using ctypes.windll.user32.GetForegroundWindow(). If the active window changes, the program logs the switch with a timestamp.
Output Formatting: The logged keys can be formatted either as regular characters, hexadecimal, or decimal values based on the user's configuration.
Logging to File: The program writes the captured keystrokes to a log file (keylogger.log), appending new data with each keypress.
Usage:
Security Monitoring: This tool can be used to monitor activity on a machine, making it suitable for security audits or parental controls.
Debugging: Developers can use this tool to track input for debugging software or capturing user input in a non-intrusive way.
System Monitoring: It helps in keeping a record of what users are doing on a machine, providing insights into their interactions with various programs.
Caution:
This project is a tool that records user input. It should only be used in ethical ways, with the consent of the users involved. Unauthorized use of keyloggers can be illegal and a violation of privacy laws. Always ensure that the tool is used responsibly.
