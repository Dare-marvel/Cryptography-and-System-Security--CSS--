class PlayfairCipherCracker:
    """Playfair cipher cracker implementation."""

    def __init__(self, key_phrase):
        self.key_matrix = self.create_key_matrix(key_phrase.lower())

    def create_key_matrix(self, key_phrase):
        """Creates a 5x5 Playfair key matrix from the key phrase."""
        matrix = []
        used_chars = set()

        # Add characters from the key phrase
        for char in key_phrase:
            if char.isalpha() and char not in used_chars and char != 'j':
                used_chars.add(char)
                matrix.append(char)

        # Add remaining characters from the alphabet
        for code in range(ord('a'), ord('z') + 1):
            letter = chr(code)
            if letter not in used_chars and letter != 'j':
                used_chars.add(letter)
                matrix.append(letter)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def locate_char_position(self, matrix, char):
        """Finds the position of a character in the matrix."""
        for row_idx, row in enumerate(matrix):
            if char in row:
                return row_idx, row.index(char)
        return None

    def decrypt(self, cipher_text):
        """Decrypts the ciphertext using the Playfair cipher."""
        decrypted_text = []
        cipher_text = cipher_text.lower()

        # Ensure ciphertext length is even
        if len(cipher_text) % 2 != 0:
            cipher_text += 'x'  # Append a filler character if length is odd

        for idx in range(0, len(cipher_text), 2):
            char1 = cipher_text[idx]
            char2 = cipher_text[idx + 1]

            pos1 = self.locate_char_position(self.key_matrix, char1)
            pos2 = self.locate_char_position(self.key_matrix, char2)

            if pos1 is None or pos2 is None:
                decrypted_text.append(char1)
                decrypted_text.append(char2)
                continue

            if pos1[0] == pos2[0]:  # Same row
                decrypted_text.append(self.key_matrix[pos1[0]][(pos1[1] - 1) % 5])
                decrypted_text.append(self.key_matrix[pos2[0]][(pos2[1] - 1) % 5])
            elif pos1[1] == pos2[1]:  # Same column
                decrypted_text.append(self.key_matrix[(pos1[0] - 1) % 5][pos1[1]])
                decrypted_text.append(self.key_matrix[(pos2[0] - 1) % 5][pos2[1]])
            else:  # Rectangle swap
                decrypted_text.append(self.key_matrix[pos1[0]][pos2[1]])
                decrypted_text.append(self.key_matrix[pos2[0]][pos1[1]])

        return ''.join(decrypted_text).upper()  # Convert to uppercase for consistency

def main():
    cipher_text = input("Enter the ciphertext: ")
    possible_keys = ["secret", "playfair", "example", "keyword", "random", "monarch"]

    for key_phrase in possible_keys:
        cracker = PlayfairCipherCracker(key_phrase)
        decrypted_text = cracker.decrypt(cipher_text)
        print(f"Key: {key_phrase} -> Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
