from itertools import product

def create_playfair_key_matrix(key_phrase):
    matrix = []
    used_chars = set()
    
    # Remove duplicates and insert key characters
    for char in key_phrase:
        if char not in used_chars and char != 'j':
            used_chars.add(char)
            matrix.append(char)
    
    # Fill the remaining cells with the rest of the alphabet
    for code in range(ord('a'), ord('z') + 1):
        letter = chr(code)
        if letter not in used_chars and letter != 'j':
            used_chars.add(letter)
            matrix.append(letter)
    
    # Convert the list to a 5x5 matrix
    return [matrix[i:i + 5] for i in range(0, 25, 5)]

def locate_char_position(matrix, char):
    for row_idx, row in enumerate(matrix):
        if char in row:
            return row_idx, row.index(char)
    return None

def decrypt_playfair(cipher_text, key_phrase):
    key_matrix = create_playfair_key_matrix(key_phrase)
    decrypted_text = []
    
    # Ensure the ciphertext length is even
    if len(cipher_text) % 2 != 0:
        cipher_text += 'x'  # Append a filler character if length is odd
    
    for idx in range(0, len(cipher_text), 2):
        char1 = cipher_text[idx]
        char2 = cipher_text[idx + 1]
        
        pos1 = locate_char_position(key_matrix, char1)
        pos2 = locate_char_position(key_matrix, char2)
        
        if pos1 is None or pos2 is None:
            decrypted_text.append(char1)
            decrypted_text.append(char2)
            continue
        
        if pos1[0] == pos2[0]:  # Same row
            decrypted_text.append(key_matrix[pos1[0]][(pos1[1] - 1) % 5])
            decrypted_text.append(key_matrix[pos2[0]][(pos2[1] - 1) % 5])
        elif pos1[1] == pos2[1]:  # Same column
            decrypted_text.append(key_matrix[(pos1[0] - 1) % 5][pos1[1]])
            decrypted_text.append(key_matrix[(pos2[0] - 1) % 5][pos2[1]])
        else:  # Rectangle swap
            decrypted_text.append(key_matrix[pos1[0]][pos2[1]])
            decrypted_text.append(key_matrix[pos2[0]][pos1[1]])
    
    return ''.join(decrypted_text)

def main():
    cipher_text = "gkelsbqdblsrifbz"
    possible_keys = ["secret", "playfair", "example", "keyword", "random", "monarch"]
    
    for key_phrase in possible_keys:
        decrypted_text = decrypt_playfair(cipher_text, key_phrase)
        print(f"Key: {key_phrase} -> Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
