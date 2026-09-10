import platform

def play_alert():
    """Play a simple system alert without requiring an audio file."""
    print("\aALERT: Driver drowsiness/yawning detected!")

    try:
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            # Terminal bell; behavior depends on the operating system/terminal.
            print("\a")
    except Exception:
        pass
