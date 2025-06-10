import json
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa


class Transaction:
    def __init__(self, inputs, outputs, signature=None):
        self.inputs = inputs
        self.outputs = outputs
        self.signature = signature

    def to_dict(self, include_signature=True):
        data = {
            "inputs": self.inputs,
            "outputs": self.outputs
        }
        if include_signature and self.signature:
            data["signature"] = self.signature.hex()
        return data

    def serialize(self):
        return json.dumps(self.to_dict(include_signature=False), sort_keys=True).encode()

    def sign(self, private_key):
        self.signature = private_key.sign(
            self.serialize(),
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )

    def verify_signature(self, public_key):
        try:
            public_key.verify(
                self.signature,
                self.serialize(),
                padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False


def generate_key_pair():
    priv = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pub = priv.public_key()
    return priv, pub
