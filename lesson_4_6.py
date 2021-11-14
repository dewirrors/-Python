from itertools import count, cycle

print('Итератор целых чисел: ', end='')
for i in count(21):
    if i > 30:
        break
    else:
        print(i, end=' ')

print('')
print('Итератор-повторитель: ', end='')
k = 0
iter_list = [1, 2, 3, 4, 5]
for j in cycle(iter_list):
    if k > 30:
        break
    k += 1
    print(j, end=' ')
