import psutil
import time
import tkinter as tk
from tkinter import messagebox
import threading

root = tk.Tk()
root.title("App Blocker")
root.configure(bg="#2e2e2e")  
root.resizable(False, False)  
root.geometry("400x270")
stop_blocking = False

def onclick_submit():
    global stop_blocking

    try:
        name = app_name_textbox.get()
        if not name:
            messagebox.showerror("Error", "No input entered. Please enter the App name to terminate.")
            return

        name = [app.strip() for app in name.split(",")]
        time_format = var.get()
        duration_str = duration_textbox.get()

        if not duration_str:
            messagebox.showerror("Error", "No duration entered to lock the app for!")
            return

        duration = int(duration_str)
        if time_format == "Minutes":
            duration = duration * 60
        elif time_format == "Hours":
            duration = duration * 60 * 60

        endtime = time.time() + duration

        messagebox.showinfo("Info", f"Apps to be blocked: {name}")

        while endtime > time.time() and not stop_blocking:
            for app in name:
                found = False
                processes = psutil.process_iter(['name'])
                try:
                    for process in processes:
                        if process.info['name'].lower() == app.lower():
                            found = True
                            process.terminate()
                            process.wait(timeout=3)
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess, AttributeError) as e:
                    print(f"Exception occurred while terminating {app}: {e}")

                if found:
                    print(f"{app} was found running and terminated.")
            time.sleep(2)

        if stop_blocking:
            messagebox.showinfo("Info", "Blocking has been stopped manually.")
        else:
            messagebox.showinfo("Info", "The apps are no longer locked!")

    except ValueError:
        messagebox.showerror("Error", "Invalid input for duration. Please enter a number.")

def start_blocking():
    global stop_blocking
    stop_blocking = False
    threading.Thread(target=onclick_submit).start()

def stop_blocking_process():
    global stop_blocking
    stop_blocking = True


main_frame = tk.Frame(root, bg="#2e2e2e")
main_frame.pack(anchor="w", padx=20, pady=20)


app_name_label = tk.Label(
    main_frame, 
    text="Enter the name(s) of the app(s) to block\n(comma separated, e.g.: notepad.exe, msedge.exe):",
    bg="#2e2e2e",
    fg="white",
    anchor="w",
    justify="left"
)
app_name_label.pack(anchor="w", pady=5)

app_name_textbox = tk.Entry(main_frame, width=50, bg="#3c3f41", fg="white", insertbackground="white", relief="flat")
app_name_textbox.pack(anchor="w", pady=5)

var = tk.StringVar(value="Hours")

radio_frame = tk.Frame(main_frame, bg="#2e2e2e")
radio1 = tk.Radiobutton(radio_frame, text="Hours", variable=var, value="Hours", bg="#2e2e2e", fg="white", selectcolor="#2e2e2e", activebackground="#2e2e2e")
radio2 = tk.Radiobutton(radio_frame, text="Minutes", variable=var, value="Minutes", bg="#2e2e2e", fg="white", selectcolor="#2e2e2e", activebackground="#2e2e2e")
radio1.pack(side="left", padx=5)
radio2.pack(side="left", padx=5)
radio_frame.pack(anchor="w", pady=5)

duration_label = tk.Label(main_frame, text="Please enter your duration:", bg="#2e2e2e", fg="white", anchor="w", justify="left")
duration_label.pack(anchor="w", pady=5)

duration_textbox = tk.Entry(main_frame, width=20, bg="#3c3f41", fg="white", insertbackground="white", relief="flat")
duration_textbox.pack(anchor="w", pady=15)
button_frame = tk.Frame(main_frame, bg="#2e2e2e")
submit_button = tk.Button(main_frame, text="Start Blocking", command=start_blocking, bg="#404040", fg="white", activebackground="#505050", activeforeground="white", relief="flat")
submit_button.pack(side="left")

quit_button = tk.Button(main_frame, text="Quit Blocking", command=stop_blocking_process, bg="#404040", fg="white", activebackground="#505050", activeforeground="white", relief="flat")
quit_button.pack(side="left",padx=10)
button_frame.pack(anchor="w", pady=5)


root.mainloop()
