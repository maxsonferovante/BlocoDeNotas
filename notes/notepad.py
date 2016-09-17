from datebase.datebase import DateBase


class Notepad:
    def __init__(self):
        self.db = DateBase("notes.db")

    def save_note(self, note):
        self.note = note

        self.db.insert_notes((self.note.name,
                              self.note.text,
                              self.note.creation_date))
