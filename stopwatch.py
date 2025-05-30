import tkinter as tk  # Import tkinter for GUI
import time           # Import time for time tracking

# Function to update the stopwatch display
def update():
    if running:
        global counter
        counter += 1
        time_str = time.strftime('%H:%M:%S', time.gmtime(counter))
        label.config(text=time_str)
        root.after(1000, update)  # Call update every 1 second

# Start the stopwatch
def start():
    global running
    if not running:
        running = True
        update()

# Stop the stopwatch
def stop():
    global running
    running = False

# Reset the stopwatch
def reset():
    global counter
    counter = 0
    label.config(text="00:00:00")

# Main window
root = tk.Tk()
root.title("Stopwatch")

counter = 0      # Time counter in seconds
running = False  # Stopwatch state

# Label to show time
label = tk.Label(root, text="00:00:00", font="Arial 40")
label.pack(pady=20)

# Buttons for start, stop, reset
frame = tk.Frame(root)
frame.pack()

start_btn = tk.Button(frame, text="Start", command=start, width=8, font="Arial 14")
start_btn.pack(side="left", padx=5)

stop_btn = tk.Button(frame, text="Stop", command=stop, width=8, font="Arial 14")
stop_btn.pack(side="left", padx=5)

reset_btn = tk.Button(frame, text="Reset", command=reset, width=8, font="Arial 14")
reset_btn.pack(side="left", padx=5)

root.mainloop()