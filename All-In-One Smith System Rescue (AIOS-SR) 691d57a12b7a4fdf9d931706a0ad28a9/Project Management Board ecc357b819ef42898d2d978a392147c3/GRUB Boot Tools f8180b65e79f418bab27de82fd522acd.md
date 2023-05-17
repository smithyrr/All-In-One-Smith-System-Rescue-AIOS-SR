# GRUB Boot Tools

Assign: Tom Deangelis
Checkbox: No
Date: May 17, 2023 → May 24, 2023
Phase: Phase0.1 Setup Enviroment
Status: In progress

# Create the Grub boot Tools

## What is Grub?

Grub is the Linux bootloader, its the menu that runs on start up that allows you to launch an OS. 

## What will the tools look like?

This is going to be used for the items that need to run as their own product and not from within the OS. This should unlock a lot of the UBCD type tools. 

The main tools will be MEMTEST86+, DBAN - Darek’s boot and nuke. 

### Python script example for a py file that will be run to force to OS to boot into a grub lmenu

```python
import os

def restart_and_launch_grub_tool():
    print("Restarting system and launching GRUB tool...")
    # Restart the system
    os.system("sudo reboot")

if __name__ == "__main__":
    restart_and_launch_grub_tool()
```

- We would need to create a menu option with some how to items such as;

User selects option 1 for Memtest86+  > Python prints out “you have selected Memtest, the operating system will now reboot to the Grub loader, Please select Memtest from the list. Are you sure you want to reboot now?…” > When user selects yes the OS will reboot to Grub 

## Installing Actual Products

This will require the following steps. 

1. Obtain the DBAN ISO:
    - Download the DBAN ISO image from the official DBAN website (**[https://dban.org/](https://dban.org/)**).
    - Make sure to select the appropriate version of DBAN for your system.
2. Create a bootable Linux USB:
    - Use a tool like **`dd`** or **`Rufus`** to create a bootable Linux USB with the DBAN ISO.
    - The specific steps may vary depending on your operating system. Refer to the documentation or user guide of the chosen tool for detailed instructions.
3. Modify the bootloader configuration:
    - Locate the bootloader configuration file on the USB drive. In most cases, it will be the GRUB configuration file.
    - Edit the configuration file to add an entry for DBAN.
    - Here's an example entry you can add to the GRUB configuration file:

```
plaintextCopy code
menuentry "DBAN" {
    set root=(hd0,1)
    linux /dban/dban.bzi
    initrd /dban/dban.bzi
}

```

- Adjust the **`set root=(hd0,1)`** line to reflect the correct partition where the DBAN files are located. Modify it as needed to match your specific USB drive's partitioning scheme.
- Ensure that the paths to **`linux`** and **`initrd`** files are correct and point to the location of the DBAN files on the USB drive.
1. Save the changes and test:
    - Save the modified bootloader configuration file.
    - Safely eject the USB drive from your computer.
    - Plug the USB drive into a target machine and boot from it.
    - When the bootloader appears, you should see the DBAN entry you added.
    - Select the DBAN option to boot into the DBAN tool.