import socket
import sys
import random
import string

# Diffie-Hellman parameters
P = 23  # A prime number P
G = 5   # A primitive root modulo P

# Receiver (Server) class
class Receiver:
    def __init__(self, host='127.0.0.1', port=3333):
        self.host = host
        self.port = port
        self.shared_key = None
        self.private_key = None
        self.substitution_key = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.host, self.port))
            self.socket.listen(1)
            print("Receiver is listening on port", self.port)
        except Exception as e:
            print(f"Failed to start receiver: {e}")
            sys.exit(1)

    def handle_connection(self, conn):
        try:
            # Diffie-Hellman Key Exchange
            print("Waiting to receive the client's public key...")
            client_public_key = int(conn.recv(1024).decode())
            print(f"Received client public key: {client_public_key}")
            self.private_key = random.randint(1, P - 1)
            public_key = pow(G, self.private_key, P)
            conn.sendall(str(public_key).encode())
            print(f"Sent own public key: {public_key}")

            self.shared_key = pow(client_public_key, self.private_key, P)
            print(f"Shared key generated: {self.shared_key}")
            self.generate_substitution_key()

            while True:
                # Receive encrypted message
                encrypted_message = conn.recv(4096).decode()  # Receive encrypted message
                if encrypted_message:
                    print(f"Received encrypted message: {encrypted_message}")
                    decrypted_message = self.decrypt_message(encrypted_message)
                    print(f"Decrypted message: {decrypted_message}")
                else:
                    print("No more messages. Closing connection.")
                    break
        except Exception as e:
            print(f"Error during communication: {e}")

    def generate_substitution_key(self):
        # Create a substitution key based on the shared key
        random.seed(self.shared_key)  # Use shared key to seed the random number generator
        alphabet = list(string.ascii_lowercase)
        shuffled = alphabet[:]
        random.shuffle(shuffled)
        self.substitution_key = dict(zip(shuffled, alphabet))  # Reverse mapping for decryption
        print(f"Substitution key: {self.substitution_key}")

    def decrypt_message(self, encrypted_message):
        # Decrypt the message using the monoalphabetic substitution cipher
        decrypted_message = ''.join([self.substitution_key.get(char, char) for char in encrypted_message])
        return decrypted_message

    def run(self):
        while True:
            print("Waiting for a connection...")
            conn, addr = self.socket.accept()
            print("Connected by", addr)
            self.handle_connection(conn)
            conn.close()
            print("Connection closed. Waiting for a new connection...")

if __name__ == "__main__":
    receiver = Receiver()
    receiver.run()

