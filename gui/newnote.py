import Tkinter as tk  # python3
import tkMessageBox
import ttk as ttk

from notes import notepad, note


class NewNote(tk.Frame):
    def __init__(self, parent, controller, note=None):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.note = note

        scrollbar = ttk.Scrollbar(self)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text = tk.Text(self)
        self.text.pack(expand=tk.YES, fill="x", pady=1)
        self.text.focus_force()

        self.button_delete = ttk.Button(self, text="Delete note",
                                        state=tk.DISABLED,
                                        command=self.btt_delete_note)

        self.btt_text = tk.StringVar()
        self.btt_text.set("Save note")

        self.button_save = ttk.Button(self, textvariable=self.btt_text,
                                      command=self.btt_save_note)

        self.button_back_find = ttk.Button(self, text="Go to try a new search",
                                           state=tk.DISABLED,
                                           command=self.btt_back_find)

        self.button_back = ttk.Button(self, text="Go to the start page",
                                      command=self.btt_back_startPage)

        self.label_name = ttk.Label(self, text="Enter the name of the note: ")

        self.var = tk.StringVar()
        self.name = tk.Entry(self, textvariable=self.var)

        self.button_delete.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_save.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_back_find.pack(side=tk.LEFT, padx=10, pady=5)
        self.button_back.pack(side=tk.LEFT, padx=10, pady=10)
        self.label_name.pack(side=tk.LEFT)
        self.name.pack(side=tk.LEFT)

        if self.note is not None:
            self.name.insert(tk.END, self.note.name)
            self.text.insert(tk.END, self.note.text)

            self.btt_text.set("Update note")

            self.button_back_find.config(state="normal")
            self.button_delete.config(state="normal")

    def btt_save_note(self):
        if self.note is None:
            result = tkMessageBox.askquestion("Save", "Are You Sure?", icon='question')
            if result == "yes":
                nt = note.Note(self.name.get(), self.text.get(1.0, tk.END))

                if not (notepad.Notepad()).save_note(nt):
                    tkMessageBox.askretrycancel("Alert", "There is already the name. Try other", icon='error')
                    self.name.focus_force()
                else:
                    tkMessageBox.showinfo("Sucess", "New notes saved", )
        else:
            result = tkMessageBox.askquestion("Update", "Are You Sure?", icon='question')
            if result == "yes":
                self.note.name = self.name.get()
                self.note.text = self.text.get("0.0", "end")

                (notepad.Notepad()).update_note(self.note)
                tkMessageBox.showinfo("Sucess", "New notes updated", )

    def btt_back_find(self):
        result = tkMessageBox.askquestion("Try a new find", "Are You Sure?", icon='question')
        if result == "yes":
            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)
            self.controller.show_frame("FindNote")

    def btt_delete_note(self):
        result = tkMessageBox.askquestion("Erase", "Are You Sure?", icon='question')
        if result == "yes":
            (notepad.Notepad()).erase(self.note)

            tkMessageBox.showinfo("Sucess", "Note deleted", )

            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)

            self.controller.show_frame("FindNote")

        else:
            self.text.focus_force()

    def btt_back_startPage(self):
        result = tkMessageBox.askquestion("Not be saved", "Are You Sure?", icon='question')
        if result == "yes":
            self.name.delete(0, tk.END)
            self.text.delete(1.0, tk.END)
            self.controller.show_frame("StartPage")
