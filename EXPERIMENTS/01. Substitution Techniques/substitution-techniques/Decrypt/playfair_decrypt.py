import re

def generate_matrix(keyword):
    grid = []
    keyword = keyword.upper().replace("J", "I")
    used_chars = set()

    for char in keyword:
        if char not in used_chars and char.isalpha():
            grid.append(char)
            used_chars.add(char)

    for char in 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in used_chars:
            grid.append(char)
            used_chars.add(char)

    # Convert to a 5x5 grid
    grid = [grid[i:i+5] for i in range(0, 25, 5)]
    return grid

def locate_position(character, grid):
    for row_index, row in enumerate(grid):
        if character in row:
            return row_index, row.index(character)
    return None

def decrypt_message(encrypted_text, grid):
    encrypted_text = re.sub(r'[^A-Z]', '', encrypted_text.upper().replace("J", "I"))
    
    pairs = []
    index = 0
    while index < len(encrypted_text):
        first_char = encrypted_text[index]
        if index + 1 < len(encrypted_text):
            second_char = encrypted_text[index + 1]
            if first_char == second_char:
                second_char = 'X'
                index += 1
            else:
                index += 2
        else:
            second_char = 'X'
            index += 1
        pairs.append(first_char + second_char)

    plaintext = []
    for pair in pairs:
        char1, char2 = pair[0], pair[1]
        row1, col1 = locate_position(char1, grid)
        row2, col2 = locate_position(char2, grid)

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

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    encrypted_text = input("Enter the encrypted text: ")

    grid = generate_matrix(keyword)
    plaintext = decrypt_message(encrypted_text, grid)
    
    print(f"Decrypted text: {plaintext}")
