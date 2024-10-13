def decryptRailFence(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    
    # Direction flag
    dir_down = None
    row, col = 0, 0
    
    # Mark the places with '*'
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        rail[row][col] = '*'
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1
            
    # Fill the rail matrix
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
                
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
            
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)

def brute_force_rail_fence(ciphertext):
    possible_plaintexts = []
    for num_rails in range(2, len(ciphertext) + 1):
        decrypted_text = decryptRailFence(ciphertext, num_rails)
        possible_plaintexts.append((num_rails, decrypted_text))
    return possible_plaintexts

# Read the ciphertext from a file
with open('C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-attack-2021300101\\input_output_rail\\rail_input.txt', 'r') as infile:
    ciphertext = infile.read().strip()

# Get the possible decryption results
results = brute_force_rail_fence(ciphertext)

# Write the outputs to a new text file
with open('C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-attack-2021300101\\input_output_rail\\rail_output.txt', 'w') as outfile:
    for num_rails, plaintext in results:
        outfile.write(f"Rails: {num_rails}, Plaintext: {plaintext}\n")