import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from key_utils import salt_key_generator


def decrypt_file(input_file: str, password: str):
    """Decrypt a single file encrypted with AES-256-CBC."""
    if not input_file or input_file.strip() == "":
        print("Error: File path cannot be empty.")
        return False

    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' does not exist.")
        return False

    if not os.path.isfile(input_file):
        print(f"Error: '{input_file}' is not a valid file.")
        return False

    if not input_file.endswith(".encrypted"):
        print("Error: Input file must have .encrypted extension.")
        return False

    try:
        with open(input_file, "rb") as file:
            data = file.read()

        if len(data) < 32:
            print(f"Error: File '{input_file}' is too small to be a valid encrypted file.")
            return False

        salt = data[:16]
        iv = data[16:32]
        ciphertext = data[32:]

        _, key = salt_key_generator(password, salt)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), AES.block_size)

        with open(input_file, "wb") as file:
            file.write(decrypted)

        os.rename(input_file, input_file[:-10])
        print(f"✓ {input_file} successfully decrypted!")
        return True

    except ValueError:
        print(f"Error: Decryption failed. Wrong password or corrupted file.")
        return False
    except PermissionError:
        print(f"Error: Permission denied to access '{input_file}'.")
        return False
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
        return False


def decrypt_directory(directory_path: str, password: str):
    """Recursively decrypt all .encrypted files in a directory and its subdirectories."""
    decrypted_count = 0
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

                # Only decrypt .encrypted files
                if not file_path.endswith(".encrypted"):
                    skipped_count += 1
                    continue

                print(f"Decrypting: {file_path}")
                if decrypt_file(file_path, password):
                    decrypted_count += 1
                else:
                    failed_count += 1

        print(f"\n=== Decryption Complete ===")
        print(f"Files decrypted: {decrypted_count}")
        print(f"Files skipped: {skipped_count}")
        print(f"Files failed: {failed_count}")

    except KeyboardInterrupt:
        print("\n\nDecryption interrupted by user.")
        print(f"Progress: {decrypted_count} decrypted, {skipped_count} skipped, {failed_count} failed")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")