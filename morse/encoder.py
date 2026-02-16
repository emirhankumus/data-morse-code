"""
This module provides functions to encode text into Morse code.

Functions:
- encode(text): Encodes a given text into Morse code, separating words with a pipe (|) and
  letters with a space.
- encode_word(word): Encodes a single word into Morse code, separating letters with a space.
"""

from morse.mapping import MORSE

def encode_word(word: str) -> str:
    """
    Encodes a single word into Morse code.
    Letters are separated by a space.
    """
    # 1. Kelimeyi büyük harfe çevir
    # 2. Karakter karakter gez, eğer MORSE sözlüğünde varsa karşılığını al
    # 3. Aralarına bir boşluk koyarak birleştir
    encoded_chars = [MORSE[char] for char in word.upper() if char in MORSE]
    return " ".join(encoded_chars)


def encode(text: str) -> str:
    """
    Encodes the given text into Morse code.
    Words are separated by a pipe (|) and letters by a space.
    """
    # 1. Metni boşluklara göre kelimelere böl
    # 2. Her kelimeyi encode_word fonksiyonuna gönder
    # 3. Aralarına '|' (pipe) koyarak birleştir
    words = text.split()
    encoded_words = [encode_word(word) for word in words]
    return "|".join(encoded_words)


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_WORD = "abc"
    ENCODED_WORD = encode_word(EXAMPLE_WORD)
    print(f"Encoded word '{EXAMPLE_WORD}' to Morse code: '{ENCODED_WORD}'")

    # Example usage for a sentence
    EXAMPLE_TEXT = "abc ABC"
    ENCODED_TEXT = encode(EXAMPLE_TEXT)
    print(f"Encoded '{EXAMPLE_TEXT}' to Morse code: '{ENCODED_TEXT}'")
