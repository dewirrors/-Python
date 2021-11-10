def my_func(var_1, var_2, var_3):
    sum = var_1 + var_2 + var_3
    my_min = min(var_1, var_2, var_3)
    sum = sum - my_min
    return sum


var_1 = float(input('Введите первый аргумент: '))
var_2 = float(input('Введите второй аргумент: '))
var_3 = float(input('Введите третий аргумент: '))
print('Сумма двух наибольших аргументов: ', my_func(var_1, var_2, var_3))
