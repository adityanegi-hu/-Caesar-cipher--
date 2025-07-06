# 🔐 Caesar Cipher Implementation

<div align="center">

![Caesar Cipher](https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif)

*A simple yet powerful implementation of the classic Caesar cipher in Java*

[![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=java&logoColor=white)](https://www.java.com/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-green.svg?style=for-the-badge)]()

</div>

This is a Java implementation of the Caesar cipher, a simple substitution cipher where each letter in the plaintext is shifted a certain number of positions down or up the alphabet.

## ✨ Features

<div align="center">

![Encryption Demo](https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif)

</div>

- 🔒 **Encryption**: Shift letters forward in the alphabet by a specified number
- 🔓 **Decryption**: Shift letters backward in the alphabet by the same number
- 📝 **Case Preservation**: Maintains the original case of letters (uppercase/lowercase)
- 🎯 **Non-letter Characters**: Preserves spaces, numbers, and special characters unchanged
- 💻 **Interactive Input**: Command-line interface for user input
- ⚡ **Fast Performance**: Efficient string manipulation with StringBuilder

## 🧠 How It Works

<div align="center">

![Algorithm Visualization](https://media.giphy.com/media/3o7TKDEqHSmQ8n8rKw/giphy.gif)

</div>

The Caesar cipher works by:
1. 🔤 Taking each letter in the input text
2. 📊 Finding its position in the alphabet (A=0, B=1, ..., Z=25)
3. ➕ Adding the shift value to that position
4. 🔄 Taking the result modulo 26 to wrap around the alphabet
5. 🔤 Converting back to a character

### 📋 Example
| Letter | Position | + Shift | Mod 26 | Result |
|--------|----------|---------|--------|--------|
| H | 7 | 7 + 3 = 10 | 10 | K |
| E | 4 | 4 + 3 = 7 | 7 | H |
| L | 11 | 11 + 3 = 14 | 14 | O |
| L | 11 | 11 + 3 = 14 | 14 | O |
| O | 14 | 14 + 3 = 17 | 17 | R |

**Input:** "HELLO" with shift 3  
**Result:** "KHOOR"

## 🚀 Usage

<div align="center">

![Terminal Demo](https://media.giphy.com/media/3o7TKDEqHSmQ8n8rKw/giphy.gif)

</div>

### 🔨 Compilation
```bash
javac Cipher.java
```

### ▶️ Running
```bash
java Cipher
```

### 💡 Example Session
```bash
Enter text to encrypt: Hello World!
Enter shift key (0-25): 3
Encrypted text: Khoor Zruog!
Decrypted text: Hello World!
```

## 📁 Code Structure

<div align="center">

![Code Structure](https://media.giphy.com/media/3o7TKDEqHSmQ8n8rKw/giphy.gif)

</div>

| Method | Description | Parameters | Return |
|--------|-------------|------------|--------|
| `encrypt(String text, int shift)` | 🔒 Encrypts the given text using the specified shift | `text`: Input string, `shift`: Shift value (0-25) | `String`: Encrypted text |
| `decrypt(String text, int shift)` | 🔓 Decrypts the given text using the specified shift | `text`: Encrypted string, `shift`: Shift value (0-25) | `String`: Decrypted text |
| `main(String[] args)` | 🎮 Main method that handles user input and demonstrates the cipher | `args`: Command line arguments | `void` |

## ⚠️ Security Note

<div align="center">

![Security Warning](https://media.giphy.com/media/3o7TKDEqHSmQ8n8rKw/giphy.gif)

</div>

🚨 **The Caesar cipher is a very basic encryption method and should not be used for securing sensitive information.** It can be easily broken by:

- 🔍 **Brute force** (trying all 25 possible shifts)
- 📊 **Frequency analysis** (analyzing letter frequency patterns)
- 🎯 **Known plaintext attacks** (using known text-cipher pairs)

> ⚠️ **This implementation is intended for educational purposes only.**

## 📋 Requirements

- ☕ **Java 8 or higher**
- 📦 **No external dependencies required**

---

<div align="center">

### 🎉 **Ready to encrypt? Let's get started!**

[![Get Started](https://img.shields.io/badge/Get%20Started-Now-green?style=for-the-badge&logo=java)](https://github.com/yourusername/caesar-cipher)

*Made with ❤️ for educational purposes*

</div> 