import sys
sys.path.append('../utilities/encryptionDecryption')
from Iencryptor import IEncryptor

class XorEncryptor(IEncryptor):
    """
    Encrypts text using XOR with a single-character key.
    """

    def __init__(self,key):
        self.key = key

    def encrypt(self, text):
        txt = ''
        try:
            if type(text) == str:
                for i, char in  enumerate(text):
                    txt += chr(ord(char) ^ ord(self.key[i % len(self.key)]))
            else:
                for i, char in  enumerate(text):
                    txt += chr(char ^ ord(self.key[i % len(self.key)]))
        except TypeError:
            raise TypeError('The character must be with length 1.')
        return txt