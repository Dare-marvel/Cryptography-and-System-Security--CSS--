import string

def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    keyword = keyword + ''.join(sorted(set(string.ascii_uppercase) - set(keyword)))
    return keyword

def encode(message, keyword):
    """Encode the message using the provided keyword."""
    keyword = keyword.upper()
    cipher_alphabet = generate_cipher_alphabet(keyword)
    standard_alphabet = string.ascii_uppercase
    translation_table = str.maketrans(standard_alphabet, cipher_alphabet)
    return message.upper().translate(translation_table)

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    message = input("Enter the message: ")

    encrypted_message = encode(message, keyword)
    print("Encoded text:", encrypted_message)
