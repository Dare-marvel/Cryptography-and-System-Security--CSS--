import math

def encryptMessage(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))
    col = len(key)
    row = int(math.ceil(msg_len / col))

    # add the padding character '_' in empty cells of the matrix
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    # read matrix column-wise using key
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher

if __name__ == "__main__":
    # Read input from a file
    with open("C:\\Users\\aspur\\OneDrive\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_encrypt\\plaintext_columnar.txt", "r") as file:
        lines = file.readlines()
        msg = lines[0].strip()  # First line is the message
        key = lines[1].strip()  # Second line is the key

    # Encrypt the message
    cipher = encryptMessage(msg, key)

    # Write the output to a file
    with open("C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_encrypt\\columnar_output.txt", "w") as file:
        file.write(f"Encrypted Message for Columnar: {cipher}")

