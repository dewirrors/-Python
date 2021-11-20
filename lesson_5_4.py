#Тоже не работает
word_dict = dict(One='Один', Two='Два', Three='Три', Four='Четыре')

with open("task_4.txt") as obj, open("task_4_1.txt", "w") as new_f:
    str_list = obj.readlines()
    for line in str_list:

        for index, num in enumerate(line.split(' — ')):
            if index == 0:
                rus = word_dict.get(num)
            else:
                new_f.write(f'{rus} — {num}\n')
