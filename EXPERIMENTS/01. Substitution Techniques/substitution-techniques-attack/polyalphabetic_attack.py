def decrypt_vigenere(ciphertext, key_phrase):
    decrypted_text = []
    key_phrase = key_phrase.upper()
    key_length = len(key_phrase)

    for index, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shift = ord(key_phrase[index % key_length]) - ord('A')
            decrypted_char = chr((ord(char) - base - shift + 26) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)

    return ''.join(decrypted_text)

def create_key_combinations(alphabet, length, current_prefix, all_keys):
    if length == 0:
        all_keys.append(current_prefix)
        return
    for letter in alphabet:
        create_key_combinations(alphabet, length - 1, current_prefix + letter, all_keys)

def exhaustive_key_search(ciphertext, max_key_length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key_combinations = []

    for length in range(1, max_key_length + 1):
        create_key_combinations(alphabet, length, "", key_combinations)

        for key in key_combinations:
            decrypted_message = decrypt_vigenere(ciphertext, key)
            print(f'Testing key "{key}": {decrypted_message}')

        key_combinations.clear()

if __name__ == "__main__":
    encrypted_message = "lxmpu"
    maximum_key_length = 3

    exhaustive_key_search(encrypted_message, maximum_key_length)
