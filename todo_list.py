import tkinter as tk
from tkinter import messagebox

# Function to center the window on the screen
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Function to make the window draggable
def make_draggable(window):
    window.bind("<Button-1>", start_drag)
    window.bind("<B1-Motion>", drag_window)

def start_drag(event):
    global x_offset, y_offset
    x_offset = event.x
    y_offset = event.y

def drag_window(event):
    x = root.winfo_x() - x_offset + event.x
    y = root.winfo_y() - y_offset + event.y
    root.geometry(f"+{x}+{y}")

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                tasks.append(line.strip())
                task_listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass  # If the file doesn't exist, do nothing

# Close Window
def close_window():
    save_tasks()  # Save tasks before closing
    root.destroy()

# Function to minimize the window
def minimize_window():
    root.iconify()  # Minimize the window to taskbar

# Create the main application window
root = tk.Tk()
root.title("Modern To-Do List")

# Set the window to not be always on top
root.overrideredirect(True)

# Center the window and set dimensions
app_width, app_height = 350, 500  # Increased width for more space
center_window(root, app_width, app_height)

# Make the window draggable
make_draggable(root)

# Style settings
root.configure(bg="#023020")
font_large = ("CaslonOpnface BT", 16, "bold")
font_medium = ("CaslonOpnface BT", 14)

# Task list
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    if task.strip():
        tasks.append(task)
        update_task_list()
        save_tasks()  # Auto-save after adding
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to handle adding a task when pressing Enter
def add_task_on_enter(event):
    add_task()

# Function to delete a selected task
def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_index = selected_task[0]
        tasks.pop(task_index)
        update_task_list()
        save_tasks()  # Auto-save after deleting
    else:
        messagebox.showwarning("Warning", "No task selected!")

# Function to clear all tasks
def clear_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?"):
        tasks.clear()
        update_task_list()
        save_tasks()  # Auto-save after clearing

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Header Frame
header_frame = tk.Frame(root, bg="#023020")
header_frame.pack(fill=tk.X)

header_buttons_frame = tk.Frame(header_frame, bg="#023020")
header_buttons_frame.pack(side=tk.RIGHT)

minimize_button = tk.Button(header_buttons_frame, text="--", command=minimize_window, font=("Arial", 14), bg="#023020", fg="yellow", relief=tk.FLAT)
minimize_button.pack(side=tk.LEFT)

close_button = tk.Button(header_buttons_frame, text="X", command=close_window, font=("Arial", 14), bg="#023020", fg="red", relief=tk.FLAT)
close_button.pack(side=tk.LEFT)

header_label = tk.Label(
    header_frame, text="To-Do List", font=font_large, bg="#023020", fg="white"
)
header_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#023020")
input_frame.pack(pady=20)

task_entry = tk.Entry(input_frame, width=22, font=font_medium, bd=2, relief=tk.GROOVE)
task_entry.grid(row=0, column=0, padx=10)

add_button = tk.Button(
    input_frame,
    text="Add Task",
    width=6,
    bg="#4CAF50",
    fg="white",
    font=font_medium,
    relief=tk.FLAT,
    command=add_task,
)
add_button.grid(row=0, column=1)

# Bind the "Enter" key to the add_task_on_enter function
task_entry.bind("<Return>", add_task_on_enter)

# Task List Frame
task_list_frame = tk.Frame(root, bg="#023020")
task_list_frame.pack(pady=20)

task_listbox = tk.Listbox(
    task_list_frame,
    width=30,  # Fixed width
    height=10,
    font=font_medium,
    bd=2,
    relief=tk.GROOVE,
    bg="#023020",
    fg="white"
)
task_listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(task_list_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_listbox.yview)

# Buttons Frame
button_frame = tk.Frame(root, bg="#023020")
button_frame.pack(pady=20)

delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    width=8,
    bg="black",
    fg="white",
    font=font_medium,
    relief=tk.FLAT,
    command=delete_task,
)
delete_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(
    button_frame,
    text="Clear All",
    width=8,
    bg="#FF9800",
    fg="white",
    font=font_medium,
    relief=tk.FLAT,
    command=clear_tasks,
)
clear_button.grid(row=0, column=1, padx=10)

# Load tasks on startup
load_tasks()

# Run the application
root.mainloop()
