from itertools import permutations


def decrypt_columnar_transposition(ciphertext, column_order, num_columns):
    # Calculate the number of rows
    num_rows = len(ciphertext) // num_columns

    # Create an empty matrix to store the characters
    matrix = ['' for _ in range(num_columns)]

    # Distribute characters into columns based on the provided order
    k = 0
    for col in column_order:
        for row in range(num_rows):
            matrix[col] += ciphertext[k]
            k += 1

    plaintext = ''.join([''.join(row) for row in zip(*matrix)])
    return plaintext


def brute_force_columnar_transposition(ciphertext):
    possible_plaintexts = []
    for num_columns in range(2, len(ciphertext)):
        if len(ciphertext) % num_columns == 0:
            # Generate all possible column permutations
            for column_order in permutations(range(num_columns)):
                decrypted_text = decrypt_columnar_transposition(
                    ciphertext, column_order, num_columns)
                possible_plaintexts.append(
                    (num_columns, column_order, decrypted_text))
    return possible_plaintexts


# Read the ciphertext from a file
with open('C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-attack-2021300101\\input_output_columnar\\columnar_input.txt', 'r') as infile:
    ciphertext = infile.read().strip()

# Get the possible decryption results
results = brute_force_columnar_transposition(ciphertext)

# Write the outputs to a new text file
with open('C:\\Users\\aspur\\OneDrive\\CSS\\2021300101 - EXP_2\\substitution-techniques-attack-2021300101\\input_output_columnar\\columnar_output.txt', 'w') as outfile:
    for num_columns, column_order, plaintext in results:
        outfile.write(
            f"Columns: {num_columns}, Column Order: {column_order}, Plaintext: {plaintext}\n")
