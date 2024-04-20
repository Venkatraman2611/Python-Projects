from tkinter import *
from pathlib import Path

class ToDoList:
    def __init__(self, root, filename):
        self.tasks = []
        self.root = root
        self.listbox = Listbox(self.root)
        #listbox to show tasks vertically
        self.entry = Entry(self.root)
        self.addButton = Button(self.root, text="Add Task", command=self.add_task)
        self.delButton = Button(self.root, text="Delete Task", command=self.delete_task)
        self.filename = filename

        # Load tasks from file
        self.load_tasks()

        # GUI Layout
        self.entry.pack()
        self.addButton.pack()
        self.listbox.pack()
        self.delButton.pack()

    def add_task(self):
        task = self.entry.get()
        if task != "":
            # self.listbox.insert(END, task)
            self.tasks.append(task)
            self.entry.delete(0, END)
            self.save_tasks()

    def delete_task(self):
        try:
            task_index = self.listbox.curselection()[0]
            del self.tasks[task_index]
            self.listbox.delete(task_index)
            self.save_tasks()
        except IndexError:
            pass

    def load_tasks(self):
        if Path(self.filename).is_file():
            #path denotes file path, and is file checks whether the file exists
            with open(self.filename, 'r') as file:
                #with used to perform actoins and closes after that
                self.tasks = [line.strip() for line in file.readlines()]
                #line.strip takes data from rdlines and remove whitespaces like that
                for task in self.tasks:
                    self.listbox.insert(END, task)

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            file.write('\n'.join(self.tasks))

root = Tk()
root.title("Python To-Do List")
root.geometry("300x400") # Set the window size
filename = "tasks.txt"
to_do_list = ToDoList(root, filename)
root.mainloop()
