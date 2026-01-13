# File Encryptor

This project was created as a **learning exercise** to better understand how file encryption works in practice.  
It focuses on cryptography basics, file I/O, and secure programming concepts using Python.

The goal of this project is **education**, not real-world deployment.

---

## Why I Built This

I built this project to learn:

- How AES encryption works at a practical level
- How passwords are turned into encryption keys
- Why salts and IVs are important
- What happens when encryption is used incorrectly
- Why losing an encryption password means permanent data loss

This project helped me understand both the **power and risks** of encryption.

---

## Important Disclaimer

> **This project is for educational and personal learning purposes only.**

It is not intended to be used on files you do not own or have permission to access.  
It should not be used as malware, ransomware, or for any malicious activity.

The program requires user interaction and only encrypts files that the user explicitly selects.

---

## What This Project Demonstrates

- File encryption and decryption using AES-256
- Password-based key derivation with PBKDF2
- Secure file handling using binary I/O
- Why strong passwords are necessary
- How encryption can permanently lock data if misused

---

## Features

- Encrypt and decrypt individual files
- Recursively encrypt and decrypt directories (for learning purposes)
- Uses AES-256-CBC with PBKDF2 (200,000 iterations)
- Enforces strong password rules
- Processes files in place to show real consequences of encryption
- Displays progress and basic error messages
- Prevents accidental re-encryption

---

## Requirements

- Python 3.7 or newer
- PyCryptodome

```bash
pip install pycryptodome
```
---
## How to Run
```bash
python main.py
```
You'll be prompted with a simple menu:
```
1. Encrypt a file
2. Decrypt a file
3. Encrypt a directory
4. Decrypt a directory
5. Exit
```
WARNING: Only encrypt files you are comfortable testing on.
---
## Password Rules
Password must:
- Be at least 8 characters long
- Include uppercase and lowercase letters
- Include a number
- Include a special character
---
## How the Encryption Works
### Encryption
1. The password is checked for strength
2. PBKDF2 is used to derive a 256-bit key
3. A random salt and IV are generated
4. The file is encrypted using AES-256-CBC
5. The file is renamed with a ```.encrypted``` extension
File layout:
```[salt][iv][encrypted data]```
### Decryption
1. The program checks that the file is encrypted
2. Salt and IV are extracted from the file
3. The key is recreated using the password
4. The file is decrypted and restored
---
## Project Structure
```bash
file-encryptor/
├── main.py        # User interface / menu
├── encryptor.py  # Encryption logic
├── decryptor.py  # Decryption logic
├── key_utils.py  # Password checking and key generation
└── README.md
```
---
## Things I Learned
- Encryption is not **forgiving** — losing a password means losing the data
- Encryption can be destructive if backups aren’t kept
- There is no “undo” button in real cryptography
---
## Warnings
- Always test on copies of files
- Back up important data before encrypting
- Do not forget your password
- Corrupted encrypted files cannot be recovered
