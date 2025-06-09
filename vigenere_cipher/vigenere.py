def prepare_text(text):
    return ''.join(filter(str.isalpha, text.upper()))


def extend_key(message, key):
    key = key.upper()
    repeated_key = (key * ((len(message) // len(key)) + 1))[:len(message)]
    return repeated_key


def encrypt(message, key):
    message = prepare_text(message)
    key = extend_key(message, key)
    encrypted = []
    for m_char, k_char in zip(message, key):
        shift = (ord(m_char) + ord(k_char) - 2 * ord('A')) % 26
        encrypted.append(chr(shift + ord('A')))
    return ''.join(encrypted)


def decrypt(ciphertext, key):
    ciphertext = prepare_text(ciphertext)
    key = extend_key(ciphertext, key)
    decrypted = []
    for c_char, k_char in zip(ciphertext, key):
        shift = (ord(c_char) - ord(k_char) + 26) % 26
        decrypted.append(chr(shift + ord('A')))
    return ''.join(decrypted)