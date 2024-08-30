import math
import matplotlib.pyplot as plt
from collections import Counter

def calculate_frequencies(text):
    text = text.upper().replace(" ", "")
    counter = Counter(text)
    total = sum(counter.values())
    frequencies = {char: (count / total) * 100 for char, count in counter.items()}
    return frequencies

def plot_frequencies(plain_freq, rail_freq, columnar_freq):
    # Define all letters for x-axis
    all_letters = sorted(set(plain_freq.keys()).union(rail_freq.keys()).union(columnar_freq.keys()))
    
    # Prepare data for plotting
    plain_freq_values = [plain_freq.get(letter, 0) for letter in all_letters]
    rail_freq_values = [rail_freq.get(letter, 0) for letter in all_letters]
    columnar_freq_values = [columnar_freq.get(letter, 0) for letter in all_letters]
    
    # Plotting
    plt.figure(figsize=(12, 8))
    plt.plot(all_letters, plain_freq_values, marker='o', linestyle='-', label='Plaintext')
    plt.plot(all_letters, rail_freq_values, marker='s', linestyle='--', label='Rail Fence Cipher')
    plt.plot(all_letters, columnar_freq_values, marker='^', linestyle='-.', label='Columnar Cipher')
    
    plt.xlabel('Letters')
    plt.ylabel('Relative Frequency (%)')
    plt.title('Relative Letter Frequencies: Plaintext vs Rail Fence Cipher vs Columnar Cipher')
    plt.legend()
    plt.grid(True)
    plt.savefig("plot.png")
    plt.show()


plaintext = "This is an example message that has more than one hundred and seventy characters. It is used to demonstrate how the encryption function handles longer messages. This should be sufficient."

def encryptRailFence(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    
    # Direction flag
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

rail_fence_ciphertext = encryptRailFence(plaintext,3)

def encryptMessage(msg, key):
    cipher = ""

    # track key indices
    k_indx = 0

    msg_len = float(len(msg))
    msg_lst = list(msg)
    key_lst = sorted(list(key))

    # calculate column of the matrix
    col = len(key)

    # calculate maximum row of the matrix
    row = int(math.ceil(msg_len / col))
    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)
    matrix = [msg_lst[i: i + col] for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx] for row in matrix])
        k_indx += 1

    return cipher
columnar_ciphertext = encryptMessage(plaintext,"KEYWORD")

# Calculate frequencies
plain_freq = calculate_frequencies(plaintext)
rail_freq = calculate_frequencies(rail_fence_ciphertext)
columnar_freq = calculate_frequencies(columnar_ciphertext)

# Plotting
plot_frequencies(plain_freq, rail_freq, columnar_freq)
