
def runLengthEncoding(string):
    encoded_str = ""
    count = 1
    prev_char = string[0]
    for char_idx in range(1, len(string)):
        if string[char_idx] == prev_char:
            count += 1
        else:
            encoded_str += f"{count}{prev_char}"
            count = 1
            prev_char = string[char_idx]
        if count == 9:
            encoded_str += f"{count}{string[char_idx]}"
            count = 0 

    encoded_str += f"{count}{prev_char}"
    
    return encoded_str






if __name__ == '__main__':
    string = "AAAAAAAAAAAAABBCCCCDD"
    print(runLengthEncoding(string))
