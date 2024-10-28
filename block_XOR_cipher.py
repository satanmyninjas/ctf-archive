import argparse
import os

# Define the 64-bit key as an integer
KEY = 0xFF4FF4F00F444004

def pad_to_64_bits(block):
    """Pad the block to 64 bits (8 bytes) if necessary by adding 0s."""
    block_int = int.from_bytes(block.encode(), 'big')
    return block_int << (8 - len(block)) * 8 if len(block) < 8 else block_int

def encrypt_block(block):
    """Encrypt a 64-bit block by XORing it with the key."""
    padded_block = pad_to_64_bits(block)
    encrypted_block = padded_block ^ KEY
    return encrypted_block

def encrypt_message(message):
    """Encrypt an entire message block-by-block."""
    encrypted_message = []
    for i in range(0, len(message), 8):
        block = message[i:i+8]
        encrypted_block = encrypt_block(block)
        encrypted_message.append(encrypted_block)
    return encrypted_message

def display_encrypted_message(encrypted_blocks):
    """Display the encrypted message as a series of hex values."""
    print("[DONE] - Encrypted message:")
    for block in encrypted_blocks:
        print(hex(block))

def save_encrypted_message_to_file(encrypted_blocks, output_file):
    """Save the encrypted message to a text file."""
    with open(output_file, 'w') as f:
        for block in encrypted_blocks:
            f.write(f"{hex(block)}\n")
    print(f"[DONE] - Encrypted message saved to '{output_file}'")

def main():
    parser = argparse.ArgumentParser(
        description="Encrypt a message using a custom block cipher with a fixed key."
    )
    parser.add_argument(
        "-m", "--message", 
        type=str, 
        help="The message you want to encrypt. Each 64-bit block will be XORed with a fixed key. Use double-quotes for your message."
    )
    parser.add_argument(
        "-f", "--file", 
        type=str, 
        help="Path to a .txt file containing the message to encrypt. Each 64-bit block will be XORed with a fixed key."
    )
    parser.add_argument(
        "-o", "--output", 
        type=str, 
        help="Optional output file to save the encrypted message."
    )

    args = parser.parse_args()

    # Check for input method
    if args.message:
        input_message = args.message
    elif args.file:
        # Ensure the file exists
        if not os.path.isfile(args.file):
            print(f"Error: File '{args.file}' does not exist.")
            return
        # Read the file content
        with open(args.file, 'r', encoding='utf-8') as file:
            input_message = file.read()
    else:
        print("[ERROR!] No message provided, or the file/message is empty. Use -m/--message or -f/--file to specify input.")
        return

    # Encrypt the input message
    encrypted_blocks = encrypt_message(input_message)

    # Output to console or file
    if args.output:
        save_encrypted_message_to_file(encrypted_blocks, args.output)
    else:
        display_encrypted_message(encrypted_blocks)

if __name__ == "__main__":
    main()
