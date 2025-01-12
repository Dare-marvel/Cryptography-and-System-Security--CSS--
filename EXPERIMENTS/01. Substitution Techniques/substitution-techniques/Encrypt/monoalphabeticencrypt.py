import string

def create_cipher_alphabet(key):
    key = key.upper()
    key = ''.join(sorted(set(key), key=key.index)) 
    key = key + ''.join(sorted(set(string.ascii_uppercase) - set(key)))
    return key

def encrypt(plaintext, key):
    """Encrypt the plaintext using the provided key."""
    key = key.upper()
    cipher_alphabet = create_cipher_alphabet(key)
    alphabet = string.ascii_uppercase
    table = str.maketrans(alphabet, cipher_alphabet)
    return plaintext.upper().translate(table)

if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext)
