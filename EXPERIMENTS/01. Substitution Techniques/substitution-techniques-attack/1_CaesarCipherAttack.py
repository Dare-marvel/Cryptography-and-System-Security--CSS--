class CaesarCipherCracker:
    def crack(self, ciphertext):
        """Cracks the Caesar cipher by trying all possible shifts."""
        for shift in range(1, 26): # shift 0 => original message itself (so shift ranges from 1 to 25 only)
            plaintext = self.decrypt(ciphertext, shift)
            print(f"Shift {shift}: {plaintext}")

    def decrypt(self, ciphertext, shift):
        """Decrypts the ciphertext using the Caesar cipher."""
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('a') if char.islower() else ord('A')
                plaintext += chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                plaintext += char
        return plaintext

def main():
    cracker = CaesarCipherCracker()
    ciphertext = input("Enter the encrypted text: ")
    cracker.crack(ciphertext)

if __name__ == "__main__":
    main()