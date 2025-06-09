import unittest
from enhanced_table import encrypt, decrypt

class TestEnhancedTableCipher(unittest.TestCase):
    def test_encrypt_simple(self):
        self.assertEqual(encrypt("HELLO", 3), "HLELOX")

    def test_encrypt_decrypt(self):
        msg = "Secret Message 123"
        key = 4
        encrypted = encrypt(msg, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, "SECRETMESSAGE123")

    def test_padding(self):
        self.assertEqual(encrypt("A", 5), "AXXXX")

    def test_decrypt_with_padding(self):
        encrypted = encrypt("HELLO", 4)
        self.assertEqual(decrypt(encrypted, 4), "HELLO")

if __name__ == '__main__':
    unittest.main()
