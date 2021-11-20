str_num = 0
str = ('str')
with open("task_2.txt") as obj:
    while len(str) != 0:
        str = obj.readline()

        if not str:
            break

        word_num = 0
        str_num += 1

        for word in str.split(' '):
            word_num += 1

        print(f'Количество слов в строке {str_num}: {word_num}')

print(f'Количество строк в файле: {str_num}')
