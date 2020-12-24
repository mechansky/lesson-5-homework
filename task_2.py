f = open('task_2_test.txt', 'r', encoding='UTF-8')
content = f.readlines()
print(content)


len_f = len(content)
print(f'Количество строк в файле "{f.name}": {len_f}')

i = 1
for string in content:
    print(f'Количество слов в строке {i}: {len(string.split())}')
    i += 1

f.close()