import psutil

def monitor_cpu_usage():
    while True:
        cpu_percent = psutil.cpu_percent(percpu=True)
        cpu_freq = psutil.cpu_freq()
        cpu_count = psutil.cpu_count()

        cpu_load = psutil.getloadavg()

        sensors_temperatures = psutil.sensors_temperatures()
        cpu_temperature = sensors_temperatures.get('coretemp')[0].current if 'coretemp' in sensors_temperatures else None

        print("=== CPU Information ===")
        print("CPU Usage:")
        for i, usage in enumerate(cpu_percent):
            print(f"  Core {i+1}: {usage}%")
        print(f"Average CPU Usage: {sum(cpu_percent) / len(cpu_percent):.2f}%")
        print(f"CPU Frequency: {cpu_freq.current:.2f} MHz")
        print(f"Number of CPU Cores: {cpu_count}")
        if cpu_temperature is not None:
            print(f"CPU Temperature: {cpu_temperature:.2f} °C")
        print(f"CPU Load: {cpu_load}")

        if max(cpu_percent) > 80:
            print("Warning: High CPU usage detected!")

        choice = input("Press 'q' to quit or any other key to continue: ")
        if choice.lower() == "q":
            break

# Example usage
if __name__ == "__main__":
    monitor_cpu_usage()
