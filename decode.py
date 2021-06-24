#Converts all binary list into ASCII numbers
def binary_to_ASSCI(binary):
    ASSCI = []

    i = 0

    while i < len(binary):
        string = ""

        for j in range(8):
            string += binary[j + i]
        
        ASSCI.append(int(string, 2))

        # adds 8 bits
        i += 8

    return ASSCI


# Converts the ASCII list into corsponding character
def ASSCI_to_letter(ASCCI_list):
    return [chr(letter) for letter in ASCCI_list]