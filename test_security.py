
import unittest
from security import (
    validate_username,
    validate_password,
    hash_password,
    verify_password
)

class TestSecurity(unittest.TestCase):

    def test_valid_username(self):
        validate_username("arang123")

    def test_invalid_username(self):
        with self.assertRaises(ValueError):
            validate_username("ab")

    def test_invalid_password(self):
        with self.assertRaises(ValueError):
            validate_password("123")

    def test_password_hash(self):
        hashed = hash_password("password123")
        self.assertTrue(verify_password("password123", hashed))

    def test_wrong_password(self):
        hashed = hash_password("password123")
        self.assertFalse(verify_password("wrong123", hashed))

if __name__ == "__main__":
    unittest.main()
