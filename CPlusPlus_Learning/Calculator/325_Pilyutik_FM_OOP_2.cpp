/*
Дана последовательность чисел (по одному в строке, завершением последовательности является число 0).
На их основе создать словарь, в котором ключами выступают делители чисел, а значениями - списки чисел, делящихся на ключ.
Вывести словарь на экран в следующем формате: для каждой пары key:value вывести key в отдельной строке,
затем элементы value по одному в строке, затем пустую строку.
*/

#include <iostream>
#include <map>
#include <vector>

using namespace std;

int main() {
    map<int, vector<int>> del_dctnr;
    int number;

    // Чтение последовательности чисел
    do {
        cin >> number;
        if (number == 0) break;

        // Создание словаря
        for (int i = 1; i <= number; ++i) {
            if (number % i == 0) {
                // Проверка на существование ключа
                if (del_dctnr.find(i) != del_dctnr.end()) {
                    del_dctnr[i].push_back(number);
                } else {
                    vector<int> values;
                    values.push_back(number);
                    del_dctnr.insert({i, values});
                }
            }
        }
    } while (true);

    // Вывод словаря
    for (const auto& pair : del_dctnr) {
        cout << pair.first << endl;
        for (const auto& num : pair.second) {
            cout << num << endl;
        }
        cout << endl;
    }

    return 0;
}