from itertools import product

def generate_playfair_key_matrix(key):
    key_matrix = []
    used_chars = set()
    
    # Removing duplicates and inserting key characters
    for c in key:
        if c not in used_chars and c != 'j':
            used_chars.add(c)
            key_matrix.append(c)
    
    # Filling the remaining cells with the rest of the alphabet
    for c in range(ord('a'), ord('z') + 1):
        char = chr(c)
        if char not in used_chars and char != 'j':
            used_chars.add(char)
            key_matrix.append(char)
    
    # Convert the list to a 5x5 matrix
    return [key_matrix[i:i + 5] for i in range(0, 25, 5)]

def find_position(key_matrix, char):
    for i, row in enumerate(key_matrix):
        if char in row:
            return i, row.index(char)
    return None

def playfair_decrypt(cipher_text, key):
    key_matrix = generate_playfair_key_matrix(key)
    plain_text = []
    
    # Ensure the ciphertext length is even
    if len(cipher_text) % 2 != 0:
        cipher_text += 'x'  # Append a filler character if length is odd
    
    for i in range(0, len(cipher_text), 2):
        a = cipher_text[i]
        b = cipher_text[i + 1]
        
        pos_a = find_position(key_matrix, a)
        pos_b = find_position(key_matrix, b)
        
        if pos_a is None or pos_b is None:
            plain_text.append(a)
            plain_text.append(b)
            continue
        
        if pos_a[0] == pos_b[0]:  # Same row
            plain_text.append(key_matrix[pos_a[0]][(pos_a[1] - 1) % 5])
            plain_text.append(key_matrix[pos_b[0]][(pos_b[1] - 1) % 5])
        elif pos_a[1] == pos_b[1]:  # Same column
            plain_text.append(key_matrix[(pos_a[0] - 1) % 5][pos_a[1]])
            plain_text.append(key_matrix[(pos_b[0] - 1) % 5][pos_b[1]])
        else:  # Rectangle swap
            plain_text.append(key_matrix[pos_a[0]][pos_b[1]])
            plain_text.append(key_matrix[pos_b[0]][pos_a[1]])
    
    return ''.join(plain_text)

def main():
    cipher_text = "gkelsbqdblsrifbz" 
    potential_keys = ["secret", "playfair", "example", "keyword", "random", "monarch"] 
    
    for key in potential_keys:
        decrypted_text = playfair_decrypt(cipher_text, key)
        print(f"Key: {key} -> Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
