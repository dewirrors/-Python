with open("task_5.txt", "w") as obj:
    obj.write(input('Введите набор чисел, разделенных пробелами: '))

sum = 0
with open("task_5.txt") as obj:
    ints = obj.readline()
    for i in ints.split(' '):
        sum += int(i)

print(f'Сумма чисел в файле: {sum}')
