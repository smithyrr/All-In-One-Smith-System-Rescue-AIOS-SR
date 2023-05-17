import sys
import subprocess
sys.path.append("/mnt/d/AIOS-SR/AIOS-SR Project")

from Tools.Recovery_Tools.system_recovery_tool import run_system_recovery_tool
from Tools.Diagnostic_Tools.diagnostics_tool import run_diagnostics_tool
from Tools.Tool_Scripts.parted_tool import run_parted_tool


# Placeholder functions for the new features

def run_gparted_tool():
    print("Running GParted Tool...")
    print("======================")
    device_path = input("Enter the device path (e.g., /dev/sda): ")

    while True:
        print("\n=== GParted Tool Menu ===")
        print("1. Print Disk Partitions")
        print("2. Create a Partition")
        print("3. Delete a Partition")
        print("4. Resize a Partition")
        print("5. Move a Partition")
        print("6. Copy a Partition")
        print("7. Set Partition Flags")
        print("8. Create File System")
        print("9. Check File System")
        print("10. Repair File System")
        print("11. Mount/Unmount Partition")
        print("12. Verify Partition Alignment")
        print("13. Back to Main Menu")

        choice = input("Choose an option: ")

        if choice == "1":
            print_disk_partitions(device_path)
        elif choice == "2":
            create_partition(device_path)
        elif choice == "3":
            delete_partition(device_path)
        elif choice == "4":
            resize_partition(device_path)
        elif choice == "5":
            move_partition(device_path)
        elif choice == "6":
            copy_partition(device_path)
        elif choice == "7":
            set_partition_flags(device_path)
        elif choice == "8":
            create_file_system(device_path)
        elif choice == "9":
            check_file_system(device_path)
        elif choice == "10":
            repair_file_system(device_path)
        elif choice == "11":
            mount_unmount_partition(device_path)
        elif choice == "12":
            verify_partition_alignment(device_path)
        elif choice == "13":
            break
        else:
            print("Invalid choice. Please try again.")

    print("GParted tool execution completed.")

def print_disk_partitions(device_path):
    print(f"Disk partitions for {device_path}:")
    subprocess.run(["gparted", device_path])

def create_partition(device_path):
    print("Creating a new partition:")
    # Placeholder logic for creating a new partition

def delete_partition(device_path):
    print("Deleting a partition:")
    # Placeholder logic for deleting a partition

def resize_partition(device_path):
    print("Resizing a partition:")
    # Placeholder logic for resizing a partition

def move_partition(device_path):
    print("Moving a partition:")
    # Placeholder logic for moving a partition

def copy_partition(device_path):
    print("Copying a partition:")
    # Placeholder logic for copying a partition

def set_partition_flags(device_path):
    print("Setting partition flags:")
    # Placeholder logic for setting partition flags

def create_file_system(device_path):
    print("Creating a file system:")
    # Placeholder logic for creating a file system

def check_file_system(device_path):
    print("Checking file system:")
    # Placeholder logic for checking a file system

def repair_file_system(device_path):
    print("Repairing file system:")
    # Placeholder logic for repairing a file system

def mount_unmount_partition(device_path):
    print("Mounting/Unmounting a partition:")
    # Placeholder logic for mounting/unmounting a partition

def verify_partition_alignment(device_path):
    print("Verifying partition alignment:")
    # Placeholder logic for verifying partition alignment

def display_menu():
    print("1. System Recovery")
    print("2. Diagnostics")
    print("3. Data Recovery")
    print("4. System Monitoring")
    print("5. Software Update Checker")
    print("6. Performance Optimization")
    print("7. Malware Scanner")
    print("8. File Shredder")
    print("9. Event Log Viewer")
    print("10. Remote Access")
    print("11. System Information")
    print("12. Scheduled Tasks")
    print("13. Log and History Management")
    print("14. User Authentication")
    print("15. Exit")

    choice = input("Choose an option: ")
    return choice

def run_tool(choice):
    if choice == "1":
        run_system_recovery_tool()
    elif choice == "2":
        print("Running diagnostics tool...")
        run_diagnostics_tool()
    elif choice == "3":
        print("Running data recovery tool...")
        run_data_recovery_tool()
    elif choice == "4":
        print("Running system monitoring tool...")
        run_system_monitoring_tool()
    elif choice == "5":
        print("Running software update tool...")
        run_software_update_tool()
    elif choice == "6":
        print("Running performance optimization tool...")
        run_performance_optimization_tool()
    elif choice == "7":
        print("Running malware scanner tool...")
        run_malware_scanner_tool()
    elif choice == "8":
        print("Running file shredder tool...")
        run_file_shredder_tool()
    elif choice == "9":
        print("Running event log viewer tool...")
        run_event_log_viewer_tool()
    elif choice == "10":
        print("Running remote access tool...")
        run_remote_access_tool()
    elif choice == "11":
        print("Running system information tool...")
        run_system_information_tool()
    elif choice == "12":
        print("Running scheduled tasks tool...")
        run_scheduled_tasks_tool()
    elif choice == "13":
        print("Running log and history management tool...")
        run_log_history_management_tool()
    elif choice == "14":
        print("Running user authentication tool...")
        run_user_authentication_tool()
    elif choice == "15":
        sys.exit("Exiting...")
    else:
        print("Invalid choice. Please try again.")

def main():
    while True:
        choice = display_menu()
        if choice == "1" or choice == "2":
            run_tool(choice)
        elif choice == "3":
            run_data_recovery_tool()
        elif choice == "4":
            run_system_monitoring_tool()
        elif choice == "5":
            run_software_update_tool()
        elif choice == "6":
            run_performance_optimization_tool()
        elif choice == "7":
            run_malware_scanner_tool()
        elif choice == "8":
            run_file_shredder_tool()
        elif choice == "9":
            run_event_log_viewer_tool()
        elif choice == "10":
            run_remote_access_tool()
        elif choice == "11":
            run_system_information_tool()
        elif choice == "12":
            run_scheduled_tasks_tool()
        elif choice == "13":
            run_log_history_management_tool()
        elif choice == "14":
            run_user_authentication_tool()
        elif choice == "15":
            sys.exit("Exiting...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
