import sys
sys.path.append('../utilities/encryptionDecryption')
sys.path.append('../server/utilities')
from encryption import Encryption
from decryption import Decryption


from config import KEY

def encrypt_data(names_of_owners):
    encrypt = Encryption(KEY)
    return [encrypt.encryption(name) for name in names_of_owners]

def decrypt_data(data):
    return Decryption(KEY).decrypt(data)
