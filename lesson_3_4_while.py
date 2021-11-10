def my_func(x, y):
    y += 1
    power = x
    while y < 0:
        power *= x
        y += 1

    power = 1 / power
    return power


x = float(input('Введите действительное положительное число x: '))
y = int(input('Введите целое отрицательное число y: '))
print('Результат возведения x в степень y: ', my_func(x, y))
