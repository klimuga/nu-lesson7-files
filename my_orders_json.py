"""
Программа для сохранения покупок
Название + Цена

ЗАДАНИЕ 1
1. В подпрограмме Мой банковский счет;
2. Добавить сохранение суммы счета в файл.

При первом открытии программы на счету 0
После того как мы воспользовались программой и вышли сохранить сумму счета
При следующем открытии программы прочитать сумму счета, которую сохранили
...
3. Добавить сохранение истории покупок в файл

При первом открытии программы истории нет.
После того как мы что нибудь купили и закрыли программу сохранить историю покупок.
При следующем открытии программы прочитать историю и новые покупки уже добавлять к ней;
...
4. Формат сохранения количество файлов и способ можно выбрать самостоятельно.
"""
import os
import json

FILE_NAME = 'orders_json.json'

orders = []
TotalCost = 0
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'r') as f:
        orders = json.load(f)
    if orders == []:
        TotalCost = 0
    else:
        TotalCost = orders[len(orders)-1][2]



while True:
    print('1. Добавить покупку')
    print('2. История покупок')
    print('3. Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input('Введите название: ')
        cost = int(input('Введите цену: '))
        TotalCost = TotalCost + cost
        order = (name, cost, TotalCost)
        orders.append(order)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILE_NAME, 'w') as f:
            json.dump(orders, f)
        break
    else:
        print('Неправильно введены даные')

