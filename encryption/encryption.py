
class Encryption:
    def __init__(self,text,key):
        self.text = text
        self.key = key

    def encryption(self):
        txt = ''
        for char in self.text:
            try:
                txt += chr(ord(char) ^ ord(self.key))
            except TypeError:
                raise TypeError('The character must be with length 1.')
        return txt