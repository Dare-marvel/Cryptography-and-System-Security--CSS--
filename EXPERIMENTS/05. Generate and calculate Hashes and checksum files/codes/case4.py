from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as crypt_padding
import hashlib
from sha512 import sha512
import os

class AESCipher:
    """Handles AES encryption and decryption using CBC mode."""
    def __init__(self, key):
        self.key = key

    def encrypt(self, data: str) -> bytes:
        """Encrypts the data using AES with CBC mode and PKCS7 padding."""
        if isinstance(data, str):
            data = data.encode('utf-8')

        iv = os.urandom(16)  # Generate a random 16-byte IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Apply PKCS7 padding
        padder = crypt_padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext

    def decrypt(self, encrypted_data: bytes) -> str:
        """Decrypts the data using AES with CBC mode and removes PKCS7 padding."""
        try:
            iv = encrypted_data[:16]
            ciphertext = encrypted_data[16:]

            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

            # Remove PKCS7 padding
            unpadder = crypt_padding.PKCS7(algorithms.AES.block_size).unpadder()
            plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

            return plaintext.decode('utf-8')
        except (ValueError, UnicodeDecodeError):
            print("Decryption failed. The message may have been tampered with.")
            return None

class MessageHasher:
    """Handles message hashing with a seed using SHA-512."""
    @staticmethod
    def hash_message(message: str, seed: str) -> str:
        """Generates the SHA-512 hash of a message concatenated with a seed."""
        return sha512(message + seed)

class SecureMessenger:
    """Handles sending and receiving secure messages with AES encryption and hash verification."""
    def __init__(self, aes_key: bytes, seed: str):
        self.aes_cipher = AESCipher(aes_key)
        self.seed = seed

    def send(self, message: str) -> bytes:
        """Encrypts the message with its hash appended and returns the encrypted data."""
        message_hash = MessageHasher.hash_message(message, self.seed)
        combined_message = message + message_hash

        encrypted_message = self.aes_cipher.encrypt(combined_message)
        print(f"Message: {message}")
        print(f"Sending encrypted message: {encrypted_message}")
        print(f"Hash: {message_hash}")
        return encrypted_message

    def receive(self, encrypted_message: bytes) -> str:
        """Decrypts the message, verifies its hash, and returns the original message if valid."""
        decrypted_message = self.aes_cipher.decrypt(encrypted_message)
        
        if decrypted_message is None:
            return None
        
        # Extract message and hash
        message = decrypted_message[:-128]
        received_hash = decrypted_message[-128:]
        
        # Recompute the expected hash
        expected_hash = MessageHasher.hash_message(message, self.seed)

        # Verify the hash and return the result
        if received_hash == expected_hash:
            print(f"Message hashes matching\nMessage: {message}\nHash: {received_hash}")
            return message
        else:
            print("Message hashes not matching! Message corrupted.")
            return None

if __name__ == "__main__":
    # Example usage
    seed_test = "thisisasecret"
    aes_key = hashlib.sha256(b'secret_key').digest()

    # Initialize the SecureMessenger
    secure_messenger = SecureMessenger(aes_key, seed_test)

    # Case 1: Correct message transfer
    print("Case 1:")
    sent_message = secure_messenger.send("Python")
    received_message = secure_messenger.receive(sent_message)
    print(f"Received message: {received_message}\n")

    # Case 2: Message tampered after encryption
    print("Case 2:")
    sent_message = secure_messenger.send("csslab")
    
    # Simulate tampering with the encrypted message
    tampered_message = sent_message[:34] + b"3a" + sent_message[36:]
    
    received_message = secure_messenger.receive(tampered_message)
    print(f"Received message: {received_message}")  # Expected None due to tampering