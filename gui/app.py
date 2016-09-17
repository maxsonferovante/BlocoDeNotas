import Tkinter as tk  # python3
import tkMessageBox

from notes import notepad, note

TITLE_FONT = ("Helvetica", 18, "bold")


class NotePadApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NewNote, FindNote):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is the note taurus", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to New Note",
                            command=lambda: controller.show_frame("NewNote"))
        button2 = tk.Button(self, text="Go to Find Note",
                            command=lambda: controller.show_frame("FindNote"))
        button1.pack()
        button2.pack()


class NewNote(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        scrollbar = tk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self)
        self.text.focus_force()
        self.text.pack(expand=tk.YES, fill="x", pady=1)

        button_reset = tk.Button(self, text="Reset note",
                                 command=self.reset_note)

        button_save = tk.Button(self, text="Save note",
                                command=self.save_note)

        button_back = tk.Button(self, text="Go to the start page",
                                command=lambda: controller.show_frame("StartPage"))

        button_reset.pack(side="left", padx=10, pady=5)
        button_save.pack(side="left", padx=10, pady=5)
        button_back.pack(side="left", padx=10, pady=10)

        label_name = tk.Label(self, text="Enter the name of the note: ")
        label_name.pack(side=tk.LEFT)

        self.var = tk.StringVar()
        self.var.set("")
        self.name = tk.Entry(self, textvariable=self.var)
        self.name.pack(side=tk.LEFT)

    def save_note(self):
        result = tkMessageBox.askquestion("Save", "Are You Sure?", icon='question')
        if result:
            nt = note.Note(self.name.get(), self.text.get(1.0, tk.END))
            (notepad.Notepad()).save_note(nt)

    def reset_note(self):
        result = tkMessageBox.askquestion("Erase", "Are You Sure?", icon='question')
        if result:
            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)
            self.text.focus_force()


class FindNote(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label = tk.Label(self, text="This is page 2", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = NotePadApp()
    app.mainloop()
