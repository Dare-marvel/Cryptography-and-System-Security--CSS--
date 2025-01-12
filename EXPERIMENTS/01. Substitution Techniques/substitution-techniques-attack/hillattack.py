from itertools import product
from math import gcd

class HillAttack:

    @staticmethod
    def decrypt_block(key_matrix, cipher_block):
        plain_block = [0] * len(cipher_block)

        for i in range(len(key_matrix)):
            for j in range(len(key_matrix[i])):
                plain_block[i] += key_matrix[i][j] * cipher_block[j]
            plain_block[i] = (plain_block[i] % 26 + 26) % 26  # Ensure non-negative modulo

        return plain_block

    @staticmethod
    def convert_to_numbers(text):
        return [ord(char) - ord('A') for char in text]

    @staticmethod
    def convert_to_text(numbers):
        return ''.join(chr(num + ord('A')) for num in numbers)

    @staticmethod
    def is_matrix_invertible(matrix):
        determinant = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % 26
        determinant = (determinant + 26) % 26  # Ensure non-negative

        # Check if determinant has a modular inverse (i.e., gcd(det, 26) == 1)
        return gcd(determinant, 26) == 1

    @staticmethod
    def generate_key_matrices():
        key_matrices = []
        for a, b, c, d in product(range(26), repeat=4):
            matrix = [[a, b], [c, d]]
            if HillAttack.is_matrix_invertible(matrix):
                key_matrices.append(matrix)
        return key_matrices

    @staticmethod
    def brute_force_hill_cipher(ciphertext):
        key_matrices = HillAttack.generate_key_matrices()
        cipher_numbers = HillAttack.convert_to_numbers(ciphertext)

        print("Brute-forcing...")
        for key_matrix in key_matrices:
            decrypted_text = []

            # Process ciphertext in blocks of 2 (for 2x2 matrix)
            for i in range(0, len(cipher_numbers), 2):
                block = [cipher_numbers[i], cipher_numbers[i + 1]]
                decrypted_block = HillAttack.decrypt_block(key_matrix, block)
                decrypted_text.append(HillAttack.convert_to_text(decrypted_block))

            decrypted_text_str = ''.join(decrypted_text)
            print(f"Trying key: [[{key_matrix[0][0]}, {key_matrix[0][1]}], "
                  f"[{key_matrix[1][0]}, {key_matrix[1][1]}]] - Decrypted Text: {decrypted_text_str}")

if __name__ == "__main__":
    ciphertext = "GFWIQPGQ"
    HillAttack.brute_force_hill_cipher(ciphertext)
