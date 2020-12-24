f = open('task_5_test.txt', 'w', encoding='UTF-8')
f.write(input('Введите числа через пробел: '))
f.close()

f = open('task_5_test.txt', 'r+', encoding='UTF-8')
data = [int(el) for el in f.read().split()]
print(f'сумма введенных в файле чисел составляет: {sum(data)}')

f.close()
