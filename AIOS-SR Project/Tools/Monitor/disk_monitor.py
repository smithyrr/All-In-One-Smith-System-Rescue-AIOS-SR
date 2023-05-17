import psutil

def monitor_disk_usage():
    while True:
        disk = psutil.disk_usage('/')

        print("=== Disk Usage Information ===")
        print(f"Total Space: {convert_size(disk.total)}")
        print(f"Used Space: {convert_size(disk.used)} ({disk.percent}%)")
        print(f"Free Space: {convert_size(disk.free)}")
        print(f"Space Details:")
        print(f"  - Used: {convert_size(disk.used)}")
        print(f"  - Free: {convert_size(disk.free)}")
        print(f"  - Available: {convert_size(disk.total - disk.used)}")
        print(f"  - Used by System: {convert_size(disk.used - disk.used - disk.free)}")

        disk_io = psutil.disk_io_counters()
        print("\n=== Disk I/O Information ===")
        print(f"Read Count: {disk_io.read_count}")
        print(f"Write Count: {disk_io.write_count}")
        print(f"Read Bytes: {convert_size(disk_io.read_bytes)}")
        print(f"Write Bytes: {convert_size(disk_io.write_bytes)}")

        choice = input("Press 'q' to quit or any other key to continue: ")
        if choice.lower() == 'q':
            break

def convert_size(size_bytes):
    # Convert bytes to appropriate unit (e.g., KB, MB, GB)
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = 0
    while size_bytes >= 1024 and i < len(size_names) - 1:
        size_bytes /= 1024
        i += 1
    size = round(size_bytes, 2)
    return f"{size} {size_names[i]}"

# Example usage
if __name__ == "__main__":
    monitor_disk_usage()
