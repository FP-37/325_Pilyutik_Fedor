#include <iostream>
#include <string>

using namespace std;

// Функции для выполнения операций
double multiply(double a, double b) {
    return a * b;
}

double divide(double a, double b) {
    return a / b;
}

double remainder(double a, double b) {
    return a % b;
}

double sum(double a, double b) {
    return a + b;
}

double difference(double a, double b) {
    return a - b;
}

// Функция для запроса операндов и выполнения операции
void calculate(string operation, double operand1, double operand2) {
    double result;
    
    switch (operation) {
        case "умножение":
            result = multiply(operand1, operand2);
            break;
        case "деление":
            result = divide(operand1, operand2);
            break;
        case "остаток":
            result = remainder(operand1, operand2);
            break;
        case "сумма":
            result = sum(operand1, operand2);
            break;
        case "разность":
            result = difference(operand1, operand2);
            break;
        default:
            result = 0; // Некорректная операция
    }

    cout << "Результат: " << result << endl;
}

// Функция для запроса ранее введенных данных
void usePreviousData() {
    cout << "Выберите операцию, для которой хотите использовать ранее введенные данные: " << endl;
    cout << "1. Умножение\n2. Деление\n3. Остаток\n4. Сумма\n5. Разность\n";
    int choice;
    cin >> choice;

    double operand1, operand2;
    cout << "Введите первый операнд: ";
    cin >> operand1;

    cout << "Введите второй операнд: ";
    cin >> operand2;

    calculate(operationMap[choice], operand1, operand2);
}

// Маппинг операций
const string operationMap[] = {"умножение", "деление", "остаток", "сумма", "разность"};

int main() {
    // Меню выбора операции
    cout << "Выберите операцию: " << endl;
    cout << "1. Умножение\n2. Деление\n3. Остаток\n4. Сумма\n5. Разность\n6. Использовать ранее введенные данные" << endl;
    int choice;
    cin >> choice;

    double operand1, operand2;
    
    switch (choice) {
        case 1:
            cout << "Введите первый операнд: ";
            cin >> operand1;

            cout << "Введите второй операнд: ";
            cin >> operand2;

            calculate("умножение", operand1, operand2);
            break;
        case 2:
            cout << "Введите первый операнд: ";
            cin >> operand1;

            cout << "Введите второй операнд: ";
            cin >> operand2;

            calculate("деление", operand1, operand2);
            break;
        case 3:
            cout << "Введите первый операнд: ";
            cin >> operand1;

            cout << "Введите второй операнд: ";
            cin >> operand2;

            calculate("остаток", operand1, operand2);
            break;
        case 4:
            cout << "Введите первый операнд: ";
            cin >> operand1;

            cout << "Введите второй операнд: ";
            cin >> operand2;

            calculate("сумма", operand1, operand2);
            break;
        case 5:
            cout << "Введите первый операнд: ";
            cin >> operand1;

            cout << "Введите второй операнд: ";
            cin >> operand2;

            calculate("разность", operand1, operand2);
            break;
        case 6:
            usePreviousData();
            break;
        default:
            cout << "Некорректный выбор. Попробуйте еще раз." << endl;
            main();
    }

    return 0;
}