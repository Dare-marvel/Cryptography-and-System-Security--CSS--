from collections import Counter
from itertools import islice

class SubstitutionCipherCracker:
    # English letter frequencies (relative order of most common letters in the English language)
    FREQUENCY_ORDER_ENGLISH = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
    ]

    @staticmethod
    def analyze_frequency(text):
        # Perform frequency analysis on the ciphertext
        return Counter(filter(str.isalpha, text))

    @staticmethod
    def generate_substitution_maps(freq_map):
        # Sort characters by frequency (most frequent first)
        sorted_chars_by_freq = [item[0] for item in freq_map.most_common()]

        substitution_maps = []

        for offset in range(100):  # Try up to 100 different frequency orders
            substitution_map = {}
            for index, cipher_char in enumerate(sorted_chars_by_freq):
                plain_char = SubstitutionCipherCracker.FREQUENCY_ORDER_ENGLISH[(index + offset) % len(SubstitutionCipherCracker.FREQUENCY_ORDER_ENGLISH)]
                substitution_map[cipher_char] = plain_char

            substitution_maps.append(substitution_map)

        return substitution_maps

    @staticmethod
    def decrypt_using_map(cipher_text, substitution_map):
        # Decrypt the ciphertext using the substitution map
        return ''.join(substitution_map.get(char, char) for char in cipher_text)

    @staticmethod
    def main():
        cipher_text = "hxlxw qxly xsz lqtzl" 

        # Perform frequency analysis
        frequency_map = SubstitutionCipherCracker.analyze_frequency(cipher_text.replace(" ", ""))

        # Generate multiple substitution maps based on frequency analysis
        substitution_maps = SubstitutionCipherCracker.generate_substitution_maps(frequency_map)

        print("Possible plaintext combinations:")
        for i, substitution_map in enumerate(substitution_maps, 1):
            decrypted_text = SubstitutionCipherCracker.decrypt_using_map(cipher_text, substitution_map)
            print(f"{i}. {decrypted_text}")

if __name__ == "__main__":
    SubstitutionCipherCracker.main()
