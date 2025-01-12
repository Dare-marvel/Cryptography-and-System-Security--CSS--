def letter_to_number(letter):
    return ord(letter) - ord('A')


def number_to_letter(number):
    return chr(number + ord('A'))
 

def vector_matrix_multiplication(key_matrix, vector):
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += key_matrix[i][j] * vector[j]
            result[i] %= 26
    return result


def hill_encrypt(word, key_matrix):
    encrypted_word = ""
    for i in range(0, len(word), 2):
        vector = [letter_to_number(word[i]), letter_to_number(word[i + 1])]
        encrypted_vector = vector_matrix_multiplication(key_matrix, vector)
        encrypted_letters = [number_to_letter(num) for num in encrypted_vector]
        encrypted_word += "".join(encrypted_letters)

    return encrypted_word


def main():
    print("Hill Cipher Encryption")
    
    key_matrix = [[3, 3], [2, 5]]  # Default key matrix

    word = input("Enter a word with an even number of letters: ").upper()
    if len(word) % 2 != 0:
        print("Word length must be even. Padding with 'X'.")
        word += 'X'

    encrypted = hill_encrypt(word, key_matrix)
    print("Encrypted word:", encrypted)


if __name__ == "__main__":
    main()
