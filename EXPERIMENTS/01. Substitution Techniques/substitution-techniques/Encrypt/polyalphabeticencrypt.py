def create_extended_key(plaintext, key):
    key = key.upper()
    extended_key = key
    while len(extended_key) < len(plaintext):
        extended_key += key
    return extended_key[:len(plaintext)]

def encrypt(plaintext, key):
    plaintext = plaintext.upper().replace(" ", "")
    key = create_extended_key(plaintext, key)
    
    ciphertext = ""
    for i in range(len(plaintext)):
        p = ord(plaintext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        c = (p + k) % 26
        ciphertext += chr(c + ord('A'))

    return ciphertext

if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    ciphertext = encrypt(plaintext, key)
    print("Encrypted text:", ciphertext)
