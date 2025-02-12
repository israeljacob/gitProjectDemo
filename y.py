def encription(str):
    return chr(ord(str) ^ ord("1"))

def write(char):
    char = char
    file = open("data","a")
    file.write(chr(ord(char) ^ ord("1")))


write("d")
write("6")


