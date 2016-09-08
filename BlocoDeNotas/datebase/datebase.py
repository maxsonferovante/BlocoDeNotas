import sqlite3

from access import Private

Private("conn", "cursor", "create_table", "commint_db")


class DateBase(object):
    def __init__(self, db_name):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()

            self.create_table()

        except sqlite3.Error:
            print "ERRO ao Abrir o banco..."
            return False

    def create_table(self):
        if self.conn:
            sql = 'CREATE TABLE IF NOT EXISTS notes' \
                  '(id INTEGER PRIMARY KEY ,' \
                  'name VARCHAR (100),' \
                  'date VARCHAR (200)' \
                  'text VARCHAR (5000))'

            self.cursor(sql)

    def commint_db(self):
        if self.conn:
            self.conn.commint()

    def insert_db(self, notes):
        sql = "INSERT INTO notes VALUES (null,?,?,?)"

        if notes == list():
            for note in notes:
                self.cursor.execute(sql, note)
                self.commint_db()
        else:
            self.cursor.execute(sql, notes)
            self.commint_db()

    def get_name_notes_salve(self):
        sql = "SELECT name FROM note ORDER BY date"
        self.cursor.execute(sql)
        return [note[0] for note in self.cursor.fetchall()]

    def get_notes(self):
        sql = "SELECT * FROM note ORDER BY date"
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
