import sqlite3

from access.access import Private

Private("conn", "cursor", "create_table", "commint_db")


class DateBase(object):
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):
        if self.conn:
            sql = 'CREATE TABLE IF NOT EXISTS notes' \
                  '(id INTEGER PRIMARY KEY ,' \
                  'name VARCHAR (100),' \
                  'date VARCHAR (200),' \
                  'text VARCHAR (5000))'

            self.cursor.execute(sql)

    def commint_db(self):
        if self.conn:
            self.conn.commit()

    def insert_notes(self, notes):
        sql = "INSERT INTO notes VALUES (null,?,?,?)"

        if type(notes[0]) == tuple:
            self.cursor.execute(sql, notes)
            self.commint_db()
        else:
            self.cursor.execute(sql, notes)
            self.commint_db()

    def update_note(self, note):
        sql = "UPDATE notes SET name =" + note.name \
              + ", date = " + note.creation_date \
              + ", text = " + note.text \
              + "WHERE id = " + note.id

        self.cursor.execute(sql)
        self.commint_db()

    def delete_note(self, note):
        sql = "DELETE FROM notes WHERE name =? "
        self.cursor.execute(sql, (note.name,))

    def get_name_notes_salve(self):
        sql = "SELECT name FROM notes ORDER BY date"
        self.cursor.execute(sql)
        return [note[0] for note in self.cursor.fetchall()]

    def get_notes(self):
        sql = "SELECT * FROM notes ORDER BY date"
        self.cursor.execute(sql)
        return [note for note in self.cursor.fetchall()]

    def get_note(self, name):
        sql = "SELECT * FROM note WHERE name = " + name + " ORDER BY date"
        self.cursor.execute(sql)

        recset = self.cursor.fetchall()

        if len(recset) == 1:
            return recset
        return [note for note in recset]

    def close_db(self):
        if self.conn:
            self.conn.close()
