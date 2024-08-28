def char_to_num(char):
    """Converts a character to its corresponding numerical value."""
    return ord(char) - ord('A')

def num_to_char(num):
    """Converts a numerical value to its corresponding character."""
    return chr(num + ord('A'))

def calculate_determinant(matrix):
    """Calculates the determinant of a 2x2 matrix."""
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

def mod_inverse(a, mod):
    """Finds the modular inverse of a under modulo mod."""
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse found for {a} under modulo {mod}")

def calculate_inverse_matrix(matrix):
    """Calculates the inverse of a 2x2 matrix under modulo 26."""
    det = calculate_determinant(matrix)
    scalar = mod_inverse(det % 26, 26)
    return [
        [(matrix[1][1] * scalar) % 26, ((-matrix[0][1] % 26) * scalar) % 26],
        [((-matrix[1][0] % 26) * scalar) % 26, (matrix[0][0] * scalar) % 26]
    ]

def matrix_vector_multiply(matrix, vector):
    """Multiplies a 2x2 matrix with a 2x1 vector under modulo 26."""
    product = [0, 0]
    for i in range(2):
        for j in range(2):
            product[i] += matrix[i][j] * vector[j]
            product[i] %= 26
    return product

def decrypt_hill_cipher(ciphertext, key_matrix=[[3, 3], [2, 5]]):
    """Decrypts a ciphertext using the Hill cipher."""
    inverse_matrix = calculate_inverse_matrix(key_matrix)
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        vector = [char_to_num(ciphertext[i]), char_to_num(ciphertext[i + 1])]
        decrypted_vector = matrix_vector_multiply(inverse_matrix, vector)
        decrypted_chars = [num_to_char(num) for num in decrypted_vector]
        plaintext += "".join(decrypted_chars)
    return plaintext

def main():
    print("Hill Cipher Decryption")
    key_matrix = input("Enter the key matrix (default = [[3, 3], [2, 5]]): ")
    if key_matrix == "":
        key_matrix = [[3, 3], [2, 5]]
    else:
        key_matrix = eval(key_matrix)
    ciphertext = input("Enter the encrypted text: ").upper()
    decrypted_text = decrypt_hill_cipher(ciphertext, key_matrix)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()