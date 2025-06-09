import unittest
from vigenere import encrypt, decrypt

class TestVigenereCipher(unittest.TestCase):
    def test_encrypt_basic(self):
        self.assertEqual(encrypt("ATTACKATDAWN", "LEMON"), "LXFOPVEFRNHR")

    def test_decrypt_basic(self):
        self.assertEqual(decrypt("LXFOPVEFRNHR", "LEMON"), "ATTACKATDAWN")

    def test_encrypt_with_spaces(self):
        self.assertEqual(encrypt("HELLO WORLD", "KEY"), "RIJVSUYVJN")

    def test_decrypt_with_spaces(self):
        self.assertEqual(decrypt("RIJVSUYVJN", "KEY"), "HELLOWORLD")

    def test_encrypt_decrypt(self):
        original = "Vigenere Cipher Example"
        key = "Secret"
        encrypted = encrypt(original, key)
        decrypted = decrypt(encrypted, key)
        self.assertEqual(decrypted, "VIGENERECIPHEREXAMPLE")

if __name__ == '__main__':
    unittest.main()
