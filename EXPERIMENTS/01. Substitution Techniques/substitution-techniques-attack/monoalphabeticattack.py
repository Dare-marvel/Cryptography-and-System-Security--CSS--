from collections import Counter
from itertools import islice

class MonoalphabeticAttack:
    # English letter frequencies (relative order of most common letters in the English language)
    ENGLISH_FREQUENCY_ORDER = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
    ]

    @staticmethod
    def get_frequency_map(text):
        # Perform frequency analysis on the ciphertext
        return Counter(filter(str.isalpha, text))

    @staticmethod
    def get_substitution_maps(freq_map):
        # Sort characters by frequency (most frequent first)
        sorted_freq_list = [item[0] for item in freq_map.most_common()]

        substitution_maps = []

        for i in range(100):  # Try up to 100 different frequency orders
            substitution_map = {}
            for j, cipher_char in enumerate(sorted_freq_list):
                plain_char = MonoalphabeticAttack.ENGLISH_FREQUENCY_ORDER[(j + i) % len(MonoalphabeticAttack.ENGLISH_FREQUENCY_ORDER)]
                substitution_map[cipher_char] = plain_char

            substitution_maps.append(substitution_map)

        return substitution_maps

    @staticmethod
    def decrypt_with_substitution_map(cipher_text, substitution_map):
        # Decrypt the ciphertext using the substitution map
        return ''.join(substitution_map.get(c, c) for c in cipher_text)

    @staticmethod
    def main():
        cipher_text = "hxlxw qxly xsz lqtzl" 

        # Perform frequency analysis
        freq_map = MonoalphabeticAttack.get_frequency_map(cipher_text.replace(" ", ""))

        # Generate multiple substitution maps based on frequency analysis
        substitution_maps = MonoalphabeticAttack.get_substitution_maps(freq_map)

        print("Possible plaintext combinations:")
        for i, substitution_map in enumerate(substitution_maps, 1):
            decrypted_text = MonoalphabeticAttack.decrypt_with_substitution_map(cipher_text, substitution_map)
            print(f"{i}. {decrypted_text}")

if __name__ == "__main__":
    MonoalphabeticAttack.main()
