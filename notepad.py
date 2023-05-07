import tkinter as tk
from tkinter import filedialog

class Notepad:
    def __init__(self, master):
        self.master = master
        master.title("Notepad")

        self.text = tk.Text(master, wrap="word")
        self.text.pack(expand=True, fill="both")

        self.toolbar = tk.Frame(master)
        self.toolbar.pack(side="top", fill="x")

        self.save_button = tk.Button(self.toolbar, text="Save", command=self.save_file)
        self.save_button.pack(side="left")

        self.load_button = tk.Button(self.toolbar, text="Load", command=self.load_file)
        self.load_button.pack(side="left")

    def save_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.text.get("1.0", "end"))

    def load_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as f:
                self.text.delete("1.0", "end")
                self.text.insert("1.0", f.read())
