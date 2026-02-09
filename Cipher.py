# This code implements a Caesar cipher using Python. It includes encryption and decryption functions
# that shift characters by a specified amount, preserving non-letter characters.

def encrypt(text, shift):
    """
    Encrypts text using Caesar cipher with the given shift value.
    
    Args:
        text (str): The text to encrypt
        shift (int): The number of positions to shift each character
    
    Returns:
        str: The encrypted text
    """
    result = []
    
    for character in text:
        if character.isalpha():
            base = ord('a') if character.islower() else ord('A')
            shifted = chr((ord(character) - base + shift) % 26 + base)
            result.append(shifted)
        else:
            result.append(character)
    
    return ''.join(result)

def decrypt(text, shift):
    """
    Decrypts text using Caesar cipher with the given shift value.
    
    Args:
        text (str): The text to decrypt
        shift (int): The number of positions the text was shifted by
    
    Returns:
        str: The decrypted text
    """
    return encrypt(text, 26 - shift)

def main():
    """Main function to run the cipher program."""
    print("Enter text to encrypt: ", end="")
    input_text = input()
    
    print("Enter shift key (0-25): ", end="")
    shift_key = int(input())
    
    encrypted = encrypt(input_text, shift_key)
    print(f"Encrypted text: {encrypted}")
    
    decrypted = decrypt(encrypted, shift_key)
    print(f"Decrypted text: {decrypted}")

if __name__ == "__main__":
    main()
