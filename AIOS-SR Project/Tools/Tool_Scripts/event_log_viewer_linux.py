import subprocess

def run_event_log_viewer_linux():
    print("Running Linux Event Log Viewer...")
    try:
        subprocess.run(["gnome-system-log"])
    except FileNotFoundError:
        print("The Event Log Viewer is not available on this Linux distribution.")

# Call the function to run the Linux Event Log Viewer
if __name__ == "__main__":
    run_event_log_viewer_linux()
