import decode
import encode

def encode_phase():
    word_to_encode = str(input("Please enter a sentence to encode "))

    ASCII = encode.word_to_ASCII(word_to_encode)
    binary_converted = encode.ASCII_to_bin(ASCII)
    
    print(f"The encoded message is: {''.join(binary_converted)}")


def decode_phase():
    binary_message = input(str("Enter the binary decode: "))

    if " " in binary_message:
        binary_message = "".join(binary_message.split(" "))

    ASSCI_message = decode.binary_to_ASSCI(binary_message)
    decoded = decode.ASSCI_to_letter(ASSCI_message)

    print(f"The decoded message is: {''.join(decoded)}")


def main():
    options = str(input("Would you like to encode or decode?"))

    if options.lower() == "encode":
        encode_phase()
    elif options.lower() == "decode":
        decode_phase()
    else:
        print("Please specify if you want to encode or decode the message")
        
if __name__ == "__main__":
    main()