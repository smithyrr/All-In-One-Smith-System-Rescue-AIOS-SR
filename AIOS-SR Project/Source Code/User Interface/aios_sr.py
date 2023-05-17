import sys
import os

# Add the project directory to the module search path
project_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "AIOS-SR Project")
sys.path.append(project_dir)

# Check the operating system and add the appropriate path
if sys.platform.startswith("linux"):
    sys.path.append("/mnt/d/AIOS-SR/AIOS-SR Project")
elif sys.platform.startswith("win"):
    sys.path.append("D:\\AIOS-SR\\AIOS-SR Project")

# Import necessary modules from the project
from import_tools import *


def display_data_recovery_menu():
    """Display the menu for data recovery options."""
    print("=== Data Recovery ===")
    print("1. TestDisk")
    print("2. PhotoRec")
    print("3. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice


def run_data_recovery_tool():
    """Run the data recovery tool based on the user's choice."""
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
    """Display the menu for system monitoring options."""
    print("\n=== System Monitoring ===")
    print("1. Monitor CPU Usage")
    print("2. Monitor Memory Usage")
    print("3. Monitor Disk Usage")
    print("4. Monitor Network Statistics")
    print("5. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice


def run_system_monitoring_tool():
    """Run the system monitoring tool based on the user's choice."""
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


# Define more functions and menus...

def display_menu():
    """Display the main menu options."""
    print("=== Tools ===")
    print("1. System Recovery")
    print("2. Diagnostics")
    print("3. Data Recovery-offline")
    print("4. System Monitoring")
    print("5. Software Update Checker")
    print("\n=== Utilities ===")
    print("6. Malware Scanner")
    print("7. File Shredder")
    print("8. Event Log Viewer")
    print("9. Remote Access-offline")
    print("10. System Information")
    print("11. Scheduled Tasks-offline")
    print("12. Log and History Management-offline")
    print("13. User Authentication-offline")
    print("\n14. Exit")

    choice = input("Choose an option: ")
    return choice


def run_tool(choice):
    """Run the selected tool based on the user's choice."""
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
        while True:
            print("=== Software Update Checker ===")
            print("1. Windows Update Checker")
            print("2. Linux Update Checker")
            print("3. Back to Main Menu")
            update_choice = input("Choose an option: ")

            if update_choice == "1":
                print("Running Windows update checker...")
                run_windows_update_checker()
            elif update_choice == "2":
                print("Running Linux update checker...")
                run_linux_update_checker()
            elif update_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "6":
        print("Running malware scanner tool...")
        run_malware_scanner_tool()
    elif choice == "7":
        while True:
            print("=== File Shredder ===")
            print("1. Run File Shredder")
            print("2. Back to Main Menu")
            file_choice = input("Choose an option: ")

            if file_choice == "1":
                print("Running file shredder tool...")
                run_file_shredder()
                break
            elif file_choice == "2":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "8":
        while True:
            print("=== Event Log Viewer ===")
            print("1. Windows Event Log Viewer")
            print("2. Linux Event Log Viewer")
            print("3. Back to Main Menu")
            event_choice = input("Choose an option: ")

            if event_choice == "1":
                print("Running Windows Event Log Viewer...")
                run_event_log_viewer_windows()
                break
            elif event_choice == "2":
                print("Running Linux Event Log Viewer...")
                run_event_log_viewer_linux()
                break
            elif event_choice == "3":
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == "9":
        print("Running remote access tool...")
        run_remote_access_tool()
    elif choice == "10":
        print("Running system information tool...")
        run_system_information_tool()
    elif choice == "11":
        print("Running scheduled tasks tool...")
        run_scheduled_tasks_tool()
    elif choice == "12":
        print("Running log and history management tool...")
        run_log_history_management_tool()
    elif choice == "13":
        print("Running user authentication tool...")
        run_user_authentication_tool()
    elif choice == "14":
        sys.exit("Exiting...")
    else:
        print("Invalid choice. Please try again.")


def main():
    """Main function to run the program."""
    while True:
        choice = display_menu()
        run_tool(choice)


if __name__ == "__main__":
    main()
