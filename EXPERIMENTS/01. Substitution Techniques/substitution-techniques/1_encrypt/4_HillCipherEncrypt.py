def char_to_num(char):
    """Converts a character to its corresponding numerical value."""
    return ord(char) - ord('A')

def num_to_char(num):
    """Converts a numerical value to its corresponding character."""
    return chr(num + ord('A'))

def matrix_multiplication(matrix, vector):
    """Performs matrix-vector multiplication."""
    result = [0, 0]
    for i in range(2):
        for j in range(2):
            result[i] += matrix[i][j] * vector[j]
            result[i] %= 26
    return result

def hill_cipher_encrypt(plaintext, key):
    """Encrypts plaintext using the Hill cipher."""
    ciphertext = ""
    for i in range(0, len(plaintext), 2):
        vector = [char_to_num(plaintext[i]), char_to_num(plaintext[i + 1])]
        encrypted_vector = matrix_multiplication(key, vector)
        ciphertext += "".join([num_to_char(num) for num in encrypted_vector])
    return ciphertext

def main():
    print("Hill Cipher Encryption")
    key = input("Enter the key matrix (default = [[3, 3], [2, 5]]): ")
    if key == "":
        key = [[3, 3], [2, 5]]
    else:
        key = eval(key)
    plaintext = input("Enter a text with an even number of characters: ").upper()
    if len(plaintext) % 2 != 0:
        print("Text length must be even. Padding with 'X'.")
        plaintext += 'X'
    ciphertext = hill_cipher_encrypt(plaintext, key)
    print("Encrypted text:", ciphertext)

if __name__ == "__main__":
    main()