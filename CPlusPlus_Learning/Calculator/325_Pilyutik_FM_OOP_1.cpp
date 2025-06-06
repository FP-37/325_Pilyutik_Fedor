/*
Дана последовательность строк, завершающаяся пустой строкой. На их основе создать словарь, в котором ключами выступают слова,
а значениями - списки строк, содержащих данные слова. Регистр и символы ',:;.?!-' не учитывать. Вывести словарь на экран
в следующем формате: для каждой пары key:value вывести key в отдельной строке, затем элементы value по одному в строке,
затем пустую строку. Используйте map и vector.
*/

#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

int main() {
    map<string, vector<string>> dctnr;
    string wrd;

    // Чтение строк до пустой строки
    while (true) {
        getline(cin, wrd);
        if (wrd.empty()) break;

        // Преобразование слова в нижний регистр и удаление символов
        wrd = wrd.lower();
        wrd.erase(remove(wrd.begin(),wrd.end(), '\'', ':', ';', '?', '.', '!', '-'), wrd.end());

        // Добавление слова в словарь
        if (dctnr.find(wrd) == dctnr.end()) {
            dctnr[wrd] = vector<string>();
        }

        // Добавление текущей строки в список строк для данного слова
        dctnr[wrd].push_back(wrd);
    }

    // Вывод словаря
    for (const auto& pair : dctnr) {
        cout << pair.first << endl;
        for (const auto& str : pair.second) {
            cout << str << endl;
        }
        cout << endl;
    }

    return 0;
}