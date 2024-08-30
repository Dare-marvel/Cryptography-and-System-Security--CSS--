def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    dir_down = False
    row, col = 0, 0
    
    for i in range(len(text)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        
        rail[row][col] = text[i]
        col += 1
        
        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])
    return "".join(result)

if __name__ == "__main__":

    # Read input from a file
    with open("C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_encrypt\\plaintext_rail.txt", "r") as file:
        lines = file.readlines()
        msg = lines[0].strip()  # First line is the message
        key = int(lines[1].strip())  # Second line is the key

    # Encrypt the message
    cipher = encryptRailFence(msg, key)

    # Write the output to a file
    with open("C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_encrypt\\railfence_output.txt", "w") as file:
        file.write(f"Encrypted Message for RailFence: {cipher}")

