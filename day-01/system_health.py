import psutil

def check_system_health(cpu_thresold, memory_thresold, disk_thresold):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

    print(f"CPU Usage: {cpu_usage}%")
    if (cpu_usage > cpu_thresold):
        print(f"Alert! CPU usage is at {cpu_usage}%, which exceeds the threshold of {cpu_thresold}%")
    else:
        print(f"CPU usage is within acceptable limits.")
 
    print(f"Memory Usage: {memory_usage.percent}% (Used: {memory_usage.used / (1024 ** 3):.2f} GB, Total: {memory_usage.total / (1024 ** 3):.2f} GB)")
    if (memory_usage.percent > memory_thresold):
        print(f"Alert! Memory usage is at {memory_usage.percent}%, which exceeds the threshold of {memory_thresold}%")
    else:
        print(f"Memory usage is within acceptable limits.")

    print(f"Disk Usage: {disk_info.percent}% (Used: {disk_info.used / (1024 ** 3):.2f} GB, Total: {disk_info.total / (1024 ** 3):.2f} GB)")
    if (disk_info.percent > disk_thresold):
        print(f"Alert! Disk usage is at {disk_info.percent}%, which exceeds the threshold of {disk_thresold}%")
    else:
        print(f"Disk usage is within acceptable limits.")

cpu_thresold = int(input("Enter CPU usage threshold percentage (e.g., 75 for 75%): "))
memory_thresold = int(input("Enter Memory usage threshold percentage (e.g., 75 for 75%): "))
disk_thresold = int(input("Enter Disk usage threshold percentage (e.g., 90 for 90%): "))

check_system_health(cpu_thresold, memory_thresold, disk_thresold)