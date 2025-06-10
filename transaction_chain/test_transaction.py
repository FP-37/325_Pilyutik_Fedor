import unittest
from transaction import Transaction, generate_key_pair

class TestTransaction(unittest.TestCase):
    def test_sign_and_verify(self):
        priv, pub = generate_key_pair()

        tx = Transaction(
            inputs=[{"txid": "abc123", "index": 0}],
            outputs=[{"address": "Bob", "amount": 10}]
        )

        tx.sign(priv)
        self.assertTrue(tx.verify_signature(pub))

    def test_fail_with_wrong_key(self):
        priv1, pub1 = generate_key_pair()
        priv2, pub2 = generate_key_pair()

        tx = Transaction(
            inputs=[{"txid": "abc123", "index": 0}],
            outputs=[{"address": "Alice", "amount": 50}]
        )
        tx.sign(priv1)
        self.assertFalse(tx.verify_signature(pub2))

if __name__ == '__main__':
    unittest.main()
