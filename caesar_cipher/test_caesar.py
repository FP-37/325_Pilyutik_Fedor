import unittest
from caesar import caesar_encrypt, caesar_decrypt

class TestCaesarCipher(unittest.TestCase):
    def test_encrypt_lowercase(self):
        self.assertEqual(caesar_encrypt('abc', 3), 'def')

    def test_encrypt_uppercase(self):
        self.assertEqual(caesar_encrypt('XYZ', 3), 'ABC')

    def test_encrypt_mixed(self):
        self.assertEqual(caesar_encrypt('Hello, World!', 5), 'Mjqqt, Btwqi!')

    def test_decrypt(self):
        self.assertEqual(caesar_decrypt('Mjqqt, Btwqi!', 5), 'Hello, World!')

    def test_encrypt_decrypt(self):
        original = 'Caesar Cipher!'
        shift = 7
        encrypted = caesar_encrypt(original, shift)
        decrypted = caesar_decrypt(encrypted, shift)
        self.assertEqual(decrypted, original)

if __name__ == '__main__':
    unittest.main()
