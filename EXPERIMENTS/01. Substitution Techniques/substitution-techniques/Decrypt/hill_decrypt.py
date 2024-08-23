def char_to_num(char):
    return ord(char) - ord('A')


def num_to_char(num):
    return chr(num + ord('A'))


def calc_determinant(matrix):
    det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return det


def mod_inverse(a, mod):
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse found for {a} under modulo {mod}")


def calc_inverse_matrix(matrix):
    det = calc_determinant(matrix)
    scalar = mod_inverse(det % 26, 26)
    inv_matrix = [
        [(matrix[1][1] * scalar) % 26, ((-matrix[0][1] % 26) * scalar) % 26],
        [((-matrix[1][0] % 26) * scalar) % 26, (matrix[0][0] * scalar) % 26]
    ]
    return inv_matrix


def matrix_vector_multiply(matrix, vector):
    product = [0, 0]
    for i in range(2):
        for j in range(2):
            product[i] += matrix[i][j] * vector[j]
            product[i] %= 26
    return product


def hill_cipher_decrypt(cipher_text, key_matrix):
    plain_text = ""
    inverse_matrix = calc_inverse_matrix(key_matrix)
    for i in range(0, len(cipher_text), 2):
        vector = [char_to_num(cipher_text[i]), char_to_num(cipher_text[i + 1])]
        decrypted_vector = matrix_vector_multiply(inverse_matrix, vector)
        decrypted_chars = [num_to_char(num) for num in decrypted_vector]
        plain_text += "".join(decrypted_chars)

    return plain_text


def main():
    print("Hill Cipher Decryption")
    
    key_matrix = [[3, 3], [2, 5]]  # Default key matrix

    cipher_text = input("Enter the encrypted text: ").upper()
    decrypted_text = hill_cipher_decrypt(cipher_text, key_matrix)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
