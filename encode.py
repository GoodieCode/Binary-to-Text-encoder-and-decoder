# Converts all the characters of word or sentence into ASCII numbers
def word_to_ASCII(word: str):
    return [ord(word[i]) for i in range(0, len(word))]


# Converts all the ASCII values into binary
def ASCII_to_bin(ASCII_list: list):
    return [bin(assci_value)[2:].zfill(8) for assci_value in ASCII_list]