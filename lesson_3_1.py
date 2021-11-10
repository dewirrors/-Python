def div_func(num, den):
    div = num / den
    return div


num = float(input('Введите числитель: '))
den = float(input('Введите знаменатель: '))
while den == 0:
    den = float(input('Знаменатель должен быть отличен от нуля! Введите новый знаменатель: '))

print('Частное: ', div_func(num, den))
