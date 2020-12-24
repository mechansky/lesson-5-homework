f = open('task_3_test.txt', 'r', encoding='UTF-8')
list_of_salaries = []


def from_list_to_dict(l):
    print(f'Сотрудники, которые получают менее 20000 руб:')
    for element in l:
        new_element = element.split()
        list_of_salaries.append(float(new_element[1]))
        if float(new_element[1]) < 20000:
            print(f'{new_element[0]}: {float(new_element[1])} руб')
        else:
            continue
    average_salary = (sum(list_of_salaries)/len(list_of_salaries))
    print(f'Средняя зарплата всех сотрудников: {round(average_salary, 2)} руб')


f_lines = f.readlines()
from_list_to_dict(f_lines)

f.close()
