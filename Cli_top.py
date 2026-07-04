import psutil
import time 
import os
import platform

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_system_info():
    clear_screen()
    print(f"System: {platform.system()}")
    print(f"CPU: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory: {psutil.virtual_memory().percent}%")
    print(f"Disk: {psutil.disk_usage('/').percent}%")
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            print(f"{proc.info['pid']}: {proc.info['name']} - {proc.info['cpu_percent']}%")
        except psutil.NoSuchProcess:
            continue
    print("\nPress 'q' to quit, any other key to refresh...")

def main():
    while True:
        display_system_info()
        if input() == 'q':
            break
        time.sleep(1)

if __name__ == "__main__":
    main()
