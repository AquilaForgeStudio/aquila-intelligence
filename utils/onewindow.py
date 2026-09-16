import ctypes
import sys

def check():
    MUTEX_NAME = "AQUILA_AI_SINGLE_INSTANCE"

    mutex = ctypes.windll.kernel32.CreateMutexW(
        None,
        False,
        MUTEX_NAME
    )

    if ctypes.windll.kernel32.GetLastError() == 183:
        user32 = ctypes.windll.user32

        hwnd = user32.FindWindowW(None, "Aquila Intelligence")

        if hwnd:
            user32.ShowWindow(hwnd, 9)
            user32.SetForegroundWindow(hwnd)

        sys.exit(0)
