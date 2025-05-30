import tkinter as tk  # Import the tkinter library for GUI

# Function to handle button clicks
def click(event):
    value = entry.get()  # Get current entry value
    btn_text = event.widget.cget("text")  # Get text of clicked button
    if btn_text == "=":
        try:
            result = str(eval(value))  # Evaluate the expression
            entry.delete(0, tk.END)    # Clear entry
            entry.insert(0, result)    # Show result
        except:
            entry.delete(0, tk.END)
            entry.insert(0, "Error")   # Show error if invalid
    elif btn_text == "C":
        entry.delete(0, tk.END)        # Clear entry if 'C' is pressed
    else:
        entry.insert(tk.END, btn_text) # Add button text to entry

root = tk.Tk()                         # Create main window
root.title("Calculator")               # Set window title

# Entry widget for input/output
entry = tk.Entry(root, font="Arial 20", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# List of calculator buttons
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C"
]

# Place buttons in a grid
row, col = 1, 0
for text in buttons:
    btn = tk.Button(root, text=text, font="Arial 18", width=4, height=2)
    btn.grid(row=row, column=col)
    btn.bind("<Button-1>", click)      # Bind click event
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()                        # Start the GUI event loop