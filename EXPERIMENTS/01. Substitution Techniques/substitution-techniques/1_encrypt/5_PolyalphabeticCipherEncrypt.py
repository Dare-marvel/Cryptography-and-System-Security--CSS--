def generate_key(plaintext, key):
    """Generates a repeated key to match the length of the plaintext."""
    key = key.upper()
    return (key * (len(plaintext) // len(key) + 1))[:len(plaintext)]

def vignere_cipher(plaintext, key):
    """Encrypts plaintext using the Vigenère (Polyalphabetic) cipher."""
    plaintext = plaintext.upper().replace(" ", "")
    key = generate_key(plaintext, key)
    ciphertext = ""
    for i in range(len(plaintext)):
        text_char = ord(plaintext[i]) - ord('A')
        key_char = ord(key[i]) - ord('A')
        ciphertext += chr((text_char + key_char) % 26 + ord('A'))
    return ciphertext

if __name__ == "__main__":
    key = input("Enter the keyword: ")
    plaintext = input("Enter the text: ")

    ciphertext = vignere_cipher(plaintext, key)
    print("Encrypted text:", ciphertext)