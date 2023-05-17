import psutil

def monitor_disk_usage():
    disk = psutil.disk_usage('/')
    print(f"Disk usage: {disk.percent}%")
