from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding as crypt_padding
import hashlib
from sha512 import sha512
import os


class AESCipher:
    """Class to handle AES encryption and decryption."""
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        """Encrypts data using AES-CBC with PKCS7 padding."""
        iv = os.urandom(16)  # Generate a random 16-byte IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Apply PKCS7 padding
        padder = crypt_padding.PKCS7(algorithms.AES.block_size).padder()
        padded_data = padder.update(data.encode()) + padder.finalize()

        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return iv + ciphertext

    def decrypt(self, ciphertext):
        """Decrypts AES-CBC encrypted data."""
        iv = ciphertext[:16]  # Extract IV
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()

        padded_plaintext = decryptor.update(ciphertext[16:]) + decryptor.finalize()

        # Remove PKCS7 padding
        unpadder = crypt_padding.PKCS7(algorithms.AES.block_size).unpadder()
        plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()

        return plaintext.decode()


class HashManager:
    """Handles hashing of messages."""
    @staticmethod
    def hash_message(message):
        """Generates SHA-512 hash of the input message."""
        return sha512(message)


class MessageHandler:
    """Handles message encryption, decryption, and verification."""
    def __init__(self, key):
        self.cipher = AESCipher(key)

    def encrypt_hash_of_message(self, message):
        """Generates a hash of the message and encrypts it."""
        message_hash = HashManager.hash_message(message)
        encrypted_hash = self.cipher.encrypt(message_hash)
        return encrypted_hash

    @staticmethod
    def concatenate_message_and_encrypted_hash(message, encrypted_hash):
        """Concatenates the original message and the encrypted hash."""
        return message.encode() + encrypted_hash

    @staticmethod
    def extract_message_and_encrypted_hash(concatenated_data):
        """Extracts the original message and the encrypted hash from concatenated data."""
        message = concatenated_data[:-160].decode()
        encrypted_hash = concatenated_data[-160:]
        return message, encrypted_hash

    def decrypt_and_verify(self, concatenated_data):
        """Decrypts the encrypted hash and verifies the message integrity."""
        message, encrypted_hash = self.extract_message_and_encrypted_hash(concatenated_data)
        decrypted_hash = self.cipher.decrypt(encrypted_hash)

        message_hash = HashManager.hash_message(message)

        # Compare the decrypted hash with the computed message hash
        return decrypted_hash == message_hash


def generate_aes_key(passphrase):
    """Generates a 256-bit AES key from a passphrase using SHA-256."""
    return hashlib.sha256(passphrase).digest()


if __name__ == "__main__":
    message = "Hello, world!"

    # Generate AES key from a passphrase
    aes_key = generate_aes_key(b'secret_key')

    # Initialize the MessageHandler with the AES key
    handler = MessageHandler(aes_key)

    # Encrypt the hash of the message
    encrypted_hash = handler.encrypt_hash_of_message(message)

    # Concatenate the original message and the encrypted hash
    concatenated_data = handler.concatenate_message_and_encrypted_hash(message, encrypted_hash)

    # Decrypt the hash and verify the message integrity
    verification_status = handler.decrypt_and_verify(concatenated_data)

    # Output verification result
    if verification_status:
        print("Message integrity verified!")
    else:
        print("Message integrity verification failed!")
