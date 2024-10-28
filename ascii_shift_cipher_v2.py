phrase = "x$ra}yL}E0#%`b0qFE0cfN"

for shift in range(1, 51):
    result = ""
    for character in phrase:
        if 'A' <= character <= 'Z':  # Uppercase letters
            shifted_value = (ord(character) - ord('A') + shift) % 26 + ord('A')
            result += chr(shifted_value)
        elif 'a' <= character <= 'z':  # Lowercase letters
            shifted_value = (ord(character) - ord('a') + shift) % 26 + ord('a')
            result += chr(shifted_value)
        else:
            # For non-alphabet characters, keep them unchanged
            result += character
    
    print(f"Shift {shift}: {result}")
