def char_to_index(character):
    return ord(character) - ord('A')

def index_to_char(index):
    return chr(index + ord('A'))

def matrix_vector_multiplication(matrix, vector):
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += matrix[i][j] * vector[j]
            result[i] %= 26
    return result

def encrypt_hill_cipher(text, matrix):
    encrypted_text = ""
    for i in range(0, len(text), 2):
        vector = [char_to_index(text[i]), char_to_index(text[i + 1])]
        encrypted_vector = matrix_vector_multiplication(matrix, vector)
        encrypted_chars = [index_to_char(num) for num in encrypted_vector]
        encrypted_text += "".join(encrypted_chars)

    return encrypted_text

def main():
    print("Hill Cipher Encryption")
    
    key_matrix = [[3, 3], [2, 5]]  # Default key matrix

    text = input("Enter a text with an even number of characters: ").upper()
    if len(text) % 2 != 0:
        print("Text length must be even. Padding with 'X'.")
        text += 'X'

    encrypted = encrypt_hill_cipher(text, key_matrix)
    print("Encrypted text:", encrypted)

if __name__ == "__main__":
    main()
