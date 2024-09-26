{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "842e59a0-d53d-4709-9b6a-bba8cc4f77c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import tkinter as tk\n",
    "from tkinter import messagebox, simpledialog, Listbox, Scrollbar\n",
    "\n",
    "class Task:\n",
    "    def __init__(self, title, description, category, completed=False):\n",
    "        self.title = title\n",
    "        self.description = description\n",
    "        self.category = category\n",
    "        self.completed = completed\n",
    "\n",
    "    def mark_completed(self):\n",
    "        self.completed = True\n",
    "\n",
    "    def to_dict(self):\n",
    "        return {\n",
    "            'title': self.title,\n",
    "            'description': self.description,\n",
    "            'category': self.category,\n",
    "            'completed': self.completed\n",
    "        }\n",
    "\n",
    "def save_tasks(tasks):\n",
    "    \"\"\"Save tasks to a JSON file.\"\"\"\n",
    "    with open('tasks.json', 'w') as f:\n",
    "        json.dump([task.to_dict() for task in tasks], f, indent=4)\n",
    "\n",
    "def load_tasks():\n",
    "    \"\"\"Load tasks from a JSON file.\"\"\"\n",
    "    try:\n",
    "        with open('tasks.json', 'r') as f:\n",
    "            return [Task(**data) for data in json.load(f)]\n",
    "    except FileNotFoundError:\n",
    "        return []\n",
    "\n",
    "class ToDoApp:\n",
    "    def __init__(self, root):\n",
    "        self.root = root\n",
    "        self.root.title(\"To-Do List Application\")\n",
    "\n",
    "        self.tasks = load_tasks()\n",
    "\n",
    "        self.listbox = Listbox(root, width=50, height=15)\n",
    "        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)\n",
    "        self.scrollbar = Scrollbar(root)\n",
    "        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)\n",
    "        self.listbox.config(yscrollcommand=self.scrollbar.set)\n",
    "        self.scrollbar.config(command=self.listbox.yview)\n",
    "\n",
    "        self.add_task_button = tk.Button(root, text=\"Add Task\", command=self.add_task)\n",
    "        self.add_task_button.pack(fill=tk.X)\n",
    "\n",
    "        self.mark_completed_button = tk.Button(root, text=\"Mark Completed\", command=self.mark_completed)\n",
    "        self.mark_completed_button.pack(fill=tk.X)\n",
    "\n",
    "        self.delete_task_button = tk.Button(root, text=\"Delete Task\", command=self.delete_task)\n",
    "        self.delete_task_button.pack(fill=tk.X)\n",
    "\n",
    "        self.load_tasks_to_listbox()\n",
    "\n",
    "    def load_tasks_to_listbox(self):\n",
    "        \"\"\"Load tasks into the Listbox.\"\"\"\n",
    "        self.listbox.delete(0, tk.END)  # Clear the Listbox\n",
    "        for task in self.tasks:\n",
    "            status = \"✔️\" if task.completed else \"❌\"\n",
    "            self.listbox.insert(tk.END, f\"[{status}] {task.title} - {task.description} (Category: {task.category})\")\n",
    "\n",
    "    def add_task(self):\n",
    "        \"\"\"Add a new task.\"\"\"\n",
    "        title = simpledialog.askstring(\"Task Title\", \"Enter task title:\")\n",
    "        if not title:\n",
    "            return\n",
    "        description = simpledialog.askstring(\"Task Description\", \"Enter task description:\")\n",
    "        category = simpledialog.askstring(\"Task Category\", \"Enter task category:\")\n",
    "        \n",
    "        task = Task(title, description, category)\n",
    "        self.tasks.append(task)\n",
    "        save_tasks(self.tasks)\n",
    "        self.load_tasks_to_listbox()\n",
    "        messagebox.showinfo(\"Success\", \"Task added successfully.\")\n",
    "\n",
    "    def mark_completed(self):\n",
    "        \"\"\"Mark selected task as completed.\"\"\"\n",
    "        selected_index = self.listbox.curselection()\n",
    "        if selected_index:\n",
    "            task = self.tasks[selected_index[0]]\n",
    "            task.mark_completed()\n",
    "            save_tasks(self.tasks)\n",
    "            self.load_tasks_to_listbox()\n",
    "            messagebox.showinfo(\"Success\", \"Task marked as completed.\")\n",
    "        else:\n",
    "            messagebox.showwarning(\"Select Task\", \"Please select a task to mark as completed.\")\n",
    "\n",
    "    def delete_task(self):\n",
    "        \"\"\"Delete selected task.\"\"\"\n",
    "        selected_index = self.listbox.curselection()\n",
    "        if selected_index:\n",
    "            del self.tasks[selected_index[0]]\n",
    "            save_tasks(self.tasks)\n",
    "            self.load_tasks_to_listbox()\n",
    "            messagebox.showinfo(\"Success\", \"Task deleted successfully.\")\n",
    "        else:\n",
    "            messagebox.showwarning(\"Select Task\", \"Please select a task to delete.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    root = tk.Tk()\n",
    "    app = ToDoApp(root)\n",
    "    root.mainloop()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a712f86f-ec9d-4cf7-8b35-7e9fdeb49438",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ae40fe6-2f36-4ef4-aed0-ea4550bea7d3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ac4f7d72-170c-4a11-8890-4e48c761ade4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
