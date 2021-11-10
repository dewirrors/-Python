def data_func(name, sur, yr, city, email, tel):
    return f"Имя: {name}; фамилия: {sur}; год рождения: {yr}; город проживания: {city}; email: {email}; телефон: {tel}"


n = input('Введите имя: ')
s = input('Введите фамилию: ')
y = input('Введите год рождения: ')
c = input('Введите город проживания: ')
e = input('Введите email: ')
t = input('Введите телефон: ')
print(data_func(name = n, sur = s, yr = y, city  =c, email = e, tel = t))
