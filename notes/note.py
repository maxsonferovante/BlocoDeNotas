import datetime


class Note(object):
    def __init__(self, name="", text=""):
        self.id = int()
        self.creation_date = str(datetime.datetime.now())[:19]
        self.name = name or ("Documento-sem-Nome-" + self.creation_date)
        self.text = text


    def find_word(self, word):
        if word in self.text:
            return True
        else:
            return False

    def update_date(self):
        self.creation_date = ("Documento-sem-Nome-" + datetime.datetime.now()[:19])
