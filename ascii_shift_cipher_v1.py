phrase = "x$ra}yL}E0#%`b0qFE0cfN"
shift = 47
result = ""

for character in phrase:
    x = ord(character)

    if character == ' ':
        result += ' '
    else:
        shifted_value = (x + shift - 32) % 95 + 32
        result += chr(shifted_value)

print(result)
