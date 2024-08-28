from collections import Counter

class MonoalphabeticCipherCracker:
    """Cracks a substitution cipher by analyzing letter frequencies."""

    ENGLISH_FREQ_ORDER = [
        'e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'c', 'u', 'm', 'w', 'f', 'g', 'y', 'p', 'b', 'v', 'k', 'j', 'x', 'q', 'z'
    ]

    @staticmethod
    def analyze_freq(text):
        """Analyzes the frequency of letters in the text."""
        return Counter(filter(str.isalpha, text))

    @staticmethod
    def generate_substitution_maps(freq_map, iterations):
        """Generates substitution maps based on frequency analysis."""
        sorted_chars = [item[0] for item in freq_map.most_common()]
        maps = []

        for offset in range(iterations):
            map = {}
            for i, char in enumerate(sorted_chars):
                plain_char = MonoalphabeticCipherCracker.ENGLISH_FREQ_ORDER[(i + offset) % len(MonoalphabeticCipherCracker.ENGLISH_FREQ_ORDER)]
                map[char] = plain_char
            maps.append(map)

        return maps

    @staticmethod
    def decrypt(text, substitution_map):
        """Decrypts the text using the substitution map."""
        return ''.join(substitution_map.get(char, char) for char in text)

    @staticmethod
    def main():
        text = input("Enter the ciphertext: ")
        freq_map = MonoalphabeticCipherCracker.analyze_freq(text.replace(" ", ""))
        
        iterations = int(input("Enter iterations (offsets): "))
        maps = MonoalphabeticCipherCracker.generate_substitution_maps(freq_map, iterations)

        print("Possible plaintext combinations:")
        for i, map in enumerate(maps, 1):
            decrypted_text = MonoalphabeticCipherCracker.decrypt(text, map)
            print(f"{i}. {decrypted_text}")

if __name__ == "__main__":
    MonoalphabeticCipherCracker.main()