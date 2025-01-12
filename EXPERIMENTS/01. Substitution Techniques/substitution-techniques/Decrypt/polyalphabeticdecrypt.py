def create_extended_key(ciphertext, key):
    key = key.upper()
    extended_key = key
    while len(extended_key) < len(ciphertext):
        extended_key += key
    return extended_key[:len(ciphertext)]

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper().replace(" ", "")
    key = create_extended_key(ciphertext, key)
    
    plaintext = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        p = (c - k) % 26
        plaintext += chr(p + ord('A'))

    return plaintext

if __name__ == "__main__":
    key = input("Enter the key: ")
    ciphertext = input("Enter the ciphertext: ")

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
