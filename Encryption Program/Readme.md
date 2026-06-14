Substitution Cipher Encryption Program

Overview

This Python program implements a simple Substitution Cipher encryption and decryption system.

The program creates a randomized mapping between characters and their encrypted equivalents. Each character in the original message is replaced with another character based on this mapping. The same key is then used to decrypt the message back to its original form.

⸻

Features

* Randomly generates an encryption key each time the program runs.
* Encrypts user-provided text.
* Decrypts encrypted text back to the original message.
* Supports:
    * Uppercase letters (A-Z)
    * Lowercase letters (a-z)
    * Numbers (0-9)
    * Punctuation symbols
    * Spaces

⸻

How It Works

1. Character Set Creation

The program creates a list containing:

* Space character
* Punctuation symbols
* Digits
* Uppercase and lowercase letters

Example:

chars = " " + string.punctuation + string.digits + string.ascii_letters

2. Key Generation

A copy of the character list is created and shuffled randomly:

key = chars.copy()
random.shuffle(key)

This shuffled list acts as the encryption key.

3. Encryption

For each character in the plaintext:

1. Find its position in chars.
2. Replace it with the character at the same position in key.

Example:

index = chars.index(letter)
cipher_text += key[index]

4. Decryption

For each character in the encrypted text:

1. Find its position in key.
2. Replace it with the character at the same position in chars.

Example:

index = key.index(letter)
plain_text += chars[index]

⸻

Example

Input

Enter message to encrypt: Hello World

Output

Original Text: Hello World
Encrypted Message: X7mmA@wArmQ

Decryption

Enter message to decrypt: X7mmA@wArmQ

Output

Encrypted Message: X7mmA@wArmQ
Original Text: Hello World

⸻

Requirements

* Python 3.x

Modules used:

import random
import string

Both modules are included in Python’s standard library.

⸻

Limitations

* The encryption key changes every time the program runs.
* Messages encrypted in one session cannot be decrypted in another session unless the same key is saved.
* This is an educational project and is not secure for real-world cryptography.

⸻

Future Improvements

* Save and load encryption keys from a file.
* Add support for key-based encryption.
* Create a graphical user interface (GUI).
* Encrypt and decrypt text files.
* Generate multiple encryption schemes.

⸻

Author

Created as a Python learning project to understand:

* Lists
* String manipulation
* Randomization
* Encryption concepts
* Character mapping
* Loops and indexing