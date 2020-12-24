f = open('task_4_test.txt', 'r', encoding='UTF-8')

numbers = {'One': 'Один',
           'Two': 'Два',
           'Three': 'Три',
           'Four': 'Четыре'
           }
f_lines = f.readlines()
result_list = []

def from_english_to_russian(l):
    for el in l:
        number = el.split()
        if number[0] in numbers.keys():
            number[0] = numbers[number[0]]
            result_list.append(' '.join(number))


from_english_to_russian(f_lines)
f2 = open('task_4_test_2.txt', 'w', encoding='UTF-8')
for el in result_list:
    f2.write(f'{el}\n')
f2.close()
