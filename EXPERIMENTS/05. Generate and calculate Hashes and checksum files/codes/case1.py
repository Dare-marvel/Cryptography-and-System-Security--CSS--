from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as crypt_padding
import hashlib
from sha512 import sha512  

class AESCipher:
    def __init__(self, key):
        """Initialize with a key, which should be a 256-bit hash (32 bytes)."""
        self.key = key

    def encrypt(self, data):
        """Encrypts the provided data using AES encryption in CBC mode."""
        if isinstance(data, str):
            data = data.encode('utf-8')
        
        # Generate a random 16-byte IV
        iv = os.urandom(16)
        
        # Initialize cipher
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        
        # Pad the data to make sure it's a multiple of the block size
        padder = crypt_padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data) + padder.finalize()
        
        # Encrypt the data
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        
        return iv + ciphertext

    def decrypt(self, encrypted_data):
        """Decrypts AES encrypted data."""
        iv = encrypted_data[:16]
        ciphertext = encrypted_data[16:]
        
        # Initialize cipher
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        
        # Decrypt the ciphertext
        padded_data = decryptor.update(ciphertext) + decryptor.finalize()
        
        # Unpad the decrypted data
        unpadder = crypt_padding.PKCS7(algorithms.AES.block_size).unpadder()
        original_message_bytes = unpadder.update(padded_data) + unpadder.finalize()
        
        return original_message_bytes.decode('utf-8')

class MessageHasher:
    @staticmethod
    def hash_message(message):
        """Generates SHA-512 hash of the message."""
        return sha512(message)

class SecureMessageHandler:
    def __init__(self, key):
        self.aes_cipher = AESCipher(key)
    
    def encrypt_message(self, message):
        """Hashes the message and encrypts the message with its hash appended."""
        message_hash = MessageHasher.hash_message(message)
        combined_message = message + message_hash
        encrypted_data = self.aes_cipher.encrypt(combined_message)
        return encrypted_data

    def decrypt_message(self, encrypted_data):
        """Decrypts the message and verifies its integrity using hash comparison."""
        decrypted_message = self.aes_cipher.decrypt(encrypted_data)
        
        # Split the decrypted message into original message and hash
        original_message = decrypted_message[:-128]
        received_hash = decrypted_message[-128:]
        
        # Recompute the hash and verify
        computed_hash = MessageHasher.hash_message(original_message)
        verification_status = (received_hash == computed_hash)
        
        return original_message, verification_status

def generate_aes_key(passphrase):
    """Generates a 256-bit AES key from a passphrase using SHA-256."""
    return hashlib.sha256(passphrase).digest()

if __name__ == "__main__":
    import os

    # Generate AES key from passphrase
    aes_key = generate_aes_key(b'secret_key')

    # Initialize the SecureMessageHandler
    message_handler = SecureMessageHandler(aes_key)

    # Message to be encrypted
    message = "This is a secret message."

    # Encrypt the message
    encrypted_data = message_handler.encrypt_message(message)
    print("Encrypted data:", encrypted_data)

    # Decrypt and verify the message
    decrypted_message, verification_status = message_handler.decrypt_message(encrypted_data)
    
    print("Decrypted message:", decrypted_message)
    print("Verification status:", verification_status)
