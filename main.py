from encryptor import encrypt_file, encrypt_directory
from decryptor import decrypt_file, decrypt_directory
from key_utils import password_strength_check


def get_password(require_strength_check=True):
    """Get password from user with optional strength validation."""
    password = input("Enter password: ").strip()

    if require_strength_check:
        while not password_strength_check(password):
            password = input("Please enter a stronger password: ").strip()

    return password


def get_confirmation(message):
    """Get yes/no confirmation from user."""
    while True:
        response = input(f"{message} (yes/no): ").strip().lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


def main():
    print("=" * 40)
    print("            FILE ENCRYPTOR")
    print("=" * 40)

    while True:
        print("\nOptions:")
        print("  1. Encrypt a file")
        print("  2. Decrypt a file")
        print("  3. Encrypt a directory")
        print("  4. Decrypt a directory")
        print("  5. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Encrypt File ---")
            file_path = input("File path: ").strip()
            password = get_password(require_strength_check=True)
            encrypt_file(file_path, password)

        elif choice == "2":
            print("\n--- Decrypt File ---")
            file_path = input("File path: ").strip()
            password = get_password(require_strength_check=False)
            decrypt_file(file_path, password)

        elif choice == "3":
            print("\n--- Encrypt Directory ---")
            directory_path = input("Directory path: ").strip()
            password = get_password(require_strength_check=True)

            if get_confirmation(f"Encrypt ALL files in '{directory_path}' and subdirectories?"):
                encrypt_directory(directory_path, password)
            else:
                print("Encryption cancelled.")

        elif choice == "4":
            print("\n--- Decrypt Directory ---")
            directory_path = input("Directory path: ").strip()
            password = get_password(require_strength_check=False)

            if get_confirmation(f"Decrypt ALL .encrypted files in '{directory_path}' and subdirectories?"):
                decrypt_directory(directory_path, password)
            else:
                print("Decryption cancelled.")

        elif choice == "5":
            print("\n" + "=" * 40)
            print("Thank you for using File Encryptor!")
            print("=" * 40)
            break

        else:
            print("✗ Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n✗ Fatal error: {e}")