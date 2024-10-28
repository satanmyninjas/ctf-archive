# Given values
a = 5
b = 8
m = 26
a_inv = 21  # Modular inverse of 5 under 26

# Cipher text
cipher_text = "WUS2{Qizru_1u_hev_wuvz_wz?}"

# Function to decrypt each character
def decrypt_char(char):
    if 'A' <= char <= 'Z':  # Uppercase letters
        y = ord(char) - ord('A')
        x = (a_inv * (y - b)) % m
        return chr(x + ord('A'))
    elif 'a' <= char <= 'z':  # Lowercase letters
        y = ord(char) - ord('a')
        x = (a_inv * (y - b)) % m
        return chr(x + ord('a'))
    else:
        return char  # Non-alphabet characters are unchanged

# Decrypt the entire message
decrypted_message = ''.join(decrypt_char(c) for c in cipher_text)

print("Decrypted message:", decrypted_message)
