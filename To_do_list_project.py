
from tkinter import *
from tkinter import messagebox

#Create the window
window = Tk()
window.title("To-Do List Application")
window.geometry("600x600")
window.config(bg="lightgray")

#Title name
title_name = Label(window, text="To-Do List Application", font=("Helvetica", 18, "bold"), bg="lightgray")
title_name.pack(pady=10)

#Frame to hold the task list and buttons
frame_task = Frame(window, bg="lightgray")
frame_task.pack(pady=10)

#Create a holder in frame_task for the items in a listbox with a Scrollbar
scrollbar_task = Scrollbar(frame_task, orient=VERTICAL)
listbox_task = Listbox(frame_task, bg="white", fg="black", height=15, width=45, font=("Helvetica", 12), yscrollcommand=scrollbar_task.set, selectbackground="lightblue")
scrollbar_task.config(command=listbox_task.yview)

scrollbar_task.pack(side=RIGHT, fill=Y)
listbox_task.pack(side=LEFT, fill=BOTH)

#Entry widget to add new tasks
task_input = Entry(window, width=50, font=("Helvetica", 12))
task_input.pack(pady=10)

#Functions for the buttons: add task, delete task, mark task as completed, and clear all tasks
def entertask():
    task = task_input.get().strip() 
    if task:
        if task not in listbox_task.get(0, END): 
            listbox_task.insert(END, task)
            task_input.delete(0, END) 
            messagebox.showinfo("Task Added", "The task '" + task + "' has been added successfully.")
        else:
            messagebox.showwarning("Warning", "The task '" + task + "' already exists.")
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def deletetask():
    try:
        selected_task_index = listbox_task.curselection()[0]
        task = listbox_task.get(selected_task_index)
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete the task: '" + task + "'?")
        if confirm:
            listbox_task.delete(selected_task_index)
            messagebox.showinfo("Task Deleted", "The task '" + task + "' has been deleted successfully.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def markcompleted():
    try:
        selected_task_index = listbox_task.curselection()[0]
        task = listbox_task.get(selected_task_index)
        listbox_task.delete(selected_task_index)
        if "✔" not in task:
            listbox_task.insert(END, task + " ✔")
            messagebox.showinfo("Task Completed", "The task '" + task + "' has been marked as completed.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed")

def clearalltasks():
    confirm = messagebox.askyesno("Clear All Tasks", "Are you sure you want to delete all tasks?")
    if confirm:
        listbox_task.delete(0, END)
        messagebox.showinfo("Tasks Cleared", "All tasks have been cleared successfully.")

#Create widget buttons: add task, delete task, mark task as completed, and clear all tasks
button_frame = Frame(window, bg="lightgray")
button_frame.pack(pady=20)

add_task_button = Button(button_frame, text="Add Task", width=18, command=entertask, font=("Helvetica", 12), bg="green", fg="white")
add_task_button.grid(row=0, column=0, padx=5, pady=5)

delete_button = Button(button_frame, text="Delete Selected Task", width=18, command=deletetask, font=("Helvetica", 12), bg="red", fg="white")
delete_button.grid(row=0, column=1, padx=5, pady=5)

mark_button = Button(button_frame, text="Mark as Completed", width=18, command=markcompleted, font=("Helvetica", 12), bg="blue", fg="white")
mark_button.grid(row=1, column=0, padx=5, pady=5)

clear_button = Button(button_frame, text="Clear All Tasks", width=18, command=clearalltasks, font=("Helvetica", 12), bg="gray", fg="white")
clear_button.grid(row=1, column=1, padx=5, pady=5)


window.mainloop()