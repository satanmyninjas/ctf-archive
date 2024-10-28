from itertools import cycle
import string

# Cipher text
cipher_text = "VWY2{Vicghw_zyorg}"

# Alphabet and allowed characters
alphabet = string.ascii_letters
allowed_chars = string.ascii_letters + "0123456789{}_"

# Function to decrypt Vigenère given a cipher and key
def decrypt_vigenere(cipher_text, key):
    decrypted_text = []
    key_cycle = cycle(key)
    for char in cipher_text:
        if char in alphabet:
            shift = ord(next(key_cycle)) - ord('A')
            if 'A' <= char <= 'Z':
                decrypted_text.append(chr((ord(char) - ord('A') - shift) % 26 + ord('A')))
            elif 'a' <= char <= 'z':
                decrypted_text.append(chr((ord(char) - ord('a') - shift) % 26 + ord('a')))
        else:
            decrypted_text.append(char)  # Non-alphabet characters remain unchanged
    return ''.join(decrypted_text)

# Function to test all keys up to a given length
def brute_force_vigenere(cipher_text, max_key_length=6):
    for key_length in range(1, max_key_length + 1):
        # Generate all possible keys of the current length
        for key in itertools.product(string.ascii_uppercase, repeat=key_length):
            key = ''.join(key)
            decrypted_message = decrypt_vigenere(cipher_text, key)
            # Display only plausible messages
            if all(c in allowed_chars for c in decrypted_message):
                print(f"Key: {key} -> Decrypted Message: {decrypted_message}")

# Test decryption with key lengths up to 6
import itertools
brute_force_vigenere(cipher_text, max_key_length=6)
