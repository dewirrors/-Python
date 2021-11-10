def my_func(x, y):
    power = 1 / (x ** abs(y))
    return power


x = float(input('Введите действительное положительное число x: '))
y = int(input('Введите целое отрицательное число y: '))
print('Результат возведения x в степень y: ', my_func(x, y))
