
class Encryption:
    def __init__(self,text,key):
        self.text = text
        self.key = key

    def encryption(self,text, key):
        txt = ''
        for char in self.text:
            txt += chr(ord(char) ^ ord(key))
        return txt

