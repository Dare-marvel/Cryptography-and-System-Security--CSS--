def caesar_encrypt(message, shift):
    encrypted_message = ""

    # Traverse through each character in the message
    for i in range(len(message)):
        char = message[i]

        # Encrypt uppercase characters
        if char.isupper():
            encrypted_message += chr((ord(char) + shift - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            encrypted_message += chr((ord(char) + shift - 97) % 26 + 97)

    return encrypted_message

message = input("Enter the message: ")
shift_amount = int(input("Enter the shift amount: "))
print("Message  : " + message)
print("Shift    : " + str(shift_amount))
print("Encrypted: " + caesar_encrypt(message, shift_amount))
