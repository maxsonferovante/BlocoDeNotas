import Tkinter as tk  # python3
import tkMessageBox
import ttk as ttk

from newnote import NewNote
from notes import notepad


class FindNote(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.parent = parent

        label_find = ttk.Label(self, text="Texto para Pesquisa: ")

        self.var = tk.StringVar()
        self.var.set("")
        self.name = tk.Entry(self, textvariable=self.var)

        button_find = ttk.Button(self, text="Find Note",
                                 command=self.btt_find_note)
        button = ttk.Button(self, text="Go to the start page",
                            command=self.btt_back_startPage)

        label_find.pack(pady=5)
        self.name.pack(pady=5)
        button_find.pack(pady=10)
        button.pack(pady=10)

    def btt_find_note(self):
        note_returned = (notepad.Notepad()).find_note(self.name.get())
        print (note_returned)

        if note_returned is not None:
            nn = NewNote(parent=self.parent, controller=self.controller, note=note_returned)
            nn.grid(row=0, column=0, sticky="nsew")
            self.name.delete(0, 'end')
            nn.tkraise()
        else:
            tkMessageBox.askretrycancel("Retry", "No note found", icon="error")
            self.name.delete(0, 'end')
            self.name.focus_force()

    def btt_back_startPage(self):
        self.controller.show_frame("StartPage")
