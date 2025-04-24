import psutil
import time

try:
    check_app = input("Enter the name(s) of the app(s) to block \n(comma separated for multiple apps. e.g.: notepad.exe, msedge.exe): ").lower().split(",")
    check_app = [app.strip() for app in check_app]
    if not check_app:
        raise ValueError("No input entered. Please enter the App name to terminate.")
    
    interval = 2
    time_format = int(input("Please select your time format:\n1. Type 1 for minutes.\n2. Type 2 for hours.\n"))
    duration = int(input("Enter the time (in your selected format) you want to lock the app for: "))
    if not duration:
        raise ValueError("No duration entered to lock the app for!")
    if time_format == 1:
        duration = duration * 60
    elif time_format == 2:
        duration = duration * 60 * 60
    endtime = time.time() + duration
    while endtime > time.time():    
        for app in check_app:
            found = False
            processes = psutil.process_iter(['name'])
            try:
                for process in processes:
                    if process.info['name'].lower() == app:
                        found = True
                        process.terminate()
                        process.wait(timeout=3)
                        continue
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, AttributeError):
                print("An exception has occurred.")        
            if found:
                print(f"{app} was found to be running and was terminated.")
            else:
                print(f"{app} is not running.")
        time.sleep(interval) 
        
except ValueError as e:
    print(e)
except TypeError:
    print("the key 'name' doesn't exists.")
except AttributeError:
    print("A process doesn't have a name attribute.")
except psutil.Error:
    print("An exception has occurred.")