
class Encryption:
    def __init__(self):
        self.key = open("key.txt","r").read()

    def encryption(self, text):
        txt = ''
        for char in text:
            txt += chr(ord(char) ^ ord(self.key))
        return txt
