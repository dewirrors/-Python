#1
print('Ex. 1')
var_1 = 5
var_2 = 7
var_3 = 4
var_4 = 9
print("Initial variables: ", var_1, var_2, var_3, var_4)
user_var_1 = input('Enter the first number: ')
user_var_2 = input('Enter the second number: ')
user_var_3 = input('Enter the first string: ')
user_var_4 = input('Enter the second string: ')
var_1 = user_var_1
var_2 = user_var_2
var_3 = user_var_3
var_4 = user_var_4
print("User's variables: ", var_1, var_2, var_3, var_4)
print (' ')

#2
print('Ex. 2')
time_s = int(input('Enter time (secs): '))
time_min = 0
time_h = 0
if time_s > 59:
    time_min = time_s // 60
    time_s = time_s % 60
    if time_min > 59:
        time_h = time_min // 60
        time_min = time_min % 60

if time_s < 10 and time_min < 10 and time_h < 10:
    print(f'Time: 0{time_h}:0{time_min}:0{time_s}')
elif time_s < 10 and time_min < 10:
    print(f'Time: {time_h}:0{time_min}:0{time_s}')
elif time_s < 10 and time_h < 10:
    print(f'Time: 0{time_h}:{time_min}:0{time_s}')
elif time_min < 10 and time_h < 10:
    print(f'Time: 0{time_h}:0{time_min}:{time_s}')
elif time_s < 10:
    print(f'Time: {time_h}:{time_min}:0{time_s}')
elif time_min < 10:
    print(f'Time: {time_h}:0{time_min}:{time_s}')
elif time_h < 10:
    print(f'Time: 0{time_h}:{time_min}:{time_s}')
else:
    print(f'Time: {time_h}:{time_min}:{time_s}')

print (' ')

#3
print('Ex. 3')
n = input('Enter single-digit number n: ')
nn = int(n * 2)
nnn = int(n * 3)
n = int(n)
sum = n + nn + nnn
print('n + nn + nnn =', sum)
print (' ')

#4
print('Ex. 4')
user_int = int(input('Enter positive integer: '))
biggest_numb = 0
while user_int > 0:
    ref = user_int % 10
    user_int = user_int // 10
    if ref > biggest_numb:
        biggest_numb = ref

print('The biggest number is', biggest_numb)
print (' ')

#5
print('Задание 5')
proceeds = float(input('Введите значение выручки фирмы: '))
costs = float(input('Введите значение издержек фирмы: '))
if proceeds > costs:
    print('Фирма работает в прибыль!')
    rent = (proceeds - costs) / proceeds
    print('Рентабельность выручки: ', rent)
    workers = int(input('Введите число сотрудников в фирме: '))
    profit_w = (proceeds - costs) / workers
    print('Прибыль фирмы в расчёте на одного сотрудника: ', profit_w)
elif proceeds < costs:
    print('Фирма работает в убыток.')
else:
    print('Фирма не приносит дохода, но и не работает в минус.')

print (' ')

#6
print('Задание 6')
first = float(input('Введите результат пробежки в первый день (в км): '))
wish = float(input('Введите желаемый результат пробежки (в км): '))
day = 1
while first < wish:
    first = first * 1.1
    day = day + 1

print(f'На {day}-й день спортсмен пробежал не менее {wish} км.')
