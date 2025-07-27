
LIST_DICT_MAP = {
        "1": ['1'],
        "0": ['0'],
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }

def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    current = [0] * len(phoneNumber)
    index = 0
    final_lst = []
    pickDigitHelper(index, current, final_lst, phoneNumber)
    return final_lst

def pickDigitHelper(index, current, final_lst, phoneNumber):
    if index == len(phoneNumber):
        current_data = "".join(current)
        final_lst.append(current_data)
    else:
        digit = phoneNumber[index]
        letters = LIST_DICT_MAP[digit]

        for letter in letters:
            current[index] = letter
            pickDigitHelper(index + 1, current, final_lst, phoneNumber)


if __name__ == '__main__':
    ph_number = "1905"
    print(phoneNumberMnemonics(ph_number))