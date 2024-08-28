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

def encode(plaintext, grid):
    """Encodes the plaintext using the Playfair cipher."""
    plaintext = re.sub(r'[^A-Z]', '', plaintext.upper()).replace('J', 'I')
    digraphs = [plaintext[i:i+2] for i in range(0, len(plaintext), 2)]
    digraphs = [d if len(d) == 2 else d + 'X' for d in digraphs]
    ciphertext = []
    for d in digraphs:
        c1, c2 = d
        r1, c1 = find_position(c1, grid)
        r2, c2 = find_position(c2, grid)
        if r1 == r2:
            ciphertext.append(grid[r1][(c1 + 1) % 5])
            ciphertext.append(grid[r2][(c2 + 1) % 5])
        elif c1 == c2:
            ciphertext.append(grid[(r1 + 1) % 5][c1])
            ciphertext.append(grid[(r2 + 1) % 5][c2])
        else:
            ciphertext.append(grid[r1][c2])
            ciphertext.append(grid[r2][c1])
    return ''.join(ciphertext)

if __name__ == "__main__":
    key = input("Enter keyword: ")
    plaintext = input("Enter message: ")

    grid = create_matrix(key)
    ciphertext = encode(plaintext, grid)
    print(f"Encrypted message: {ciphertext}")