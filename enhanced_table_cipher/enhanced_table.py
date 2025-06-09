import math

def prepare_text(text):
    return ''.join(filter(str.isalnum, text.upper()))


def encrypt(text, key):
    text = prepare_text(text)
    cols = key
    rows = math.ceil(len(text) / cols)
    padded_text = text.ljust(rows * cols, 'X')

    table = [padded_text[i*cols:(i+1)*cols] for i in range(rows)]
    ciphertext = ''.join(''.join(row[i] for row in table) for i in range(cols))
    return ciphertext


def decrypt(ciphertext, key):
    cols = key
    rows = math.ceil(len(ciphertext) / cols)
    total = rows * cols
    extra = total - len(ciphertext)
    ciphertext += 'X' * extra

    col_len = rows
    table = [''] * rows
    index = 0

    for col in range(cols):
        for row in range(rows):
            table[row] += ciphertext[index]
            index += 1

    plaintext = ''.join(table)
    return plaintext.rstrip('X')
