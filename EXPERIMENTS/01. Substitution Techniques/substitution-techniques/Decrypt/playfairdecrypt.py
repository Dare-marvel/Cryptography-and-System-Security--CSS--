import re

def create_matrix(key):
    matrix = []
    key = key.upper().replace("J", "I")
    used = set()

    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used:
            matrix.append(char)
            used.add(char)

    # Convert to a 5x5 matrix
    matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return matrix

def find_position(char, matrix):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def decrypt_text(ciphertext, matrix):
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper().replace("J", "I"))
    
    digraphs = []
    i = 0
    while i < len(ciphertext):
        a = ciphertext[i]
        if i + 1 < len(ciphertext):
            b = ciphertext[i + 1]
            if a == b: 
                b = 'X'
                i += 1
            else:
                i += 2
        else:
            b = 'X' 
            i += 1
        digraphs.append(a + b)

    plaintext = []
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)

        if row_a == row_b:
            plaintext.append(matrix[row_a][(col_a - 1) % 5])
            plaintext.append(matrix[row_b][(col_b - 1) % 5])
        elif col_a == col_b:
            plaintext.append(matrix[(row_a - 1) % 5][col_a])
            plaintext.append(matrix[(row_b - 1) % 5][col_b])
        else:
            plaintext.append(matrix[row_a][col_b])
            plaintext.append(matrix[row_b][col_a])

    return ''.join(plaintext)

if __name__ == "__main__":
    key = input("Enter the key: ")
    ciphertext = input("Enter the ciphertext: ")

    matrix = create_matrix(key)
    plaintext = decrypt_text(ciphertext, matrix)
    
    print(f"Decrypted text: {plaintext}")
