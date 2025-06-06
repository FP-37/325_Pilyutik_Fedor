"""
Дана последовательность чисел (по одному в строке, завершением последовательности является число 0). На их основе создать
словарь, в котором ключами выступают делители чисел, а значениями - списки чисел, делящихся на ключ. Вывести словарь
на экран в следующем формате: для каждой пары key:value вывести key в отдельной строке, затем элементы value по одному
в строке, затем пустую строку.
"""
# Считываем последовательность чисел до 0
nmbrs = []
while True:
    nmb = int(input())
    if nmb == 0:
        break
    nmbrs.append(nmb)

# Создаем словарь с делителями и списками чисел
dctnr = {}
for nmb in nmbrs:
    if nmb != 0:
        for delitel in range(1, nmb + 1):
            if nmb % delitel == 0:
                dctnr[delitel] = dctnr.get(delitel, []) + [nmb]

# Выводим словарь
for key, value in dctnr.items():
    print(key)
    for num in value:
        print(num)
    print()