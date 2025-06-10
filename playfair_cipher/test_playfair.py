import unittest
from playfair import encrypt, decrypt

class TestPlayfairCipher(unittest.TestCase):
    def test_encrypt(self):
        self.assertEqual(encrypt("HELLO", "KEYWORD"), "RIJVSX")

    def test_decrypt(self):
        self.assertEqual(decrypt("RIJVSX", "KEYWORD"), "HELXLO")

    def test_double_letters(self):
        self.assertEqual(encrypt("BALLOON", "KEYWORD"), "DBMMLPVN")

    def test_encrypt_decrypt_cycle(self):
        original = "DEFEND THE EAST WALL"
        keyword = "MONARCHY"
        encrypted = encrypt(original, keyword)
        decrypted = decrypt(encrypted, keyword)
        self.assertTrue("DEFENDTHEEASTWALL".replace('J', 'I') in decrypted)

if __name__ == '__main__':
    unittest.main()
