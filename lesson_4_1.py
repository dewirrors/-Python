from sys import argv

script_name, time, rate, prem = argv

sal = float(time) * float(rate) + float(prem)
print(f'Заработная плата сотрудника: {sal}')
