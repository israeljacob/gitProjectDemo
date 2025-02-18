class Decryption:
    def __init__(self, key):
        self.key = key
    def decrypt(self, text):
        txt = ''
        try:
            for char in text:
                txt += chr(char ^ ord(self.key))
        except:
            raise TypeError('The character must be a binary character with length 1.')
        return txt

