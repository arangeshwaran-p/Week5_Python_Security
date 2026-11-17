import hashlib
import secrets
import hmac
import re

def validate_username(username):
    if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
        raise ValueError("Invalid username")

def validate_password(password):
    if len(password) < 8 or len(password) > 128:
        raise ValueError("Password must be 8 to 128 characters")

def hash_password(password):
    salt = secrets.token_bytes(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        600000
    )

    return salt.hex() + "$" + hashed.hex()

def verify_password(password, stored):
    try:
        salt_hex, hash_hex = stored.split("$")
        salt = bytes.fromhex(salt_hex)
        expected = bytes.fromhex(hash_hex)

        actual = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode(),
            salt,
            600000
        )

        return hmac.compare_digest(actual, expected)

    except (ValueError, TypeError):
        return False
