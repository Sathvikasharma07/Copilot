import os
import platform
import subprocess

def print_system_uptime():
    """
    Prints the system uptime in a human-readable format.
    """
    system = platform.system()

    if system == "Windows":
        # Use 'net stats srv' and parse output
        try:
            output = subprocess.check_output("net stats srv", shell=True, text=True)
            for line in output.splitlines():
                if "Statistics since" in line:
                    print("System Uptime (since):", line.split("Statistics since")[1].strip())
                    return
            print("Could not determine uptime on Windows.")
        except Exception as e:
            print(f"Error retrieving uptime on Windows: {e}")
    elif system == "Linux":
        # Use /proc/uptime
        try:
            with open("/proc/uptime", "r") as f:
                uptime_seconds = float(f.readline().split()[0])
                hours = int(uptime_seconds // 3600)
                minutes = int((uptime_seconds % 3600) // 60)
                seconds = int(uptime_seconds % 60)
                print(f"System Uptime: {hours} hours, {minutes} minutes, {seconds} seconds")
        except Exception as e:
            print(f"Error retrieving uptime on Linux: {e}")
    elif system == "Darwin":
        # Use 'uptime' command on macOS
        try:
            output = subprocess.check_output(["uptime"], text=True)
            print("System Uptime:", output.strip())
        except Exception as e:
            print(f"Error retrieving uptime on macOS: {e}")
    else:
        print(f"Unsupported OS: {system}")

if __name__ == "__main__":
    print_system_uptime()
