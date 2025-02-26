import sys
from utilities.encryptionDecryption import Encryption

def main():
    data = sys.argv
    if len(data) > 2:
        with open(data[1]) as f:
            file = f.read()
            for chr in file:
                print(Encryption(data[2]).encryption(chr), end="")

if __name__ == "__main__":
    main()

