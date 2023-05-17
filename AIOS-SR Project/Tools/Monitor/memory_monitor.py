import psutil
import math

def monitor_memory_usage():
    while True:
        memory = psutil.virtual_memory()
        swap = psutil.swap_memory()

        print("=== Memory Information ===")
        print(f"Total Memory: {convert_size(memory.total)}")
        print(f"Available Memory: {convert_size(memory.available)}")
        print(f"Used Memory: {convert_size(memory.used)} ({memory.percent}%)")
        print(f"Free Memory: {convert_size(memory.free)}")
        print(f"Memory Usage Details:")
        print(f"  - Used: {convert_size(memory.used)}")
        print(f"  - Available: {convert_size(memory.available)}")
        print(f"  - Cached: {convert_size(memory.cached)}")
        print(f"  - Buffers: {convert_size(memory.buffers)}")
        print(f"  - Shared: {convert_size(memory.shared)}")
        print(f"Swap Usage:")
        print(f"  - Used: {convert_size(swap.used)}")
        print(f"  - Free: {convert_size(swap.free)}")
        print(f"  - Percent: {swap.percent}%")

        choice = input("Press 'q' to quit or any other key to continue: ")
        if choice.lower() == 'q':
            break

def convert_size(size_bytes):
    # Convert bytes to appropriate unit (e.g., KB, MB, GB)
    if size_bytes == 0:
        return "0B"
    size_names = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    size = round(size_bytes / p, 2)
    return f"{size} {size_names[i]}"

# Example usage
if __name__ == "__main__":
    monitor_memory_usage()
