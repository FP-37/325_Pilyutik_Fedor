"""
В шифре Цезаря каждый символ заменяется на другой символ, третий по счету в алфавите после данного, с цикличность.
То есть символ A заменяется на D, символ B - на E, символ C - на F, ..., символ Z на C.
Аналогично строчные буквы заменяются на строчные буквы. Все остальные символы не меняются.

Дана строка, зашифруйте ее при помощи шифра Цезаря. Решение оформите в виде функции CaesarCipher (S, k),
возвращающей новую строку.
S — исходная строка,
k — величина сдвига. Функцию нужно вызывать со значением k=3.

Указание: сделайте функцию CaesarCipherChar(c, k), шифрующую один символ.
"""
def CaesarCipher(S,k):

    new_string = ""

    for letter in S:

        if letter == " ":
            new_string += letter
            continue

        num_of_l = ord(letter)

        if (num_of_l >= 97 and num_of_l <= 119) or (num_of_l >= 65 and num_of_l <= 87):
            letter = chr(num_of_l+k)
        elif (num_of_l >= 123-k and num_of_l <= 122) or (num_of_l >= 90-k and num_of_l <= 90):
            if letter.isupper():
                letter = chr(64+(num_of_l%(89-k)))
            else:
                letter = chr(96+(num_of_l%(122-k)))
        new_string += letter
        
    return new_string

our_string = input()

print(CaesarCipher(our_string,3))