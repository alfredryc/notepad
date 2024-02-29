from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter import messagebox

class NotepadApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Notepad") 
        self.root.geometry("500x500")
        self.root.config(bg="#5d5c5a")
        self.document = None
        self.create_ui()

    def create_ui(self):
        # Square text
        self.editor = Text(self.root, undo="true")
        self.editor.pack(side=TOP, fill=BOTH, expand=1)
        # Navigation bar
        navigation_bar = Menu(self.root)
        self.root.config(menu=navigation_bar)

        # Navigation bar buttons
        # File
        file_menu = Menu(navigation_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_app)
        navigation_bar.add_cascade(label="File", menu=file_menu)
        # Edit
        edit_menu = Menu(navigation_bar, tearoff=0)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_command(label="Undo", command=self.undo_text)
        edit_menu.add_command(label="Redo", command=self.redo_text)
        navigation_bar.add_cascade(label="Edit", menu=edit_menu)
        # Help
        help_menu = Menu(navigation_bar, tearoff=0)
        help_menu.add_command(label="License", command=self.show_license)
        help_menu.add_command(label="About...", command=self.about)
        navigation_bar.add_cascade(label="Help", menu=help_menu)


    # File functions
    def new_file(self):
        self.editor.delete(1.0, END)

    def open_file(self):
        self.document = askopenfile(filetypes=[("Text files","*.txt"), ("All files","*.*")])
        if self.document is not None:
            content = self.document.read()
            self.editor.insert(1.0, content)
            self.document.close()

    def save_file(self):
        self.document = asksaveasfile(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if self.document is not None:
            content = self.editor.get(1.0, END)
            self.document.write(content)
            self.document.close()


    # Edit functions
    def copy_text(self):
        self.editor.clipboard_clear()
        self.editor.clipboard_append(self.editor.selection_get())

    def paste_text(self):
        self.editor.insert(INSERT, self.editor.clipboard_get())

    def cut_text(self):
        self.editor.clipboard_clear()
        self.editor.clipboard_append(self.editor.selection_get())
        self.editor.delete("sel.first", "sel.last")

    def undo_text(self):
        self.editor.edit_undo()

    def redo_text(self):
        self.editor.edit_redo()


    # Help functions
    def about(self):
        messagebox.showinfo("About...", "Created by Alfred")

    def show_license(self):
        messagebox.showwarning("License", "Open source :).")

    def exit_app(self):
        exit = messagebox.askokcancel("Exit", "Do you want to go out?")
        if exit:
            self.root.destroy()

def main():
    root = Tk()
    notepad_app = NotepadApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
