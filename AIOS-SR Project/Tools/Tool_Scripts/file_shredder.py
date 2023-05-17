import os

def run_file_shredder():
    file_path = input("Enter the file path to be shredded: ")
    if os.path.exists(file_path):
        # Perform the file shredding logic here
        print(f"Shredding file: {file_path}")
        # Your file shredding code goes here
    else:
        print(f"File not found: {file_path}")


# Call the shred_file() function
if __name__ == "__main__":
  shred_file()
