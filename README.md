# 🔐 Caesar Cipher

<div align="center">

![Caesar Cipher Demo](https://raw.githubusercontent.com/yourusername/caesar-cipher/main/demo.gif)

*A Python implementation of the ancient Caesar cipher encryption technique*

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</div>

## 📖 Overview

The Caesar cipher is one of the oldest and simplest encryption techniques, named after **Julius Caesar** who used it to protect his military messages. This implementation brings this historic cipher to modern Python with a clean, interactive interface.

> *"The shift that protected empires, now in your terminal!"* 🏛️

## ✨ Features

- 🔒 **Encrypt & Decrypt** - Full bidirectional cipher support
- 🎯 **Smart Shifting** - Handles any shift value (0-25)
- 📝 **Character Preservation** - Keeps spaces, punctuation, and numbers intact
- 🔤 **Case Sensitive** - Maintains uppercase and lowercase distinction
- 💻 **Interactive CLI** - User-friendly command-line interface
- 📦 **Modular Design** - Easy to import and use in your own projects

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/caesar-cipher.git

# Navigate to the directory
cd caesar-cipher

# Run the program
python caesar_cipher.py
```

### Usage

```bash
$ python caesar_cipher.py

Enter text to encrypt: Hello, World!
Enter shift key (0-25): 3
Encrypted text: Khoor, Zruog!
Decrypted text: Hello, World!
```

## 🎨 Visual Examples

### Encryption Process

```
Plain text:  HELLO WORLD
Shift by 3:  KHOOR ZRUOG
             ↓↓↓↓↓ ↓↓↓↓↓
             H→K E→H L→O L→O O→R
```

### ASCII Visualization

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
↓ ↓ ↓ ↓ ↓ (shift by 3)
D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
```

## 💡 Code Examples

### Basic Usage

```python
from caesar_cipher import encrypt, decrypt

# Encrypt a secret message
message = "Meet me at midnight"
encrypted = encrypt(message, 7)
print(f"🔒 Encrypted: {encrypted}")
# Output: 🔒 Encrypted: Tlla tl ha tpkupnoa

# Decrypt it back
decrypted = decrypt(encrypted, 7)
print(f"🔓 Decrypted: {decrypted}")
# Output: 🔓 Decrypted: Meet me at midnight
```

### Advanced: Brute Force Attack

```python
from caesar_cipher import decrypt

# Try all possible shifts to crack the cipher
encrypted_message = "Uryyb, Jbeyq!"

print("🔍 Attempting to crack the cipher...\n")
for shift in range(26):
    result = decrypt(encrypted_message, shift)
    print(f"Shift {shift:2d}: {result}")

# Output will show all 26 possible decryptions
# Including the correct one: "Hello, World!" at shift 13
```

### Fun: ROT13 Implementation

```python
from caesar_cipher import encrypt

# ROT13 is a special case of Caesar cipher (shift = 13)
def rot13(text):
    return encrypt(text, 13)

secret = "Secret Message"
encoded = rot13(secret)
decoded = rot13(encoded)  # ROT13 is its own inverse!

print(f"Original: {secret}")
print(f"Encoded:  {encoded}")
print(f"Decoded:  {decoded}")
```

## 🎮 Interactive Demo

Try these example messages:

| Original Text | Shift | Encrypted Result |
|--------------|-------|------------------|
| `HELLO` | 3 | `KHOOR` |
| `Python is awesome!` | 5 | `Udymts nx fbjxtrj!` |
| `ABC xyz 123` | 1 | `BCD yza 123` |
| `The quick brown fox` | 13 | `Gur dhvpx oebja sbk` |

## 📚 How It Works

### The Algorithm

1. **For each character** in the input text:
   - If it's a letter, shift it by the specified amount
   - Wrap around the alphabet (Z + 1 = A)
   - Preserve the original case (uppercase/lowercase)
   - Non-letters pass through unchanged

2. **Mathematical Formula**:
   ```
   Encryption: E(x) = (x + n) mod 26
   Decryption: D(x) = (x - n) mod 26
   ```

### Code Structure

```python
📁 caesar_cipher.py
   ├── 🔐 encrypt(text, shift)      # Main encryption function
   ├── 🔓 decrypt(text, shift)      # Main decryption function
   └── 🎮 main()                    # Interactive CLI interface
```

## 🎯 Use Cases

- 📖 **Educational** - Learn about basic cryptography
- 🎲 **Puzzles & Games** - Create encoded messages for fun
- 🧪 **Testing** - Practice cryptanalysis techniques
- 🏫 **Teaching** - Demonstrate encryption concepts

## ⚠️ Security Notice

> **Important:** The Caesar cipher is **NOT SECURE** for protecting sensitive information! 

- ❌ Vulnerable to frequency analysis
- ❌ Only 25 possible keys (easy to brute force)
- ❌ Pattern preservation makes it easy to crack
- ✅ Great for learning and educational purposes

For real security, use modern encryption like **AES** or **RSA**.

## 🤝 Contributing

Contributions are welcome! Here are some ideas:

- 🎨 Add a GUI interface
- 📊 Create frequency analysis tools
- 🌍 Support for non-English alphabets
- 🔧 Add command-line arguments
- 📝 Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🌟 Fun Facts

- 🏛️ Julius Caesar used a shift of 3 in his private correspondence
- 🔤 ROT13 (shift of 13) is still used in online forums to hide spoilers
- 📜 This cipher was considered unbreakable for centuries
- 🎖️ During WWII, more complex substitution ciphers evolved from this basic concept

---

<div align="center">

**Made with ❤️ for cryptography enthusiasts**

[⭐ Star this repo](https://github.com/yourusername/caesar-cipher) | [🐛 Report Bug](https://github.com/yourusername/caesar-cipher/issues) | [✨ Request Feature](https://github.com/yourusername/caesar-cipher/issues)

</div>
