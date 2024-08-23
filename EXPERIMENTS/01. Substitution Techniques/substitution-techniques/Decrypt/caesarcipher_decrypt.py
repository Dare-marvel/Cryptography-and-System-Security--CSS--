def decode(cipher_text, shift_amount):
    decrypted_text = ""

    # Iterate through each character in the cipher_text
    for index in range(len(cipher_text)):
        current_char = cipher_text[index]

        # Decode uppercase characters
        if current_char.isupper():
            decrypted_text += chr((ord(current_char) - shift_amount - 65) % 26 + 65)

        # Decode lowercase characters
        else:
            decrypted_text += chr((ord(current_char) - shift_amount - 97) % 26 + 97)

    return decrypted_text

cipher_text = input("Enter the encrypted text: ")
for shift in range(1, 26):
    print(str(shift) + " " + decode(cipher_text, shift))
