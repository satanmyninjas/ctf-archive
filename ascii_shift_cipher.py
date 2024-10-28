# Cipher text
cipher_text = "x$ra}yL}E0#%`b0qFE0cfN"

# Function to decrypt by shifting characters back by 47 positions, with wrapping for printable ASCII range
def decrypt_message(cipher_text, shift):
    decrypted_message = ''
    for char in cipher_text:
        # Shift character back by the specified shift amount (47), wrapping within 32-126 ASCII range
        new_ascii = ord(char) - shift
        if new_ascii < 32:
            new_ascii += 95  # Wrap around to stay within printable ASCII range (32 to 126)
        decrypted_message += chr(new_ascii)
    return decrypted_message

# Decrypt the cipher text
shift = 47
decrypted_message = decrypt_message(cipher_text, shift)

print("Decrypted message:", decrypted_message)
