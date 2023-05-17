import sys
sys.path.append("/mnt/d/AIOS-SR/AIOS-SR Project")

import platform
import psutil
import socket
import subprocess

def run_diagnostics_tool():
    print("Running Diagnostics Tool...")
    print("===========================")

    while True:
        print("\n=== Diagnostics Menu ===")
        print("1. Check System Performance")
        print("2. Check Hardware Status")
        print("3. Check Network Connectivity")
        print("4. Exit Diagnostics Tool")

        choice = input("Choose an option: ")

        if choice == "1":
            check_system_performance()
        elif choice == "2":
            check_hardware_status()
        elif choice == "3":
            check_network_connectivity()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Diagnostics tool execution completed.")





def run_system_recovery_tool():
    print("Running System Recovery Tool...")
    print("===============================")

    # Perform system recovery tasks here
    print("Performing system recovery tasks...")
    # Add your system recovery logic here

    print("System recovery tasks completed.")

def run_data_recovery_tool():
    print("Running Data Recovery Tool...")
    print("=============================")

    # Perform data recovery tasks here
    print("Performing data recovery tasks...")
    # Add your data recovery logic here

    print("Data recovery tasks completed.")

def check_system_performance():
    print("Checking system performance...")

    # Get CPU usage
    cpu_usage = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_usage}%")

    # Get memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    print(f"Memory Usage: {memory_usage}%")

    # Get disk usage
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    print(f"Disk Usage: {disk_usage}%")

    # Get network usage
    network = psutil.net_io_counters()
    network_usage = network.bytes_sent + network.bytes_recv
    print(f"Network Usage: {network_usage} bytes")

    # You can add more performance checks here

def check_hardware_status():
    print("Checking hardware status...")

    # Get system information
    system = platform.uname()
    print(f"System: {system.system} {system.release}")

    # Get CPU information
    cpu = platform.processor()
    print(f"CPU: {cpu}")

    # Get memory information
    memory = psutil.virtual_memory()
    total_memory = round(memory.total / (1024**3), 2)
    available_memory = round(memory.available / (1024**3), 2)
    used_memory = round(memory.used / (1024**3), 2)
    print(f"Total Memory: {total_memory} GB")
    print(f"Available Memory: {available_memory} GB")
    print(f"Used Memory: {used_memory} GB")

    # Get disk information
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"Partition: {partition.device}")
        disk = psutil.disk_usage(partition.device)
        total_space = round(disk.total / (1024**3), 2)
        used_space = round(disk.used / (1024**3), 2)
        free_space = round(disk.free / (1024**3), 2)
        print(f"Total Space: {total_space} GB")
        print(f"Used Space: {used_space} GB")
        print(f"Free Space: {free_space} GB")

    # You can add more hardware status checks here

def check_network_connectivity():
    print("Checking network connectivity...")

    # Check IP address
    ip_address = subprocess.check_output(['hostname', '-I']).decode().strip()
    print(f"IP Address: {ip_address}")

    # Check default gateway
    default_gateway = subprocess.check_output(['ip', 'route', 'show', 'default']).decode().split()
    if len(default_gateway) > 0:
        default_gateway = default_gateway[2]
        print(f"Default Gateway: {default_gateway}")
    else:
        print("Default Gateway: Not available")

    # Check DNS servers
    dns_servers = subprocess.check_output(['cat', '/etc/resolv.conf']).decode().split('\n')
    dns_servers = [line.split(' ')[1] for line in dns_servers if line.startswith('nameserver')]
    if len(dns_servers) > 0:
        print("DNS Servers:")
        for dns_server in dns_servers:
            print(f"  - {dns_server}")
    else:
        print("DNS Servers: Not available")

    # Check internet connectivity
    try:
        socket.setdefaulttimeout(3)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("www.google.com", 80))
        print("Internet Connectivity: Connected")
    except socket.error as ex:
        print("Internet Connectivity: Disconnected")

def display_menu():
    print("1. System Recovery")
    print("2. Diagnostics")
    print("3. Data Recovery")
    print("4. Exit")
    choice = input("Choose an option: ")
    return choice

def run_tool(choice):
    if choice == "1":
        print("Running system recovery tool...")
        run_system_recovery_tool()
    elif choice == "2":
        print("Running diagnostics tool...")
        run_diagnostics_tool()
    elif choice == "3":
        print("Running data recovery tool...")
        run_data_recovery_tool()
    elif choice == "4":
        sys.exit("Exiting...")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        choice = display_menu()
        run_tool(choice)

if __name__ == "__main__":
    main()
