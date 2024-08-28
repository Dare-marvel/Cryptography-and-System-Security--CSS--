class VigenereCipherCracker:
    """Cracks Vigenere ciphers by exhaustive key search."""

    def __init__(self, ciphertext):
        self.ciphertext = ciphertext

    def decrypt(self, key):
        """Decrypts the ciphertext using the Vigenere cipher."""
        decrypted_text = []
        key = key.upper()
        key_length = len(key)

        for index, char in enumerate(self.ciphertext):
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                shift = ord(key[index % key_length]) - ord('A')
                decrypted_char = chr((ord(char) - base - shift + 26) % 26 + base)
                decrypted_text.append(decrypted_char)
            else:
                decrypted_text.append(char)

        return ''.join(decrypted_text)

    def generate_keys(self, alphabet, length):
        """Generates all possible keys of a given length."""
        if length == 0:
            return ['']
        keys = []
        for letter in alphabet:
            for key in self.generate_keys(alphabet, length - 1):
                keys.append(letter + key)
        return keys

    def exhaustive_key_search(self, max_key_length):
        """Performs an exhaustive key search."""
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for length in range(1, max_key_length + 1):
            for key in self.generate_keys(alphabet, length):
                decrypted_message = self.decrypt(key)
                print(f'Testing key "{key}": {decrypted_message}')

def main():
    ciphertext = input("Enter the ciphertext: ")
    max_key_length = int(input("Enter the maximum key length: "))

    cracker = VigenereCipherCracker(ciphertext)
    cracker.exhaustive_key_search(max_key_length)

if __name__ == "__main__":
    main()