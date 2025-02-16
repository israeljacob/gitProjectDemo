def cipher_key():
    with open("/Users/admin/desktop/data") as f:
        file = f.read()
        for i in file:
            print(chr(ord(i) ^ ord("a")), end="")
        print("\ncipher:", file)


cipher_key()


