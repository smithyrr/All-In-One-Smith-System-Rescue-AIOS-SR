import psutil
import time
import math

def monitor_network_stats():
    while True:
        net_io = psutil.net_io_counters()

        print("=== Network Statistics ===")
        print(f"Bytes Sent: {convert_size(net_io.bytes_sent)}")
        print(f"Bytes Received: {convert_size(net_io.bytes_recv)}")
        print(f"Packets Sent: {net_io.packets_sent}")
        print(f"Packets Received: {net_io.packets_recv}")
        print(f"Error In: {net_io.errin}")
        print(f"Error Out: {net_io.errout}")
        print(f"Drop In: {net_io.dropin}")
        print(f"Drop Out: {net_io.dropout}")
        print(f"Network Connections: {len(psutil.net_connections())}")

        choice = input("Press 'q' to quit or any other key to continue: ")
        if choice.lower() == 'q':
            break

        time.sleep(1)

def convert_size(size_bytes):
    # Convert bytes to appropriate unit (e.g., KB, MB, GB)
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    size = round(size_bytes / p, 2)
    return f"{size} {size_names[i]}"

# Example usage
if __name__ == "__main__":
    monitor_network_stats()
