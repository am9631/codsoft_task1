import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

def refresh_list():
    listbox.delete(0, tk.END)
    for t in tasks:
        mark = "✅ " if t["done"] else "❌  "
        listbox.insert(tk.END, mark + t["text"])


def add_task():
    text = simpledialog.askstring("Add Task", "Task:")
    if text:
        tasks.append({"text": text, "done": False})
        refresh_list()


def delete_task():
    sel = listbox.curselection()
    if not sel:
        return
    tasks.pop(sel[0])
    refresh_list()


def toggle_task():
    sel = listbox.curselection()
    if not sel:
        return
    t = tasks[sel[0]]
    t["done"] = not t["done"]
    refresh_list()


def edit_task():
    sel = listbox.curselection()
    if not sel:
        return
    t = tasks[sel[0]]
    new_text = simpledialog.askstring("Edit Task", "New text:", initialvalue=t["text"])
    if new_text:
        t["text"] = new_text
        refresh_list()

root = tk.Tk()
root.title("Simple To-Do App")
root.geometry("350x350")

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

btn_add = tk.Button(btn_frame, text="Add", width=9, command=add_task)
btn_add.grid(row=0, column=0, padx=5)

btn_edit = tk.Button(btn_frame, text="Edit", width=9, command=edit_task)
btn_edit.grid(row=0, column=1, padx=5)

btn_del = tk.Button(btn_frame, text="Delete", width=9, command=delete_task)
btn_del.grid(row=0, column=2, padx=5)

btn_toggle = tk.Button(root, text="Update", width=10, command=toggle_task)
btn_toggle.pack(pady=5)

refresh_list()

root.mainloop()
