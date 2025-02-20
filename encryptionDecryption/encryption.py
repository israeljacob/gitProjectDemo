
class Encryption:
    def __init__(self,key):
        self.key = key

    def encryption(self, text):
        txt = ''
        for char in text:
            try:
                txt += chr(ord(char) ^ ord(self.key))
            except TypeError:
                raise TypeError('The character must be with length 1.')
        return txt