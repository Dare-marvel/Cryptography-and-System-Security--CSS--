def letter_to_number(letter):
    return ord(letter) - ord('A')


def number_to_letter(number):
    return chr(number + ord('A'))


def determinant_matrix(key_matrix):
    determinant = key_matrix[0][0] * key_matrix[1][1] - key_matrix[0][1] * key_matrix[1][0]
    return determinant


def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse found for {a} under modulo {m}")


def inverse_matrix(key_matrix):
    determinant = determinant_matrix(key_matrix)
    scalar = mod_inverse(determinant % 26, 26)
    inverse_key_matrix = [
        [(key_matrix[1][1] * scalar) % 26, ((-key_matrix[0][1] % 26) * scalar) % 26],
        [((-key_matrix[1][0] % 26) * scalar) % 26, (key_matrix[0][0] * scalar) % 26]
    ]
    return inverse_key_matrix


def vector_matrix_multiplication(key_matrix, vector):
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += key_matrix[i][j] * vector[j]
            result[i] %= 26
    return result


def hill_decrypt(encrypted_word, key_matrix):
    decrypted_word = ""
    inverse_key_matrix = inverse_matrix(key_matrix)
    for i in range(0, len(encrypted_word), 2):
        vector = [letter_to_number(encrypted_word[i]), letter_to_number(encrypted_word[i + 1])]
        decrypted_vector = vector_matrix_multiplication(inverse_key_matrix, vector)
        decrypted_letters = [number_to_letter(num) for num in decrypted_vector]
        decrypted_word += "".join(decrypted_letters)

    return decrypted_word


def main():
    print("Hill Cipher Decryption")
    
    key_matrix = [[3, 3], [2, 5]]  # Default key matrix

    encrypted = input("Enter the encrypted word: ").upper()
    decrypted = hill_decrypt(encrypted, key_matrix)
    print("Decrypted word:", decrypted)


if __name__ == "__main__":
    main()
