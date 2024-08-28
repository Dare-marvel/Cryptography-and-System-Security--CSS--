def decode_caesar(cipher_text, shift_amount):
    """Decodes Caesar cipher with given shift."""
    plain_text = ""
    for char in cipher_text:
        if char.isupper():
            plain_text += chr((ord(char) - shift_amount - 65) % 26 + 65)
        elif char.islower():
            plain_text += chr((ord(char) - shift_amount - 97) % 26 + 97)
        else:
            plain_text += char
    return plain_text

def main():
    encrypted_text = input("Enter encrypted text: ")
    for shift in range(1, 26):
        print(f"Shift {shift}: {decode_caesar(encrypted_text, shift)}")

if __name__ == "__main__":
    main()