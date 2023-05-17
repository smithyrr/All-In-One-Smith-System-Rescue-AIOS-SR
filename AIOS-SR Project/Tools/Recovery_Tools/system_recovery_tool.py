import parted
import subprocess

def print_disk_partitions(disk):
    print("Disk partitions:")
    partitions = disk.partitions
    for partition in partitions:
        print(f"Partition: {partition.path}")
        print(f"File System Type: {partition.fileSystem.type}")
        print(f"Size: {partition.getLength() / (1024 ** 2)} MB")
        # Add other partition details as needed

def create_partition(disk):
    print("Creating a new partition:")
    partition_size = input("Enter the partition size (e.g., 10GB): ")
    file_system_type = input("Enter the file system type (e.g., ext4): ")
    disk_partition = parted.Partition(disk)
    disk_partition.fileSystem = parted.FileSystem(file_system_type)
    disk_partition.geometry = parted.Geometry(start=parted.size("0%"), length=parted.size(partition_size))
    disk_partition.setFlag(parted.PARTITION_BOOT)
    disk_partition.setFlag(parted.PARTITION_ROOT)
    disk.addPartition(disk_partition)
    print("Partition created successfully.")

def delete_partition(disk):
    print("Deleting a partition:")
    partition_path = input("Enter the partition path to delete (e.g., /dev/sda1): ")
    partition = disk.getPartitionByPath(partition_path)
    if partition:
        disk.removePartition(partition)
        print("Partition deleted successfully.")
    else:
        print("Partition not found.")

def resize_partition(disk):
    print("Resizing a partition:")
    partition_path = input("Enter the partition path to resize (e.g., /dev/sda1): ")
    new_size = input("Enter the new partition size (e.g., 5GB): ")
    partition = disk.getPartitionByPath(partition_path)
    if partition:
        parted.resize(partition, new_size)
        print("Partition resized successfully.")
    else:
        print("Partition not found.")

def format_partition(disk):
    print("Formatting a partition:")
    partition_path = input("Enter the partition path to format (e.g., /dev/sda1): ")
    file_system_type = input("Enter the file system type (e.g., ext4): ")
    subprocess.run(["mkfs", "-t", file_system_type, partition_path])
    print("Partition formatted successfully.")

def clone_disk():
    print("Cloning a disk:")
    source_disk = input("Enter the source disk path (e.g., /dev/sda): ")
    target_disk = input("Enter the target disk path (e.g., /dev/sdb): ")
    subprocess.run(["dd", "if=" + source_disk, "of=" + target_disk, "bs=4M"])
    print("Disk cloned successfully.")

def configure_bootloader():
    print("Configuring bootloader:")
    # Add your bootloader configuration logic here
    # For example, use grub-install or efibootmgr to configure the bootloader

def wipe_disk():
    print("Wiping a disk:")
    disk_path = input("Enter the disk path to wipe (e.g., /dev/sda): ")
    subprocess.run(["shred", "-v", "-n", "1", disk_path])
    print("Disk wiped successfully.")

def run_system_recovery_tool():
    print("Running System Recovery Tool...")
    print("================================")
    device_path = input("Enter the device path (e.g., /dev/sda): ")
    disk = parted.getDevice(device_path)

    while True:
        print("\n=== System Recovery Menu ===")
        print("1. Print Disk Partitions")
        print("2. Create a Partition")
        print("3. Delete a Partition")
        print("4. Resize a Partition")
        print("5. Format a Partition")
        print("6. Clone a Disk")
        print("7. Configure Bootloader")
        print("8. Wipe a Disk")
        print("9. Exit System Recovery Tool")

        choice = input("Choose an option: ")

        if choice == "1":
            print_disk_partitions(disk)
        elif choice == "2":
            create_partition(disk)
        elif choice == "3":
            delete_partition(disk)
        elif choice == "4":
            resize_partition(disk)
        elif choice == "5":
            format_partition(disk)
        elif choice == "6":
            clone_disk()
        elif choice == "7":
            configure_bootloader()
        elif choice == "8":
            wipe_disk()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")

    print("System recovery tool execution completed.")

if __name__ == "__main__":
    run_system_recovery_tool()
