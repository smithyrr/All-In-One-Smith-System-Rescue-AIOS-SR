import psutil

def monitor_cpu_usage():
    print(f"CPU usage: {psutil.cpu_percent()}%")
