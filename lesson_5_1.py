with open("task_1.txt", "w") as obj:
    str = input('Введите строку данных: ')
    while len(str) != 0:
        obj.write(f'{str}\n')
        str = input('Введите новую строку данных: ')
