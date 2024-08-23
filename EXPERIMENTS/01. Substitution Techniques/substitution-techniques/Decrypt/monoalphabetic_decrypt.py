import string

def generate_cipher_alphabet(keyword):
    keyword = keyword.upper()
    keyword = ''.join(sorted(set(keyword), key=keyword.index))
    keyword = keyword + ''.join(sorted(set(string.ascii_uppercase) - set(keyword)))
    return keyword

def decipher(encrypted_message, keyword):
    """Decipher the encrypted message using the provided keyword."""
    keyword = keyword.upper()
    cipher_alphabet = generate_cipher_alphabet(keyword)
    standard_alphabet = string.ascii_uppercase
    translation_table = str.maketrans(cipher_alphabet, standard_alphabet)
    return encrypted_message.upper().translate(translation_table)

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    encrypted_message = input("Enter the encrypted message: ")

    decrypted_message = decipher(encrypted_message, keyword)
    print("Decrypted message:", decrypted_message)
