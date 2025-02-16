
class Encryption:
    def __init__(self,text,key):
        self.text = text
        self.key = key

    def encryption(self):
        txt = ''
        for char in self.text:
            txt += chr(ord(char) ^ ord(self.key))
        return txt