def sum_func(nums_str):
    nums_list = nums_str.split(' ')
    sum = 0
    for el in nums_list:
        if el == '#':
            break
        sum += float(el)

    return sum


s = 0
finish = False
while not finish:
    nums_str = input('Введите несколько чисел для суммирования через пробел. После введения последнего слагаемого нажмите #: ')
    nums_str_user = sum_func(nums_str)
    s += nums_str_user
    finish = '#' in nums_str
    print(f'Сумма чисел: {s}')
