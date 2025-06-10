def prepare_text(text):
    text = text.upper().replace('J', 'I')
    text = ''.join(filter(str.isalpha, text))
    result = ''
    i = 0
    while i < len(text):
        a = text[i]
        b = ''
        if i + 1 < len(text):
            b = text[i + 1]
        if a == b:
            result += a + 'X'
            i += 1
        else:
            result += a + (b if b else 'X')
            i += 2
    if len(result) % 2 != 0:
        result += 'X'
    return result


def generate_key_square(keyword):
    keyword = keyword.upper().replace('J', 'I')
    seen = set()
    square = []
    for char in keyword + 'ABCDEFGHIKLMNOPQRSTUVWXYZ':
        if char not in seen and char.isalpha():
            seen.add(char)
            square.append(char)
    return [square[i:i+5] for i in range(0, 25, 5)]


def find_position(char, square):
    for r, row in enumerate(square):
        for c, val in enumerate(row):
            if val == char:
                return r, c
    raise ValueError(f"Char not found in square: {char}")


def encrypt_pair(a, b, square):
    r1, c1 = find_position(a, square)
    r2, c2 = find_position(b, square)
    if r1 == r2:
        return square[r1][(c1 + 1) % 5] + square[r2][(c2 + 1) % 5]
    elif c1 == c2:
        return square[(r1 + 1) % 5][c1] + square[(r2 + 1) % 5][c2]
    else:
        return square[r1][c2] + square[r2][c1]


def decrypt_pair(a, b, square):
    r1, c1 = find_position(a, square)
    r2, c2 = find_position(b, square)
    if r1 == r2:
        return square[r1][(c1 - 1) % 5] + square[r2][(c2 - 1) % 5]
    elif c1 == c2:
        return square[(r1 - 1) % 5][c1] + square[(r2 - 1) % 5][c2]
    else:
        return square[r1][c2] + square[r2][c1]


def encrypt(text, keyword):
    square = generate_key_square(keyword)
    prepared = prepare_text(text)
    return ''.join(encrypt_pair(prepared[i], prepared[i+1], square) for i in range(0, len(prepared), 2))


def decrypt(ciphertext, keyword):
    square = generate_key_square(keyword)
    return ''.join(decrypt_pair(ciphertext[i], ciphertext[i+1], square) for i in range(0, len(ciphertext), 2))
