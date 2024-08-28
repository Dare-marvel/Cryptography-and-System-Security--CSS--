import re

def create_matrix(key):
    """Creates a 5x5 Playfair matrix from the key."""
    key = key.upper().replace("J", "I")
    grid = []
    for char in key:
        if char not in grid and char.isalpha():
            grid.append(char)
    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in grid:
            grid.append(char)
    return [grid[i:i+5] for i in range(0, 25, 5)]

def find_position(char, grid):
    """Finds the position of a character in the grid."""
    for i, row in enumerate(grid):
        if char in row:
            return i, row.index(char)
    return None

def playfair_decrypt(ciphertext, grid):
    """Decrypts the ciphertext using the Playfair cipher."""
    ciphertext = re.sub(r'[^A-Z]', '', ciphertext.upper().replace("J", "I"))
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    plaintext = []
    for pair in pairs:
        char1, char2 = pair
        row1, col1 = find_position(char1, grid)
        row2, col2 = find_position(char2, grid)
        if row1 == row2:
            plaintext.append(grid[row1][(col1 - 1) % 5])
            plaintext.append(grid[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(grid[(row1 - 1) % 5][col1])
            plaintext.append(grid[(row2 - 1) % 5][col2])
        else:
            plaintext.append(grid[row1][col2])
            plaintext.append(grid[row2][col1])
    return ''.join(plaintext)

def main():
    key = input("Enter the keyword: ")
    ciphertext = input("Enter the encrypted text: ")

    grid = create_matrix(key)
    plaintext = playfair_decrypt(ciphertext, grid)
    print(f"Decrypted text: {plaintext}")

if __name__ == "__main__":
    main()