def custom_hash(data: bytes) -> bytes:
    state = [i for i in range(32)]

    for i, byte in enumerate(data):
        index = i % 32
        state[index] ^= (byte + index) % 256
        state[index] = ((state[index] << 1) | (state[index] >> 7)) & 0xFF

    for i in range(64):
        a = i % 32
        b = (i * 7) % 32
        state[a] ^= state[b]
        state[a] = (state[a] + i) % 256

    return bytes(state)