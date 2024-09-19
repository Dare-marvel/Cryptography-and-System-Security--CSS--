import socket
import sys
import random
import string

# Diffie-Hellman parameters
P = 23  # A prime number P
G = 5   # A primitive root modulo P

# Sender (Client) class
class Sender:
    def __init__(self, host='127.0.0.1', port=3333):
        self.host = host
        self.port = port
        self.shared_key = None
        self.private_key = None
        self.substitution_key = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.connect((self.host, self.port))
            print(f"Connected to receiver at {self.host}:{self.port}")
        except Exception as e:
            print(f"Failed to connect to receiver: {e}")
            sys.exit(1)

    def generate_key(self):
        # Generate private key and public key
        self.private_key = random.randint(1, P - 1)
        public_key = pow(G, self.private_key, P)
        self.socket.sendall(str(public_key).encode())
        
        # Receive receiver's public key
        receiver_public_key = int(self.socket.recv(1024).decode())
        self.shared_key = pow(receiver_public_key, self.private_key, P)
        print(f"Shared key is generated: {self.shared_key}")
        self.generate_substitution_key()

    def generate_substitution_key(self):
        # Create a substitution key based on the shared key
        random.seed(self.shared_key)  # Use shared key to seed the random number generator
        alphabet = list(string.ascii_lowercase)
        shuffled = alphabet[:]
        random.shuffle(shuffled)
        self.substitution_key = dict(zip(alphabet, shuffled))
        print(f"Substitution key: {self.substitution_key}")

    def encrypt_message(self, message):
        # Encrypt the message using the monoalphabetic substitution cipher
        encrypted_message = ''.join([self.substitution_key.get(char, char) for char in message.lower()])
        return encrypted_message

    def send_message(self):
        if not self.substitution_key:
            print("Error: Key has not been generated yet.")
            return

        message = input("Enter a message: ")
        encrypted_message = self.encrypt_message(message)
        self.socket.sendall(encrypted_message.encode())  # Send encrypted message
        print("Message sent successfully.")

    def run(self):
        while True:
            print("\n1. Generate Key using Diffie-Hellman")
            print("2. Send Message using Monoalphabetic Cipher")
            print("3. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                self.generate_key()
            elif choice == '2':
                self.send_message()
            elif choice == '3':
                print("Exiting...")
                self.socket.close()
                sys.exit(0)
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    sender = Sender()
    sender.run()

