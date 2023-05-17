import sys
import subprocess
sys.path.append("/mnt/d/AIOS-SR/AIOS-SR Project")

from Tools.Recovery_Tools.system_recovery_tool import run_system_recovery_tool
from Tools.Diagnostic_Tools.diagnostics_tool import run_diagnostics_tool
from Tools.Tool_Scripts.parted_tool import run_parted_tool
from Tools.Tool_Scripts.gparted_tool import run_gparted_tool


# Placeholder functions for the new features
def run_data_recovery_tool():
    print("Running Data Recovery Tool...")
    print("=============================")
    # Placeholder logic for data recovery tool

def run_system_monitoring_tool():
    print("Running System Monitoring Tool...")
    print("================================")
    # Placeholder logic for system monitoring tool

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

def display_system_recovery_menu():
    print("=== System Recovery ===")
    print("1. GParted")
    print("2. Parted")
    print("3. Other System Recovery Tool")
    print("4. Back to Main Menu")

    choice = input("Choose an option: ")
    return choice

def run_system_recovery_tool():
    while True:
        choice = display_system_recovery_menu()

        if choice == "1":
            run_gparted_tool()  # Call the function to run the GParted tool
        elif choice == "2":
            run_parted_tool()  # Call the function to run the Parted tool
        elif choice == "3":
            print("Running other system recovery tool...")
            # Placeholder logic for running other system recovery tool
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

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
        run_tool(choice)

if __name__ == "__main__":
    main()
