# coding=utf-8
import sqlite3

from access.access import Private

Private("conn", "cursor", "commint_db")


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
        self.cursor.execute(sql, notes)

        self.commint_db()

    def update_note(self, note):

        ##cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))

        self.cursor.execute("UPDATE notes SET name =?,text =? WHERE id =?", (note.name, note.text, str(note.id)))
        self.commint_db()

    def delete_note(self, id):
        sql = "DELETE FROM notes WHERE id =? "
        self.cursor.execute(sql, (id,))

    def get_name_notes_salve(self):
        sql = "SELECT name FROM notes ORDER BY date"
        self.cursor.execute(sql)
        return [note[0] for note in self.cursor.fetchall()]

    def get_notes(self):
        sql = "SELECT * FROM notes ORDER BY date"
        self.cursor.execute(sql)
        return [note for note in self.cursor.fetchall()]

    def get_note(self, name):
        sql = "SELECT * FROM notes WHERE name == '" + name + "' ORDER BY date"
        self.cursor.execute(sql)

        recset = self.cursor.fetchall()
        '''o metodo fetchall retorna uma lista de tuplas formadas pelas columas.
            Por preferência mando apenas a tupla de retorno
        '''
        print recset
        return recset

    def close_db(self):
        if self.conn:
            self.conn.close()
