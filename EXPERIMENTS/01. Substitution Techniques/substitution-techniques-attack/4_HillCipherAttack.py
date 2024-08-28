from itertools import product
from math import gcd

class HillCipherCracker:
    """Cracks Hill ciphers by brute-forcing invertible matrices."""

    @staticmethod
    def matrix_mod_inverse(matrix, modulus):
        """Finds the modular inverse of a 2x2 matrix."""
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % modulus
        det_inv = pow(det, -1, modulus)
        return [
            [(matrix[1][1] * det_inv) % modulus, (-matrix[0][1] * det_inv) % modulus],
            [(-matrix[1][0] * det_inv) % modulus, (matrix[0][0] * det_inv) % modulus]
        ]

    @staticmethod
    def decrypt_block(key_matrix, cipher_block):
        """Decrypts a block of ciphertext using the inverse of the key matrix."""
        inv_key = HillCipherCracker.matrix_mod_inverse(key_matrix, 26)
        plain_block = [0, 0]
        for i in range(2):
            for j in range(2):
                plain_block[i] += inv_key[i][j] * cipher_block[j]
            plain_block[i] = plain_block[i] % 26
        return plain_block

    @staticmethod
    def text_to_numbers(text):
        """Converts text to numerical values."""
        return [ord(char) - ord('A') for char in text]

    @staticmethod
    def numbers_to_text(numbers):
        """Converts numerical values to text."""
        return ''.join(chr(num + ord('A')) for num in numbers)

    @staticmethod
    def is_invertible(key_matrix):
        """Checks if a matrix is invertible."""
        det = (key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]) % 26
        return gcd(det, 26) == 1

    @staticmethod
    def generate_invertible_matrices():
        """Generates all invertible 2x2 matrices."""
        matrices = []
        for a, b, c, d in product(range(26), repeat=4):
            key_matrix = [[a, b], [c, d]]
            if HillCipherCracker.is_invertible(key_matrix):
                matrices.append(key_matrix)
        return matrices

    @staticmethod
    def brute_force_decryption(ciphertext):
        """Brute-forces decryption using all invertible matrices."""
        key_matrices = HillCipherCracker.generate_invertible_matrices()
        cipher_numbers = HillCipherCracker.text_to_numbers(ciphertext)

        print("Brute-forcing...")
        for key_matrix in key_matrices:
            decrypted_text = []
            for i in range(0, len(cipher_numbers), 2):
                block = [cipher_numbers[i], cipher_numbers[i + 1]]
                decrypted_block = HillCipherCracker.decrypt_block(key_matrix, block)
                decrypted_text.extend(decrypted_block)
            decrypted_text_str = HillCipherCracker.numbers_to_text(decrypted_text)
            print(f"Trying matrix: {key_matrix} - Decrypted Text: {decrypted_text_str}")

def main():
    ciphertext = input("Enter the ciphertext: ")
    HillCipherCracker.brute_force_decryption(ciphertext)

if __name__ == "__main__":
    main()