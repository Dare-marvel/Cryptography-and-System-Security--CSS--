def generate_key(plaintext, key):
    """Generates a repeated key to match the length of the plaintext."""
    key = key.upper()
    return (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

def vigenere_decrypt(ciphertext, key):
    """Decrypts ciphertext using the Vigenère (Polyalphabetic) cipher."""
    ciphertext = ciphertext.upper().replace(" ", "")
    key = generate_key(ciphertext, key)
    plaintext = ""
    for i in range(len(ciphertext)):
        cipher_char = ord(ciphertext[i]) - ord('A')
        key_char = ord(key[i]) - ord('A')
        plain_char = (cipher_char - key_char) % 26
        plaintext += chr(plain_char + ord('A'))
    return plaintext

def main():
    key = input("Enter the keyword: ")
    ciphertext = input("Enter the encrypted text: ")

    plaintext = vigenere_decrypt(ciphertext, key)
    print("Decrypted text:", plaintext)

if __name__ == "__main__":
    main()