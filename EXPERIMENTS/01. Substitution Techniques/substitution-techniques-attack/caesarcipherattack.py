class CaesarAttack:
    def caesar_cipher_attack(self, message):
        for key in range(1, 27):
            plain_text = []
            for word in message.split(" "):
                for ch in word:
                    new_ch = ord(ch) - key
                    if 65 <= ord(ch) <= 90:  # Uppercase letters
                        if new_ch < 65:
                            new_ch = 90 - (65 - new_ch - 1)
                        plain_text.append(chr(new_ch))
                    elif 97 <= ord(ch) <= 122:  # Lowercase letters
                        if new_ch < 97:
                            new_ch = 122 - (97 - new_ch - 1)
                        plain_text.append(chr(new_ch))
                    else:  # Non-alphabetic characters
                        plain_text.append(ch)
                plain_text.append(" ")
            print("".join(plain_text))

if __name__ == "__main__":
    ob = CaesarAttack()
    ob.caesar_cipher_attack("lxdpq jwm lxum")
