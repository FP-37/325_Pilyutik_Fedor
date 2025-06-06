"""
Словарь задан массивом отсортированных в лексикографическом порядке строк.
Напишите программу эффективного поиска слова в словаре.

Входные данные
На вход программе сначала подается искомое слово, во второй строке — число n (1 <= n <= 100000) — количество слов
в словаре. В следующих n строках расположены слова словаря, по одному слову в строке.
Все слова состоят только из строчных латинских букв, слова упорядочены по алфавиту
(расположены в лексикографическом порядке).

Длина слов не превосходит 20. Пустых слов нет.

Выходные данные
Выведите YES или NO в зависимости от того, есть искомое слово в словаре или нет.
"""
def binary_search(word, dictionary):
    low = 0
    high = len(dictionary) - 1

    while low <= high:
        mid = (low + high) // 2
        if dictionary[mid] == word:
            return "YES"
        elif dictionary[mid] < word:
            low = mid + 1
        else:
            high = mid - 1

    return "NO"

def main():
    word_to_find = input()
    n = int(input())
    dictionary = [input() for _ in range(n)]

    result = binary_search(word_to_find, dictionary)
    print(result)

if __name__ == "__main__":
    main()