# Vigenere Cipher

## Описание
Реализация шифра Виженера для английского текста. Программа позволяет зашифровать и расшифровать сообщения с использованием ключа.

## Использование
Пример кода:

from vigenere import encrypt, decrypt

cipher = encrypt("HELLO WORLD", "KEY")
print(cipher)

Содержимое cipher: RIJVSUYVJN

plain = decrypt(cipher, "KEY")
print(plain)

Содержимое plain: HELLOWORLD

### Требования
- Python 3.6+

### ▶ Установка
```bash
git clone https://github.com/yourusername/vigenere_cipher.git
cd vigenere_cipher
