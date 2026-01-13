# File Encryptor

A secure command-line file and directory encryption tool using AES-256-CBC encryption with PBKDF2 key derivation.

## Features

- **File Encryption/Decryption** - Encrypt and decrypt individual files
- **Directory Encryption/Decryption** - Recursively encrypt/decrypt entire directories
- **Strong Encryption** - Uses AES-256-CBC with PBKDF2 (200,000 iterations)
- **Password Strength Validation** - Enforces strong password requirements
- **In-place Processing** - Files are encrypted/decrypted in place to save disk space
- **Progress Tracking** - Shows real-time progress and completion statistics
- **Error Handling** - Comprehensive error checking and user-friendly error messages
- **Safety Checks** - Prevents re-encryption and validates file integrity

## Requirements

- Python 3.7+
- PyCryptodome library

## Installation

1. Clone or download this repository
2. Install required dependencies:

```bash
pip install pycryptodome
```

## Usage

Run the program:

```bash
python main.py
```

### Menu Options

```
1. Encrypt a file
2. Decrypt a file
3. Encrypt a directory
4. Decrypt a directory
5. Exit
```

### Password Requirements

Passwords must meet the following criteria:
- Minimum 8 characters
- At least one uppercase letter (A-Z)
- At least one lowercase letter (a-z)
- At least one number (0-9)
- At least one special character (!@#$%^&*(),.?":{}|<>)

## Examples

### Encrypting a Single File

```
Enter your choice (1-5): 1
File path: document.pdf
Enter password: MySecure123!
✓ document.pdf successfully encrypted!
```

The file will be renamed to `document.pdf.encrypted`

### Decrypting a Single File

```
Enter your choice (1-5): 2
File path: document.pdf.encrypted
Enter password: MySecure123!
✓ document.pdf.encrypted successfully decrypted!
```

The file will be renamed back to `document.pdf`

### Encrypting a Directory

```
Enter your choice (1-5): 3
Directory path: C:\MyDocuments
Enter password: MySecure123!
Encrypt ALL files in 'C:\MyDocuments' and subdirectories? (yes/no): yes

Encrypting: C:\MyDocuments\file1.txt
✓ C:\MyDocuments\file1.txt successfully encrypted!
Encrypting: C:\MyDocuments\subfolder\file2.pdf
✓ C:\MyDocuments\subfolder\file2.pdf successfully encrypted!

=== Encryption Complete ===
Files encrypted: 2
Files skipped: 0
Files failed: 0
```

### Decrypting a Directory

```
Enter your choice (1-5): 4
Directory path: C:\MyDocuments
Enter password: MySecure123!
Decrypt ALL .encrypted files in 'C:\MyDocuments' and subdirectories? (yes/no): yes

Decrypting: C:\MyDocuments\file1.txt.encrypted
✓ C:\MyDocuments\file1.txt.encrypted successfully decrypted!
Decrypting: C:\MyDocuments\subfolder\file2.pdf.encrypted
✓ C:\MyDocuments\subfolder\file2.pdf.encrypted successfully decrypted!

=== Decryption Complete ===
Files decrypted: 2
Files skipped: 0
Files failed: 0
```

## How It Works

### Encryption Process

1. **Password Validation** - Checks password strength requirements
2. **Key Derivation** - Uses PBKDF2 with 200,000 iterations and SHA-256 to derive a 256-bit key from your password
3. **Salt Generation** - Creates a random 16-byte salt for each file
4. **IV Generation** - Creates a random 16-byte initialization vector
5. **AES Encryption** - Encrypts file content using AES-256-CBC
6. **File Structure** - Saves: `[16-byte salt][16-byte IV][encrypted data]`
7. **Renaming** - Adds `.encrypted` extension to the file

### Decryption Process

1. **File Validation** - Checks for `.encrypted` extension
2. **Data Extraction** - Extracts salt, IV, and ciphertext from file
3. **Key Derivation** - Recreates the encryption key using the password and extracted salt
4. **AES Decryption** - Decrypts the data using AES-256-CBC
5. **File Restoration** - Overwrites file with decrypted data and removes `.encrypted` extension

## File Structure

```
file-encryptor/
├── main.py                    # Main program interface
├── encryptor.py              # File and directory encryption functions
├── decryptor.py              # File and directory decryption functions
├── key_utils.py              # Password validation and key generation
└── README.md                 # This file
```

## Security Notes

### ✓ Security Features

- **AES-256-CBC** - Industry-standard encryption algorithm
- **PBKDF2** - Secure password-based key derivation (200,000 iterations)
- **Random Salt** - Unique salt for each file prevents rainbow table attacks
- **Random IV** - Unique initialization vector for each file
- **Password Strength** - Enforced strong password requirements

### ⚠️ Important Warnings

- **Password Loss** - If you lose your password, your files **CANNOT** be recovered
- **Backup** - Always keep backups of important files before encryption
- **Password Storage** - Do not store passwords in plain text
- **File Corruption** - Corrupted encrypted files cannot be decrypted
- **Original Files** - Original files are overwritten during encryption (no copies kept)

## Troubleshooting

### "Error: Permission denied"
- Close any programs that might be using the file
- Run the program with administrator/sudo privileges
- Check file permissions

### "Error: Decryption failed. Wrong password or corrupted file."
- Verify you're using the correct password
- Check if the file is corrupted
- Ensure the file was encrypted with this tool

### "Error: Input file must have .encrypted extension"
- Make sure you're trying to decrypt an encrypted file
- Verify the file has the `.encrypted` extension

### Files are being skipped
- Encrypted files (`.encrypted`) are automatically skipped during encryption
- Non-encrypted files are skipped during decryption
- This is normal behavior to prevent errors

## License

This project is provided as-is for educational and personal use.

## Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

## Disclaimer

This tool is provided for legitimate file encryption purposes only. Users are responsible for:
- Remembering their passwords
- Backing up important files
- Using the tool responsibly and legally
- Understanding the risks of encryption

The authors are not responsible for any data loss, corruption, or misuse of this tool.

---

**Version:** 1.0  
**Last Updated:** January 2026