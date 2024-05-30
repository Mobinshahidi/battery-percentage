import psutil
import ctypes
import time

def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)

def check_battery():
    while True:
        battery = psutil.sensors_battery()
        if battery.percent == 100 and battery.power_plugged:
            time_remaining = convertTime(battery.secsleft)
            message = f"Battery is fully charged, please unplugged!\nTime remaining: {time_remaining}"
            title = "Battery Alert"
            ctypes.windll.user32.MessageBoxW(0, message, title, 0)
        time.sleep(60)
        
if __name__ == "__main__":
    check_battery()
