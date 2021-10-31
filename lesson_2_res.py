#1
print('Задание 1')
my_list = [4, 'Hi', 9.7, 937, 'Python', True]
for el in my_list:
    print(el, type(el))

print(' ')

#3_list
print('Задание 3 (решение через list)')
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
winter_list = [1, 2, 12]
spring_list = [3, 4, 5]
summer_list = [6, 7, 8]
autumn_list = [9, 10, 11]
for el in winter_list:
    if el == month:
        print('Зима')

for el in spring_list:
    if el == month:
        print('Весна')

for el in summer_list:
    if el == month:
        print('Лето')

for el in autumn_list:
    if el == month:
        print('Осень')

print(' ')

#3_dict
print('Задание 3 (решение через dict)')
month = int(input('Введите месяц в виде целого числа от 1 до 12: '))
month_dict = {1: 'Зима', 2: 'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето', 7: 'Лето', 8: 'Лето', 9: 'Осень', 10: 'Осень', 11: 'Осень', 12: 'Зима'}
print(month_dict.get(month))
print(' ')

#4
print('Задание 4')
user_str = input('Введите строку из нескольких слов, разделённых пробелами: ')
for index, el in enumerate(user_str.split(), 1):
    print(index, el[0:10])

print(' ')

#5
print('Задание 5')
rat_list = [8, 8, 5, 4, 4, 1]
print('Текущий рейтинг: ', rat_list)
user_rat = int(input('Введите новый элемент рейтинга: '))
index = -1
for el in rat_list:
    index += 1
    if user_rat > el:
        rat_list.insert(index, user_rat)
        print('Обновлённый рейтинг: ', rat_list)
        break
