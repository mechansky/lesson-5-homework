f = open('test.txt', 'w', encoding='UTF-8')


while True:
    user_answer = input('ввод данных: ')
    if user_answer == ' ' or user_answer == '  ':
        break
    else:
        f.write(f'{user_answer}\n')


f.close()

