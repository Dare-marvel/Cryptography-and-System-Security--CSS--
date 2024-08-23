from itertools import product
from math import gcd

class HillCipherCracker:

    @staticmethod
    def decrypt_block(matrix, cipher_block):
        plain_block = [0] * len(cipher_block)

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                plain_block[i] += matrix[i][j] * cipher_block[j]
            plain_block[i] = (plain_block[i] % 26 + 26) % 26  # Ensure non-negative modulo

        return plain_block

    @staticmethod
    def text_to_numbers(text):
        return [ord(char) - ord('A') for char in text]

    @staticmethod
    def numbers_to_text(numbers):
        return ''.join(chr(num + ord('A')) for num in numbers)

    @staticmethod
    def is_invertible(matrix):
        determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
        determinant = (determinant + 26) % 26  # Ensure non-negative

        # Check if determinant has a modular inverse (i.e., gcd(det, 26) == 1)
        return gcd(determinant, 26) == 1

    @staticmethod
    def generate_invertible_matrices():
        matrices = []
        for a, b, c, d in product(range(26), repeat=4):
            matrix = [[a, b], [c, d]]
            if HillCipherCracker.is_invertible(matrix):
                matrices.append(matrix)
        return matrices

    @staticmethod
    def brute_force_decryption(ciphertext):
        matrices = HillCipherCracker.generate_invertible_matrices()
        cipher_numbers = HillCipherCracker.text_to_numbers(ciphertext)

        print("Brute-forcing...")
        for matrix in matrices:
            decrypted_text = []

            # Process ciphertext in blocks of 2 (for 2x2 matrix)
            for i in range(0, len(cipher_numbers), 2):
                block = [cipher_numbers[i], cipher_numbers[i + 1]]
                decrypted_block = HillCipherCracker.decrypt_block(matrix, block)
                decrypted_text.append(HillCipherCracker.numbers_to_text(decrypted_block))

            decrypted_text_str = ''.join(decrypted_text)
            print(f"Trying matrix: [[{matrix[0][0]}, {matrix[0][1]}], "
                  f"[{matrix[1][0]}, {matrix[1][1]}]] - Decrypted Text: {decrypted_text_str}")

if __name__ == "__main__":
    ciphertext = "GFWIQPGQ"
    HillCipherCracker.brute_force_decryption(ciphertext)
