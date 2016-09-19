from datebase.datebase import DateBase
from notes.note import Note

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

    def find_note(self, name):
        note = None
        aux = self.db.get_note(name)
        if aux:
            note = Note(aux[0], aux[1], aux[2], aux[3])
            return note
        else:
            return note

    def update_note(self, note):
        print (note)
        self.db.update_note(note)
