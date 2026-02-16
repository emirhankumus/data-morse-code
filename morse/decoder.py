"""
This module provides functions to decode Morse code back into text.

Functions:
- decode(morse_text): Decodes Morse code into text, handling words separated by pipes (|).
"""

from morse.mapping import MORSE

# Mühendislik Dokunuşu: Sözlüğü programatik olarak ters çeviriyoruz.
DECODE_DICT = {v: k for k, v in MORSE.items()}

def decode_word(morse_word):
    """
    Decodes a single Morse word (signals separated by spaces) into text.
    """
    # Sinyalleri boşluklardan ayır
    signals = morse_word.split(' ')
    # Her sinyali sözlükten karşılığını bul (varsa) ve birleştir
    decoded_chars = [DECODE_DICT[sig] for sig in signals if sig in DECODE_DICT]
    return "".join(decoded_chars)

def decode(morse_text):
    """
    Decodes the given Morse code into text.
    Words are separated by a pipe (|) and letters by a space.
    """
    if not morse_text:
        return ""
        
    # Morse metnini pipe (|) işaretine göre kelimelere böl
    morse_words = morse_text.split('|')
    # Her bir kelimeyi decode_word fonksiyonu ile çöz
    decoded_words = [decode_word(word) for word in morse_words]
    
    # Kelimeleri aralarında birer boşluk olacak şekilde birleştir
    return " ".join(decoded_words)


if __name__ == "__main__":
    # Example usage for one word
    EXAMPLE_MORSE_WORD = ".... .. ---"
    DECODED_WORD = decode_word(EXAMPLE_MORSE_WORD)
    print(f"Decoded Morse word '{EXAMPLE_MORSE_WORD}' to text: '{DECODED_WORD}'")

    # Example usage for one sentence
    EXAMPLE_MORSE_TEXT = ".... ..|--. ..- -.-- ..."
    DECODED_TEXT = decode(EXAMPLE_MORSE_TEXT)
    print(f"Decoded Morse '{EXAMPLE_MORSE_TEXT}' to text: '{DECODED_TEXT}'")
