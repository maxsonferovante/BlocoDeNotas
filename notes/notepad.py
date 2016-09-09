from datebase.datebase import DateBase


class Notepad(DateBase):
    def __init__(self):
        DateBase.__init__(self, "notes.db")


n = Notepad()
