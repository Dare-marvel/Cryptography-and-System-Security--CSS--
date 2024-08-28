def encrypt_text(plaintext, shift):
    """Encrypts plaintext using Caesar Cipher algorithm."""
    ciphertext = ""
    for char in plaintext:
        if char.isupper():
            ciphertext += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            ciphertext += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            ciphertext += char
    return ciphertext

def main():
    message = input("Enter message: ")
    shift_key = int(input("Enter shift key: "))
    print("Original Message:", message)
    print("Shift Key:", shift_key)
    encrypted = encrypt_text(message, shift_key)
    print("Encrypted Message:", encrypted)

if __name__ == "__main__":
    main()