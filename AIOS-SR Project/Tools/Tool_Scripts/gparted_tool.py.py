import subprocess

def print_disk_partitions():
    print("Disk partitions:")
    # Placeholder logic to print disk partitions using GParted

def create_partition():
    print("Creating a new partition:")
    # Placeholder logic to create a partition using GParted

def delete_partition():
    print("Deleting a partition:")
    # Placeholder logic to delete a partition using GParted

def resize_partition():
    print("Resizing a partition:")
    # Placeholder logic to resize a partition using GParted

def format_partition():
    print("Formatting a partition:")
    # Placeholder logic to format a partition using GParted

def run_gparted_tool():
    print("Running GParted Tool...")
    print("======================")
    
    while True:
        print("\n=== GParted Tool Menu ===")
        print("1. Print Disk Partitions")
        print("2. Create a Partition")
        print("3. Delete a Partition")
        print("4. Resize a Partition")
        print("5. Format a Partition")
        print("6. Exit GParted Tool")

        choice = input("Choose an option: ")

        if choice == "1":
            print_disk_partitions()
        elif choice == "2":
            create_partition()
        elif choice == "3":
            delete_partition()
        elif choice == "4":
            resize_partition()
        elif choice == "5":
            format_partition()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

    print("GParted tool execution completed.")

if __name__ == "__main__":
    run_gparted_tool()
