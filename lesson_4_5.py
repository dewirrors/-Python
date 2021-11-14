from functools import reduce

def my_func(el_1, el_2):
    return el_1 * el_2


my_list = [el for el in range(100, 1001) if el % 2 == 0]
print(f'Произведение всех элементов спсика: {reduce(my_func, my_list)}')
