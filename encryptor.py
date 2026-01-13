import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from key_utils import salt_key_generator
from Crypto.Random import get_random_bytes


def encrypt_file(input_file: str, password: str):
    """Encrypt a single file using AES-256-CBC encryption."""
    if not input_file or input_file.strip() == "":
        print("Error: File path cannot be empty.")
        return False

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return False

    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' is not a valid file.")
        return False

    if input_file.endswith(".encrypted"):
        print(f"Error: File '{input_file}' is already encrypted.")
        return False

    try:
        with open(input_file, 'rb') as file:
            data = file.read()

        salt, key = salt_key_generator(password)
        iv = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(data, AES.block_size))

        with open(input_file, 'wb') as file:
            file.write(salt + iv + ciphertext)

        os.rename(input_file, input_file + ".encrypted")
        print(f"✓ {input_file} successfully encrypted!")
        return True

    except PermissionError:
        print(f"Error: Permission denied to access '{input_file}'.")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return False


def encrypt_directory(directory_path: str, password: str):
    """Recursively encrypt all files in a directory and its subdirectories."""
    encrypted_count = 0
    skipped_count = 0
    failed_count = 0

    if not directory_path or directory_path.strip() == "":
        print("Error: Directory path cannot be empty.")
        return

    if not os.path.exists(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        return

    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' is not a valid directory.")
        return

    try:


        for root, dirs, files in os.walk(directory_path):
            for filename in files:
                file_path = os.path.join(root, filename)

                # Skip if it's a directory
                if os.path.isdir(file_path):
                    continue

                # Skip already encrypted files
                if file_path.endswith(".encrypted"):
                    print(f"⊗ Skipping already encrypted: {file_path}")
                    skipped_count += 1
                    continue

                print(f"Encrypting: {file_path}")
                if encrypt_file(file_path, password):
                    encrypted_count += 1
                else:
                    failed_count += 1

        print(f"\n=== Encryption Complete ===")
        print(f"Files encrypted: {encrypted_count}")
        print(f"Files skipped: {skipped_count}")
        print(f"Files failed: {failed_count}")

    except KeyboardInterrupt:
        print("\n\nEncryption interrupted by user.")
        print(f"Progress: {encrypted_count} encrypted, {skipped_count} skipped, {failed_count} failed")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")