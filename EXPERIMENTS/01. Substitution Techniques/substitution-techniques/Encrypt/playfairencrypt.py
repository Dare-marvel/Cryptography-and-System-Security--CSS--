import re

def create_matrix(key):
    matrix = []
    key = key.upper().replace("J", "I")
    used = set()

    # Insert the key into the matrix
    for char in key:
        if char not in used and char.isalpha():
            matrix.append(char)
            used.add(char)

    # Insert the remaining letters of the alphabet
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

def encrypt_text(plaintext, matrix):
    plaintext = re.sub(r'[^A-Z]', '', plaintext.upper())
    plaintext = plaintext.replace('J', 'I')
    
    # Split into digraphs
    digraphs = []
    i = 0
    while i < len(plaintext):
        a = plaintext[i]
        if i + 1 < len(plaintext):
            b = plaintext[i + 1]
            if a != b:
                digraphs.append(a + b)
                i += 2
            else:
                digraphs.append(a + 'X')
                i += 1
        else:
            digraphs.append(a + 'X')
            i += 1

    ciphertext = []
    for digraph in digraphs:
        a, b = digraph[0], digraph[1]
        row_a, col_a = find_position(a, matrix)
        row_b, col_b = find_position(b, matrix)

        if row_a == row_b:
            ciphertext.append(matrix[row_a][(col_a + 1) % 5])
            ciphertext.append(matrix[row_b][(col_b + 1) % 5])
        elif col_a == col_b:
            ciphertext.append(matrix[(row_a + 1) % 5][col_a])
            ciphertext.append(matrix[(row_b + 1) % 5][col_b])
        else:
            ciphertext.append(matrix[row_a][col_b])
            ciphertext.append(matrix[row_b][col_a])

    return ''.join(ciphertext)

if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")

    matrix = create_matrix(key)
    ciphertext = encrypt_text(plaintext, matrix)
    
    print(f"Encrypted text: {ciphertext}")
