import re

def generate_matrix(keyword):
    grid = []
    keyword = keyword.upper().replace("J", "I")
    used_chars = set()

    # Insert the keyword into the grid
    for char in keyword:
        if char not in used_chars and char.isalpha():
            grid.append(char)
            used_chars.add(char)

    # Insert the remaining letters of the alphabet
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

def encode_message(message, grid):
    message = re.sub(r'[^A-Z]', '', message.upper())
    message = message.replace('J', 'I')
    
    # Split into digraphs
    digraphs = []
    index = 0
    while index < len(message):
        first_char = message[index]
        if index + 1 < len(message):
            second_char = message[index + 1]
            if first_char != second_char:
                digraphs.append(first_char + second_char)
                index += 2
            else:
                digraphs.append(first_char + 'X')
                index += 1
        else:
            digraphs.append(first_char + 'X')
            index += 1

    encrypted_message = []
    for digraph in digraphs:
        char1, char2 = digraph[0], digraph[1]
        row1, col1 = locate_position(char1, grid)
        row2, col2 = locate_position(char2, grid)

        if row1 == row2:
            encrypted_message.append(grid[row1][(col1 + 1) % 5])
            encrypted_message.append(grid[row2][(col2 + 1) % 5])
        elif col1 == col2:
            encrypted_message.append(grid[(row1 + 1) % 5][col1])
            encrypted_message.append(grid[(row2 + 1) % 5][col2])
        else:
            encrypted_message.append(grid[row1][col2])
            encrypted_message.append(grid[row2][col1])

    return ''.join(encrypted_message)

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    message = input("Enter the message: ")

    grid = generate_matrix(keyword)
    encrypted_message = encode_message(message, grid)
    
    print(f"Encrypted message: {encrypted_message}")
