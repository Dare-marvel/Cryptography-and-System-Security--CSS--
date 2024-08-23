class CaesarCipherCracker:
    def perform_attack(self, encrypted_message):
        for shift in range(1, 27):
            decrypted_message = []
            for segment in encrypted_message.split(" "):
                for char in segment:
                    decrypted_char = ord(char) - shift
                    if 65 <= ord(char) <= 90:  # Uppercase letters
                        if decrypted_char < 65:
                            decrypted_char = 90 - (65 - decrypted_char - 1)
                        decrypted_message.append(chr(decrypted_char))
                    elif 97 <= ord(char) <= 122:  # Lowercase letters
                        if decrypted_char < 97:
                            decrypted_char = 122 - (97 - decrypted_char - 1)
                        decrypted_message.append(chr(decrypted_char))
                    else:  # Non-alphabetic characters
                        decrypted_message.append(char)
                decrypted_message.append(" ")
            print("".join(decrypted_message))

if __name__ == "__main__":
    cracker = CaesarCipherCracker()
    cracker.perform_attack("lxdpq jwm lxum")
