import psutil

def monitor_memory_usage():
    memory = psutil.virtual_memory()
    print(f"Memory usage: {memory.percent}%")
