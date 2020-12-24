f = open('task_6_test.txt', 'r', encoding='UTF-8')
subjects = {}
f_lines = f.readlines()
keys = []
i = 0
for el in f_lines:
    keys.append(el.split(':')[0])


for el in range(len(f_lines)):
    values = []
    for el in f_lines[i]:
        if el.isdigit():
            values.append(el)
        elif el == ')':
            values.append(' ')
    values = ''.join(values).split()
    summ = sum([int(el) for el in values])
    subjects[keys[i]] = summ
    i += 1

print(f_lines)
print(subjects)
