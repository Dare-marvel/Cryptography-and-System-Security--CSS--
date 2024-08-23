def generate_repeated_key(encrypted_text, keyword):
    keyword = keyword.upper()
    repeated_key = keyword
    while len(repeated_key) < len(encrypted_text):
        repeated_key += keyword
    return repeated_key[:len(encrypted_text)]

def decipher(encrypted_text, keyword):
    encrypted_text = encrypted_text.upper().replace(" ", "")
    keyword = generate_repeated_key(encrypted_text, keyword)
    
    decrypted_message = ""
    for i in range(len(encrypted_text)):
        cipher_char = ord(encrypted_text[i]) - ord('A')
        key_char = ord(keyword[i]) - ord('A')
        plain_char = (cipher_char - key_char) % 26
        decrypted_message += chr(plain_char + ord('A'))

    return decrypted_message

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    encrypted_text = input("Enter the encrypted text: ")

    decrypted_message = decipher(encrypted_text, keyword)
    print("Decrypted message:", decrypted_message)
