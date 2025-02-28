import sys
sys.path.append('../utilities/encryptionDecryption')
from xorEncryptor import XorEncryptor


from config import KEY

def encrypt_data(data):
    return XorEncryptor(KEY).encrypt(data)
