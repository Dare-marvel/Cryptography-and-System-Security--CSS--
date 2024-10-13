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

if __name__ == "__main__":

    input_file = "C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_decrypt\\rail_encrypted_message.txt"
    output_file = "C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_decrypt\\rail_decrypted_message.txt"

    with open(input_file, "r") as infile:
        encrypted_text = infile.readline().strip()
        key = int(infile.readline().strip())

    decrypted_text = decryptRailFence(encrypted_text, key)

    with open(output_file, "a") as outfile:
        outfile.write("Rail Fence Decrypt\n")
        outfile.write(f"The Decrypted Message: {decrypted_text}\n\n")

    print(f"The Decrypted Message: {decrypted_text}")

