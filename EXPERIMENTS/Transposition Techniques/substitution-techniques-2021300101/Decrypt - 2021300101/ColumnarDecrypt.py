import math

def decryptMessage(cipher, key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))

    key_lst = sorted(list(key))

    print("Column order based on sorted key:")
    column_order = [key.index(k) for k in key_lst]
    print(column_order)

    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])

        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1

    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("This program cannot handle repeating words.")

    null_count = msg.count('_')

    if null_count > 0:
        return msg[: -null_count]

    return msg

if __name__ == "__main__":
    input_file = "C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_decrypt\\columnar_encrypted_message.txt"
    output_file = "C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-2021300101\\input_output_files_for_decrypt\\columnar_decrypted_message.txt"

    with open(input_file, "r") as infile:
        encrypted_msg = infile.readline().strip()
        key = infile.readline().strip()

    decrypted_msg = decryptMessage(encrypted_msg, key)

    with open(output_file, "a") as outfile:
        outfile.write("Columnar Decrypt\n")
        outfile.write(f"The Decrypted Message: {decrypted_msg}\n\n")

    print(f"The Decrypted Message: {decrypted_msg}")
