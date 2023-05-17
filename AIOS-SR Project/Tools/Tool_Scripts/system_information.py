import platform
import sys

def get_system_information():
    system_info = {
        "Operating System": platform.system(),
        "OS Release": platform.release(),
        "OS Version": platform.version(),
        "Architecture": platform.machine(),
        "Processor": platform.processor(),
        "Python Version": sys.version,
    }
    return system_info

def display_system_information(system_info):
    print("=== System Information ===")
    for key, value in system_info.items():
        print(f"{key}: {value}")

def main():
    while True:
        # Get system information
        system_info = get_system_information()

        # Display system information
        display_system_information(system_info)

        # Prompt the user to continue or quit
        choice = input("Press Q to quit or any other key to continue: ")
        if choice.lower() == "q":
            break

if __name__ == "__main__":
    main()
