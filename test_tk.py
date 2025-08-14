import tkinter as tk

# --- Functions ---
def on_button_click():
    label.config(text="Button clicked!")

# --- Main Window ---
root = tk.Tk()
root.title("My First Tkinter App")
root.geometry("300x200")  # width x height

# --- Center the window ---
root.update_idletasks()
width = root.winfo_width()
height = root.winfo_height()
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry(f"{width}x{height}+{x}+{y}")

# --- Widgets ---
label = tk.Label(root, text="Welcome to Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=10)

# --- Run App ---
root.mainloop()