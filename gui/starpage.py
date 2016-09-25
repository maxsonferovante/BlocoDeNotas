import Tkinter as tk  # python3
import ttk as ttk

TITLE_FONT = ("Helvetica", 18, "bold")


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
