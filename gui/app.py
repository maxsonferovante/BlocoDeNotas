import Tkinter as tk  # python3
import tkMessageBox
import ttk as ttk

from notes import notepad, note

TITLE_FONT = ("Helvetica", 18, "bold")


class NotePadApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        self.wm_title("FAKE NOTE TAUROS")
        self.geometry("750x400+320+100")

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, NewNote, FindNote):
            page_name = F.__name__
            frame = F(parent=self.container, controller=self)
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

        label = ttk.Label(self, text="This is the note taurus", font=TITLE_FONT)

        button1 = ttk.Button(self, text="Go to New Note",
                            command=lambda: controller.show_frame("NewNote"))
        button2 = ttk.Button(self, text="Go to Find Note",
                             command=lambda: controller.show_frame("FindNote"))

        label.pack(side="top", padx=10, pady=10)
        button1.pack(side="top", padx=10, pady=10)
        button2.pack(side="top", padx=10, pady=10)

class NewNote(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self)
        self.text.focus_force()
        self.text.pack(expand=tk.YES, fill="x", pady=1)

        button_reset = ttk.Button(self, text="Reset note",
                                  command=self.reset_note)

        button_save = ttk.Button(self, text="Save note",
                                 command=self.save_note)

        button_back = ttk.Button(self, text="Go to the start page",
                                 command=self.back_startPage)

        label_name = ttk.Label(self, text="Enter the name of the note: ")

        self.var = tk.StringVar()
        self.var.set("")
        self.name = tk.Entry(self, textvariable=self.var)

        button_reset.pack(side=tk.LEFT, padx=10, pady=5)
        button_save.pack(side=tk.LEFT, padx=10, pady=5)
        button_back.pack(side=tk.LEFT, padx=10, pady=10)
        label_name.pack(side=tk.LEFT)
        self.name.pack(side=tk.LEFT)

    def save_note(self):
        result = tkMessageBox.askquestion("Save", "Are You Sure?", icon='question')
        if result == "yes":
            nt = note.Note(self.name.get(), self.text.get(1.0, tk.END))

            if not (notepad.Notepad()).save_note(nt):
                tkMessageBox.askretrycancel("Alert", "There is already the name. Try other", icon='error')
                self.name.focus_force()
            else:
                tkMessageBox.showinfo("Sucess", "New notes saved", )

    def reset_note(self):
        result = tkMessageBox.askquestion("Erase", "Are You Sure?", icon='question')
        if result == "yes":
            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)
            self.text.focus_force()

    def back_startPage(self):
        result = tkMessageBox.askquestion("Not be saved", "Are You Sure?", icon='question')
        if result == "yes":
            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)
            self.controller.show_frame("StartPage")

class FindNote(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        label_find = ttk.Label(self, text="Texto para Pesquisa: ")

        self.var = tk.StringVar()
        self.var.set("")
        self.name = tk.Entry(self, textvariable=self.var)

        button_find = ttk.Button(self, text="Find Note",
                                 command=self.find_note)
        button = ttk.Button(self, text="Go to the start page",
                            command=self.back_startPage)

        label_find.pack(pady=5)
        self.name.pack(pady=5)
        button_find.pack(pady=10)
        button.pack(pady=10)

    ##        self.box_value = tk.StringVar()
    ##        self.combobox = ttk.Combobox(self,
    ##                                    textvariable=self.box_value,
    ##                                    values = ('X', 'Y', 'Z'))
    ##        self.combobox.current(0)
    ##        self.combobox.bind("<<ComboboxSelected>>",self.combobox_selection)
    ##        self.combobox.pack(side="top",padx = 10, pady=10)

    ##    def combobox_selection(self,event):
    ##       print (self.box_value.get())
    ##        np = notepad.Notepad()

    def find_note(self):
        note_returned = (notepad.Notepad()).db.get_note(self.name.get())
        print (note_returned)
        self.controller.show_frame("NewNote")

    def back_startPage(self):
        result = tkMessageBox.askquestion("Not be saved", "Are You Sure?", icon='question')
        if result == "yes":
            self.name.delete(0, tk.END)
            self.controller.show_frame("StartPage")


if __name__ == "__main__":
    app = NotePadApp()
    app.mainloop()
