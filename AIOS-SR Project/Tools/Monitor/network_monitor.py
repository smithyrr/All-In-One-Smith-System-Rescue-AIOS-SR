import psutil

def monitor_network_stats():
    net_io = psutil.net_io_counters()
    print(f"Bytes sent: {net_io.bytes_sent}")
    print(f"Bytes received: {net_io.bytes_recv}")
