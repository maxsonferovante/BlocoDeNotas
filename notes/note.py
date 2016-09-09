import datetime


class Note(object):
    def __init__(self, name="", text=""):
        self.id;
        self.creation_date = str(datetime.datetime.now())[:19]
        self.name = name or ("Documento-sem-Nome-" + self.creation_date)
        self.text = text

    def find(self, word):
        if word in self.text:
            print ("A palavra foi encontrada.")
        else:
            print ("A palavra nao foi encontrada.")
