def decrypt_polyalphabetic(ciphertext, key):
    plaintext = []
    key = key.upper()
    key_length = len(key)

    for i, c in enumerate(ciphertext):
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            shift = ord(key[i % key_length]) - ord('A')
            decrypted_char = chr((ord(c) - base - shift + 26) % 26 + base)
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)

    return ''.join(plaintext)

def generate_keys(alphabet, key_length, prefix, keys):
    if key_length == 0:
        keys.append(prefix)
        return
    for char in alphabet:
        generate_keys(alphabet, key_length - 1, prefix + char, keys)

def brute_force_polyalphabetic(ciphertext, max_key_length):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    keys = []

    for length in range(1, max_key_length + 1):
        generate_keys(alphabet, length, "", keys)

        for key in keys:
            plaintext = decrypt_polyalphabetic(ciphertext, key)
            print(f'Trying key "{key}": {plaintext}')

        keys.clear()

if __name__ == "__main__":
    ciphertext = "lxmpu"
    max_key_length = 3

    brute_force_polyalphabetic(ciphertext, max_key_length)
