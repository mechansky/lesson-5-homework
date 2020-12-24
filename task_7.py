import json

f = open('task_7_test.txt', 'r+', encoding='UTF-8')
f_lines = f.readlines()
entities = {}
more_than_zero = []
report = []


def get_numbers(l):
    l_list = l.split()
    result = float(l_list[2]) - float(l_list[3])
    if result > 0:
        more_than_zero.append(result)
    return result


def get_name(l):
    l_list = l.split()
    return l_list[0]


def get_analytics(l):
    for element in f_lines:
        entities[get_name(element)] = get_numbers(element)


get_analytics(f_lines)
financial_results = {"average_profit": sum(more_than_zero) / len(more_than_zero)
                     }
report.append(entities)
report.append(financial_results)
print(report)

with open('task_7_test_2.txt', 'w', encoding='UTF-8') as f:
    json.dump(report, f)
