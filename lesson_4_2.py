user_list = []
user_str = input('Введите элементы исходного списка через пробел: ')
for i in user_str.split(' '):
    user_list.append(int(i))

print(f'Исходный список: {user_list}')
new_list = [user_list[el] for el in range(1, len(user_list)) if user_list[el] > user_list[el - 1]]
print(f'Новый список: {new_list}')
