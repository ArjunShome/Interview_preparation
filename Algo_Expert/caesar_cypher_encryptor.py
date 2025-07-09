
def caesarCipherEncryptor(string, key):
    # Write your code here.
    final_string = ""
    key = key % 26
    for char in string:
        if ord(char) + key > ord("z"):
            char = chr(ord('a') - 1 + (ord(char) + key) % ord('z'))
            final_string += char
        else:
            final_string += chr(ord(char) + key)
    return final_string

if __name__ =='__main__':
    string = "xyz"
    key = 2
    print(caesarCipherEncryptor(string, key))