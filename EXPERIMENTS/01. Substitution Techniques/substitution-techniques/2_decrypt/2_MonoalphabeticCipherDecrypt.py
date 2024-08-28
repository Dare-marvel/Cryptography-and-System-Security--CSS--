import string

def create_cipher(key):
    """Creates a cipher alphabet from the key."""
    key = key.upper()
    unique_chars = "".join(sorted(set(key), key=key.index))
    cipher = unique_chars + "".join(sorted(set(string.ascii_uppercase) - set(unique_chars)))
    return cipher

def decode(ciphertext, key):
    """Decodes ciphertext using the key."""
    cipher = create_cipher(key)
    alphabet = string.ascii_uppercase
    translation = str.maketrans(cipher, alphabet)
    return ciphertext.upper().translate(translation)

def main():
    keyword = input("Enter keyword: ").strip()
    message = input("Enter the encrypted message: ").strip()
    decoded = decode(message, keyword)
    print("Decrypted message:", decoded)

if __name__ == "__main__":
    main()
