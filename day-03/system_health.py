import psutil
import sys

"""Get current CPU usage percentage"""
def get_cpu_usage():
    try:
        return psutil.cpu_percent(interval=1)
    except Exception as error:
        print(f"Error reading CPU: {error}")
        return None

"""Get current memory usage"""
def get_memory_usage():
    try:
        return psutil.virtual_memory()
    except Exception as error:
        print(f"Error reading memory: {error}")
        return None

"""Get current disk usage"""
def get_disk_usage(path='/'):
    try:
        return psutil.disk_usage(path)
    except Exception as error:
        print(f"Error reading disk: {error}")
        return None

"""Get and validate user input"""
def get_user_input(value):
    try:
        user_value = int(input(value))
        if not 0 <= user_value <= 100:
            print(f"Invalid input. Please enter a value between 0 and 100.")
            return get_user_input(value)
        return user_value
    except ValueError:
        print(f"Invalid input. Please enter a valid integer.")
        return get_user_input(value)
    except KeyboardInterrupt:
        print("\nOperation cancelled.")
        sys.exit(0)

"""Convert bytes to GB"""
def format_bytes(bytes_value):
    return bytes_value / (1024 ** 3)

"""Display a metric with alert if threshold exceeded"""
def display_metric(metric_name, usage_percent, used, total, threshold):
    print(f"\n{metric_name}:")
    print(f"Usage: {usage_percent}% (Threshold: {threshold}%)")
    print(f"Used: {used:.2f} GB / Total: {total:.2f} GB")
    
    if usage_percent > threshold:
        print(f"ALERT: {metric_name} exceeds threshold!")
    else:
        print(f"Status: {metric_name} is normal")

"""Check and display all system metrics"""
def check_system_health(cpu_threshold, memory_threshold, disk_threshold):
    print("\nSYSTEM HEALTH CHECK")
    
    # Check CPU
    cpu_usage = get_cpu_usage()
    if cpu_usage is not None:
        display_metric("CPU", cpu_usage, cpu_usage, 100, cpu_threshold)
    
    # Check Memory
    memory = get_memory_usage()
    if memory is not None:
        used_gb = format_bytes(memory.used)
        total_gb = format_bytes(memory.total)
        display_metric("Memory", memory.percent, used_gb, total_gb, memory_threshold)
    
    # Check Disk
    disk = get_disk_usage()
    if disk is not None:
        used_gb = format_bytes(disk.used)
        total_gb = format_bytes(disk.total)
        display_metric("Disk", disk.percent, used_gb, total_gb, disk_threshold)
    
    print("\nHealth check completed")


def main():
    try:
        print("\nSYSTEM HEALTH MONITORING TOOL\n")
        
        # Get thresholds from user
        cpu_threshold = get_user_input("Enter CPU threshold (0-100): ")
        memory_threshold = get_user_input("Enter Memory threshold (0-100): ")
        disk_threshold = get_user_input("Enter Disk threshold (0-100): ")
        
        # Perform health check
        check_system_health(cpu_threshold, memory_threshold, disk_threshold)
    
    except Exception as error:
        print(f"\nUnexpected error: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
