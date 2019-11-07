"""
Кодировка и байты
"""

# строка - ?
# изображение - ?
# видео - ?
# звук - ?

print(ord('@'))
print(chr(64))

# байты и строки
some_str = 'hello'
print(type(some_str))

some_byte = b'hello'
print(some_byte)
print(type(some_byte))

for char in some_byte:
    print(char)

print(ord('Е'))

some_utf_8_str = 'тут русские буквы'

# Кодировние - получились байты
some_utf_8_bites = some_utf_8_str.encode('utf-8')

print(some_utf_8_bites)

# Декодирование из байт в строку
some_utf_8_str = some_utf_8_bites.decode('utf-8')

# Кодируем ASCII а декодируем UTF-8
some_utf_8_str = 'hello world'

# Кодировние - получились байты
some_utf_8_bites = some_utf_8_str.encode('ascii')

print(some_utf_8_str)

# Декодирование из байт в строку
some_utf_8_str = some_utf_8_bites.decode('utf-8')

# Кодируем latin-1 а декодируем UTF-8
some_utf_8_str = 'hello world üüüüüü'

# Кодировние - получились байты
some_utf_8_bites = some_utf_8_str.encode('latin-1')

print(some_utf_8_bites)

# Декодирование из байт в строку
# some_utf_8_str = some_utf_8_bites.decode('utf-8')
some_utf_8_str = some_utf_8_bites.decode('latin-1')

print(some_utf_8_str)

# Кодировка при записи в файл
with open('code.txt', 'w', encoding='utf-8') as f:
    f.write('ыыыыыы')

with open('code.txt', 'w', encoding='ascii') as f:
    f.write('abcde')

with open('code_utf8.txt', 'w', encoding='utf-8') as f:
    f.write('abcde')
