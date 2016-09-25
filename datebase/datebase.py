# coding=utf-8
import sqlite3

from access.access import Private

Private("conn", "cursor", "commint_db")


class DateBase(object):
    def __init__(self):
        self.conn = sqlite3.connect("/home/mferovante/Documents/NoteApp/note.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        if self.conn:
            self.cursor.execute("CREATE  TABLE  IF NOT EXISTS 'main'.'note' " +
                                "('id' INTEGER PRIMARY KEY  NOT NULL ," +
                                "'name' TEXT, 'date' TEXT, 'text' TEXT)")

    def commint_db(self):
        if self.conn:
            self.conn.commit()

    def insert_notes(self, note):
        self.cursor.execute('''INSERT INTO note(name,date,text) VALUES(?,?,?)''', note)

        self.commint_db()
        self.close_db()

    def update_note(self, note):

        ##cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId))

        self.cursor.execute("UPDATE note SET name =?,text =? WHERE id =?", (note.name, note.text, str(note.id)))
        self.commint_db()

    def delete_note(self, id):
        sql = "DELETE FROM note WHERE id =? "
        self.cursor.execute(sql, (id,))

    def get_name_notes_salve(self):
        sql = "SELECT name FROM note ORDER BY date"
        self.cursor.execute(sql)
        return [note for note in self.cursor.fetchall()]

    def get_notes(self):
        sql = "SELECT * FROM note ORDER BY date"
        self.cursor.execute(sql)
        return [note for note in self.cursor.fetchall()]

    def get_note(self, name):
        sql = "SELECT * FROM note WHERE name = '" + name + "'"
        self.cursor.execute(sql)
        recset = self.cursor.fetchall()
        '''o metodo fetchall retorna uma lista de tuplas formadas pelas columas.
            Por preferência mando apenas a tupla de retorno
        '''
        return recset

    def close_db(self):
        if self.conn:
            self.conn.close()
