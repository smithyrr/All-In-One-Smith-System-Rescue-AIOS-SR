import sys
import subprocess
import os


# Get the absolute path of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))


# Add the project directory to the module search path
project_dir = os.path.join(script_dir, "Tools")
sys.path.append(project_dir)

# Check the operating system
if sys.platform.startswith("linux"):
    sys.path.append("/mnt/d/AIOS-SR/AIOS-SR Project")
elif sys.platform.startswith("win"):
    sys.path.append("D:\\AIOS-SR\\AIOS-SR Project")

from import_tools import *

# Removed placeholder run_testdisk_tool and run_photorec_tool

def display_data_recovery_menu():
    print("=== Data Recovery ===")
    print("1. TestDisk")
    print("2. PhotoRec")
    print("3. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice

def run_data_recovery_tool():
    while True:
        choice = display_data_recovery_menu()

        if choice == "1":
            run_testdisk_tool()
        elif choice == "2":
            run_photorec_tool()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def display_system_monitoring_menu():
    print("\n=== System Monitoring ===")
    print("1. Monitor CPU Usage")
    print("2. Monitor Memory Usage")
    print("3. Monitor Disk Usage")
    print("4. Monitor Network Statistics")
    print("5. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice


def run_system_monitoring_tool():
    while True:
        choice = display_system_monitoring_menu()

        if choice == "1":
            monitor_cpu_usage()
        elif choice == "2":
            monitor_memory_usage()
        elif choice == "3":
            monitor_disk_usage()
        elif choice == "4":
            monitor_network_stats()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def run_software_update_tool():
    print("Running Software Update Checker...")
    print("==================================")
    # Placeholder logic for software update tool

def run_performance_optimization_tool():
    print("Running Performance Optimization Tool...")
    print("======================================")
    # Placeholder logic for performance optimization tool

def run_malware_scanner_tool():
    print("Running Malware Scanner Tool...")
    print("==============================")
    # Placeholder logic for malware scanner tool

def run_file_shredder_tool():
    print("Running File Shredder Tool...")
    print("============================")
    # Placeholder logic for file shredder tool

def run_event_log_viewer_tool():
    print("Running Event Log Viewer Tool...")
    print("===============================")
    # Placeholder logic for event log viewer tool

def run_remote_access_tool():
    print("Running Remote Access Tool...")
    print("============================")
    # Placeholder logic for remote access tool

def run_system_information_tool():
    print("Running System Information Tool...")
    print("=================================")
    # Placeholder logic for system information tool

def run_scheduled_tasks_tool():
    print("Running Scheduled Tasks Tool...")
    print("==============================")
    # Placeholder logic for scheduled tasks tool

def run_log_history_management_tool():
    print("Running Log and History Management Tool...")
    print("==========================================")
    # Placeholder logic for log and history management tool

def run_user_authentication_tool():
    print("Running User Authentication Tool...")
    print("===============================")
    # Placeholder logic for user authentication tool

def run_system_restore_tool():
    print("Running System Restore Tool...")
    print("==============================")
    Tools.Tool_Scripts.system_restore_tool.run_system_restore_tool()

def run_backup_restore_tool():
    print("Running Backup and Restore Tool...")
    print("===============================")
    # Placeholder logic for backup and restore tool

def display_system_recovery_menu():
    print("=== System Recovery ===")
    print("1. GParted")
    print("2. System Restore Tool")
    print("3. Backup and Restore Tool")
    print("4. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice

def run_system_recovery_tool():
    while True:
        choice = display_system_recovery_menu()

        if choice == "1":
            run_gparted_tool()  # Call the function to run the GParted tool
        elif choice == "2":
            run_system_restore_tool()  # Call the function to run the System Restore tool
        elif choice == "3":
            run_backup_restore_tool()  # Call the function to run the Backup and Restore tool
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def display_menu():
    print("=== Tools ===")
    print("1. System Recovery")
    print("2. Diagnostics")
    print("3. Data Recovery")
    print("4. System Monitoring")
    print("5. Software Update Checker")

    print("\n=== Utilities ===")
    print("6. Performance Optimization")
    print("7. Malware Scanner")
    print("8. File Shredder")
    print("9. Event Log Viewer")
    print("10. Remote Access")
    print("11. System Information")
    print("12. Scheduled Tasks")
    print("13. Log and History Management")
    print("14. User Authentication")

    print("\n15. Exit")
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
        run_tool(choice)

if __name__ == "__main__":
    main()
