import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import queue
import csv

# Global variables to store user role and username
user_role = None
student_name = None
query_app = None
login_window = None
role_var = None
admin_username = admin
admin_password = admin
admin_app = None

# Create a shared task queue
task_queue = queue.PriorityQueue()

# Function to simulate scheduling a task
def schedule_task(query, priority, category)
    time.sleep(2)  # Simulate task execution
    task_info = fQuery {query} (Category {category}) with Priority {priority}
    print(task_info)

# Function to process tasks from the queue
def process_tasks()
    while True
        try
            priority, task_info = task_queue.get(block=False)
            print(fProcessing task {task_info})
            schedule_task(task_info.split(, ))
        except queue.Empty
            break

# Function to export tasks to a CSV file
def export_to_csv()
    if not task_queue.empty()
        with open(queries.csv, w, newline=) as file
            writer = csv.writer(file)
            writer.writerow([Category, Priority, Query])
            while not task_queue.empty()
                priority, task_info = task_queue.get()
                category, query = task_info.split(, )
                writer.writerow([category, priority, query])
        messagebox.showinfo(Export Completed, All queries have been exported.)
    else
        messagebox.showerror(Error, There are no queries to export.)

# Function to resolve a query
def resolve_query()
    query = query_entry.get()
    priority = priority_entry.get()
    student_name = student_name_entry.get()
    
    if query and priority
        try
            priority = int(priority)
            if 1 = priority = 10
                category = category_var.get()
                task_info = f{query}, {priority}, {category}
                task_queue.put((priority, task_info))
                messagebox.showinfo(Query Resolved, fQuery '{query}' scheduled with Priority {priority} in category {category})
            else
                messagebox.showerror(Error, Priority must be between 1 and 10.)
        except ValueError
            messagebox.showerror(Error, Priority must be an integer.)
    else
        messagebox.showerror(Error, Please fill in all fields.)

# Function to open the query screen
def query_screen()
    global query_app

    login_window.destroy()
    query_app = tk.Tk()
    query_app.title(Student Query Resolver with Task Queuing and Prioritization)

    # Styling
    query_app.configure(bg=#f0f0f0)

    # Create a label and entry for the student's name
    global student_name_entry
    tk.Label(query_app, text=Your Name, bg=#f0f0f0).pack()
    student_name_entry = ttk.Entry(query_app)
    student_name_entry.pack()

    # Create a label and entry for the query
    global query_entry
    tk.Label(query_app, text=Enter your query, bg=#f0f0f0).pack()
    query_entry = ttk.Entry(query_app)
    query_entry.pack()

    # Create a label and entry for the priority
    global priority_entry
    tk.Label(query_app, text=Enter query priority (1-10), bg=#f0f0f0).pack()
    priority_entry = ttk.Entry(query_app)
    priority_entry.pack()

    # Create radio buttons for category selection
    global category_var
    category_var = tk.StringVar(value=Technical)  # Default selection
    tk.Label(query_app, text=Select Query Category, bg=#f0f0f0).pack()
    categories = [Technical, Maintenance, Hostel, Library, Faculty]
    for category in categories
        tk.Radiobutton(query_app, text=category, variable=category_var, value=category, bg=#f0f0f0).pack()

    # Create a button to resolve the query
    ttk.Button(query_app, text=Resolve Query, command=resolve_query).pack()

    # Create a Back button to return to the login screen
    ttk.Button(query_app, text=Back, command=back_to_login).pack()

    query_app.mainloop()

# Function to return to the login screen
def back_to_login()
    query_app.destroy()
    login_screen()

# Function to handle login and show the query screen
def login_and_open_query_screen()
    global user_role
    user_role = role_var.get()
    if user_role == Student
        query_screen()
    elif user_role == Admin
        admin_login_screen()

# Function to open the admin login screen
def admin_login_screen()
    for widget in login_window.winfo_children()
        widget.destroy()

    tk.Label(login_window, text=Admin Login).pack()
    tk.Label(login_window, text=Username).pack()
    username_entry = ttk.Entry(login_window)
    username_entry.pack()
    tk.Label(login_window, text=Password).pack()
    password_entry = ttk.Entry(login_window, show=)
    password_entry.pack()

    def authenticate()
        entered_username = username_entry.get()
        entered_password = password_entry.get()
        if entered_username == admin_username and entered_password == admin_password
            messagebox.showinfo(Success, Admin login successful!)
        else
            messagebox.showerror(Authentication Failed, Incorrect username or password.)

    ttk.Button(login_window, text=Login, command=authenticate).pack()

# Function to create the main login screen
def login_screen()
    global login_window, role_var

    login_window = tk.Tk()
    login_window.title(Login)
    login_window.geometry(300x200)
    login_window.configure(bg=#f0f0f0)

    tk.Label(login_window, text=Select your role, bg=#f0f0f0).pack()

    role_var = tk.StringVar(value=Student)
    tk.Radiobutton(login_window, text=Student, variable=role_var, value=Student, bg=#f0f0f0).pack()
    tk.Radiobutton(login_window, text=Admin, variable=role_var, value=Admin, bg=#f0f0f0).pack()

    ttk.Button(login_window, text=Log In, command=login_and_open_query_screen).pack()

    login_window.mainloop()

# Start the application
login_screen()
