import string

def create_cipher_alphabet(key):
    key = key.upper()
    key = ''.join(sorted(set(key), key=key.index)) 
    key = key + ''.join(sorted(set(string.ascii_uppercase) - set(key)))
    return key

def decrypt(ciphertext, key):
    """Decrypt the ciphertext using the provided key."""
    key = key.upper()
    cipher_alphabet = create_cipher_alphabet(key)
    alphabet = string.ascii_uppercase
    table = str.maketrans(cipher_alphabet, alphabet)
    return ciphertext.upper().translate(table)

if __name__ == "__main__":
    key = input("Enter the key: ")
    ciphertext = input("Enter the ciphertext: ")

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
