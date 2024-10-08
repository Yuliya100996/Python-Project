def custom_write(file_name, strings):
    table = {}
    file = open(file_name, 'a', encoding='utf-8')
    number = 1
    for i in strings:
        _tell = file.tell()
        file.write(f'{i}\n')
        table.update({(number, _tell) : i})
        number +=1
    file.close()
    return table


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)