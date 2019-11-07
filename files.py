"""
Примеры работы с текстовомы файлами
"""

# open, close не оптимальный способ
f = open('models.txt', 'w')

f.write('hello\n')
f.write('hello\n')
f.write('hello\n')

f.writelines(['1\n', '2\n', '3\n', 'end\n'])

data = ['1;', '2;', '3;']
f.writelines(data)

f.close()

# менеджер контекста
with open('models.txt', 'w') as f:
    f.write('hello\n')
    f.write('hello\n')
    f.write('hello\n')

    f.writelines(['1\n', '2\n', '3\n', 'end\n'])

    data = ['1;', '2;', '3;']
    f.writelines(data)

print('end')

# Чтение файла
with open('models.txt', 'r') as f:
    # 1. Прочитать сразу все данные
    result = f.read()
    print(result)

print('*' * 100)
with open('models.txt', 'r') as f:
    # 2. Прочитать построчно
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)

print('*' * 100)
with open('models.txt', 'r') as f:
    # 2. Читам все строки в цикле
    for line in f:
        # line - это каждая строка
        line = line.replace('\n', '')
        print(line)

print('*' * 100)
with open('models.txt', 'r') as f:
    # 2. Читам все строки в цикле
    lines = f.readlines()
    print(lines)