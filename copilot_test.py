import platform
import subprocess

def get_windows_uptime():
    """
    Retrieves system uptime on Windows.
    Returns a string describing uptime or raises an exception on failure.
    """
    try:
        result = subprocess.run(
            ["net", "stats", "srv"],
            capture_output=True,
            text=True,
            check=True
        )
        for line in result.stdout.splitlines():
            if "Statistics since" in line:
                return f"System Uptime (since): {line.split('Statistics since')[1].strip()}"
        return "Could not determine uptime on Windows."
    except Exception as e:
        raise RuntimeError(f"Error retrieving uptime on Windows: {e}")

def get_linux_uptime():
    """
    Retrieves system uptime on Linux.
    Returns a string describing uptime or raises an exception on failure.
    """
    try:
        with open("/proc/uptime", "r") as f:
            uptime_seconds = float(f.readline().split()[0])
            hours = int(uptime_seconds // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            seconds = int(uptime_seconds % 60)
            return f"System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds"
    except Exception as e:
        raise RuntimeError(f"Error retrieving uptime on Linux: {e}")

def get_macos_uptime():
    """
    Retrieves system uptime on macOS.
    Returns a string describing uptime or raises an exception on failure.
    """
    try:
        result = subprocess.run(
            ["uptime"],
            capture_output=True,
            text=True,
            check=True
        )
        return f"System Uptime: {result.stdout.strip()}"
    except Exception as e:
        raise RuntimeError(f"Error retrieving uptime on macOS: {e}")

def print_system_uptime():
    """
    Detects OS and prints the system uptime using the appropriate method.
    Handles exceptions and prints errors if they occur.
    """
    system = platform.system()
    try:
        if system == "Windows":
            print(get_windows_uptime())
        elif system == "Linux":
            print(get_linux_uptime())
        elif system == "Darwin":
            print(get_macos_uptime())
        else:
            print(f"Unsupported OS: {system}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print_system_uptime()
