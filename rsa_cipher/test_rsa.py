import unittest
from rsa import generate_primes, generate_keypair, encrypt, decrypt

class TestRSA(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.primes = generate_primes()

    def test_encrypt_decrypt(self):
        pub, priv = generate_keypair(self.primes)
        message = "HELLO RSA"
        cipher = encrypt(message, pub)
        plain = decrypt(cipher, priv)
        self.assertEqual(plain, message)

    def test_keypair_distinct(self):
        pub1, priv1 = generate_keypair(self.primes)
        pub2, priv2 = generate_keypair(self.primes)
        self.assertNotEqual(pub1[1], pub2[1])  # n должны различаться

if __name__ == '__main__':
    unittest.main()
