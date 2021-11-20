#Почему-то не работает(
gen = 0
workers = 0
with open("task_3.txt") as obj:
    str_list = obj.readlines()
    for str in str_list:

        for index, val in enumerate(str.split(' - ')):

            if index == 0:
                sur = val
                workers += 1
            else:
                sal = float(val)
                gen += sal

                if sal < 20000:
                    print(f'Сотрудник {sur} имеет оклад менее 20000.')

sal_med = gen / workers
print(f'Средняя величина доходов сотрудников: {sal_med}')
