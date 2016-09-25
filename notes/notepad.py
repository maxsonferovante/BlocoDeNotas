from datebase.datebase import DateBase
from notes.note import Note

class Notepad:
    def __init__(self):
        self.db = DateBase("/home/mferovante/PycharmProjects/BlocoDeNotas/datebase/notes.db")

    def save_note(self, note):
        self.note = note

        print self.note.id, self.note.name

        for i in self.db.get_name_notes_salve():
            if i == self.note.name:
                return False

        self.db.insert_notes((self.note.name,
                                  self.note.creation_date,
                                  self.note.text))
        self.db.close_db()
        return True

    def find_note(self, name):
        note = None
        aux = self.db.get_note(name)
        if aux:
            note = Note(aux[0], aux[1], aux[2], aux[3])
            self.db.close_db()
            return note
        else:
            self.db.close_db()
            return note


    def update_note(self, note):
        self.db.update_note(note)
        self.db.close_db()

    def erase(self, note):
        self.db.delete_note(note.id)
        self.db.close_db()
