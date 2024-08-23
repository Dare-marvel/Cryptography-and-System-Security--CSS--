def generate_repeated_key(text, keyword):
    keyword = keyword.upper()
    repeated_key = keyword
    while len(repeated_key) < len(text):
        repeated_key += keyword
    return repeated_key[:len(text)]

def encode_message(text, keyword):
    text = text.upper().replace(" ", "")
    keyword = generate_repeated_key(text, keyword)
    
    encoded_message = ""
    for i in range(len(text)):
        text_char = ord(text[i]) - ord('A')
        key_char = ord(keyword[i]) - ord('A')
        cipher_char = (text_char + key_char) % 26
        encoded_message += chr(cipher_char + ord('A'))

    return encoded_message

if __name__ == "__main__":
    keyword = input("Enter the keyword: ")
    text = input("Enter the text: ")

    encrypted_message = encode_message(text, keyword)
    print("Encoded text:", encrypted_message)
