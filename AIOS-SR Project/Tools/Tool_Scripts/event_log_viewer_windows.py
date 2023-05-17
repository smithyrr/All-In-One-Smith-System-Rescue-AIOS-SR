import subprocess

def run_event_log_viewer_windows():
    print("Running Windows Event Log Viewer...")
    try:
        subprocess.run(["eventvwr.msc"])
    except FileNotFoundError:
        print("The Event Log Viewer is not available on this Windows system.")

# Call the function to run the Windows Event Log Viewer
if __name__ == "__main__":
    run_event_log_viewer_windows()
  


  
