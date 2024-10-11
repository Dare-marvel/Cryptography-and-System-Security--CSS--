from sha512 import sha512

class MessageHasher:
    """Handles the hashing of messages with a seed."""
    @staticmethod
    def hash_message(message, seed):
        """Generates a SHA-512 hash of the message combined with a seed."""
        message_seed = message + seed
        return sha512(message_seed)


class MessageSender:
    """Handles the sending of messages with appended hashes."""
    def __init__(self, seed):
        self.seed = seed

    def send(self, message):
        """Appends a hash to the message and returns the concatenated result."""
        hash_message = MessageHasher.hash_message(message, self.seed)
        print("Sending message:", message)
        print("Hash:", hash_message)
        return message + hash_message


class MessageReceiver:
    """Handles the reception and verification of messages."""
    def __init__(self, seed):
        self.seed = seed

    def receive(self, message_recv):
        """Extracts the message and hash, verifies the hash, and checks for message integrity."""
        hash_message = message_recv[-128:]  # Extract the last 128 characters as the hash
        message = message_recv[:-128]       # The remaining part is the message

        expected_hash_message = MessageHasher.hash_message(message, self.seed)

        if self.verify_hash(expected_hash_message, hash_message):
            print(f"Message hashes matching\nMessage: {message}\nHash: {hash_message}")
            return message
        else:
            print("Message hashes not matching! Message corrupted.")
            return None

    @staticmethod
    def verify_hash(expected_hash, received_hash):
        """Checks if the expected hash matches the received hash."""
        return expected_hash == received_hash


def simulate_message_transfer():
    seed = "thisisasecret"

    # Case 1: Correct message transfer
    print("Case 1")
    sender = MessageSender(seed)
    receiver = MessageReceiver(seed)

    sent_message = sender.send("Python")
    received_message = receiver.receive(sent_message)
    print(f"Received message: {received_message}\n")

    # Case 2: Corrupted message transfer
    print("Case 2")
    sent_message = sender.send("csslab")
    corrupted_message = sent_message[:34] + "3a" + sent_message[36:]  # Tampering with the message
    received_message = receiver.receive(corrupted_message)
    assert received_message is None  # Message should be corrupted


if __name__ == "__main__":
    simulate_message_transfer()
