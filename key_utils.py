import re
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Random import get_random_bytes
from Crypto.Hash import SHA256


def password_strength_check(password: str) -> bool:
    """ Validate password strength against security requirements. """
    if not password or password.strip() == "":
        print("Error: Password cannot be empty.")
        return False

    if len(password) < 8:
        print("✗ Password too short. Minimum 8 characters required.")
        return False

    if not re.search(r"[A-Z]", password):
        print("✗ Password must include at least one uppercase letter.")
        return False

    if not re.search(r"[a-z]", password):
        print("✗ Password must include at least one lowercase letter.")
        return False

    if not re.search(r"[0-9]", password):
        print("✗ Password must include at least one number.")
        return False

    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("✗ Password must include at least one special character (!@#$%^&*...).")
        return False

    return True


def salt_key_generator(password: str, salt: bytes = None, iterations: int = 200_000) -> tuple:
    """ Generate a cryptographic key from a password using PBKDF2. """
    if salt is None:
        salt = get_random_bytes(16)

    key = PBKDF2(
        password=password,
        salt=salt,
        dkLen=32,
        count=iterations,
        hmac_hash_module=SHA256
    )

    return salt, key