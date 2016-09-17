from datebase.datebase import DateBase


class Notepad:
    def __init__(self):
        self.db = DateBase("notes.db")

    def save_note(self, note):
        self.note = note
        if note.name in self.db.get_name_notes_salve():
            return False
        else:
            self.db.insert_notes((self.note.name,
                                  self.note.creation_date,
                                  self.note.text))
            return True
