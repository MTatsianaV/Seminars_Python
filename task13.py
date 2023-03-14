'''Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. 
Они обратились к синоптикам, а те, занялись исследованиями статистики за прошлые годы. 
Их интересует, сколько дней длилась самая длинная оттепель. 
Оттепелью они называют период, в который среднесуточная температура ежедневно превышала 0 градусов Цельсия. 
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
В следующих строках располагается N целых чисел.
Каждое число – среднесуточная температура в соответствующий день. 
Температуры – целые числа и лежат в диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2'''


# Решение 1.
''' 
n = int(input('Введите количество исследуемых дней: '))
temps = list(map(int, input('Введите список температур через пробел: ').split()))
maxDuration = currentDuration = 0  # переменная для хранения максимальной и текущей длины оттепели
for temp in temps:
    if temp > 0:
        currentDuration += 1
    else:
        maxDuration = max(maxDuration, currentDuration)  # обновляем максимальную длину
        currentDuration = 0  # обнуляем текущую длину
maxDuration = max(maxDuration, currentDuration)  # проверяем последнюю оттепель
print(maxDuration) '''

# Решение 2.
''' num_days = int(input('Введите количество исследуемых дней: '))
days_list = []
for i in range(num_days):
    day = int(input('Введите температуры: '))
    days_list.append(day)
max_len = 0
temp_count = 0
for temp in days_list:
    if temp > 0:
        temp_count += 1
    else:
        if temp_count > max_len:
            max_len = temp_count
        temp_count = 0
if temp_count > max_len:
    max_len = temp_count
print(max_len) '''


# Решение 3.
''' num_days = int(input('Введите количество исследуемых дней: '))
days_list = []
for i in range(num_days):
    day = int(input(f'температура в день {i+1}-й: '))
    days_list.append(day)
max_len = 0
temp_count = 0
for temp in days_list:
    if temp > 0:
        temp_count += 1
    else:
        if temp_count > max_len:
            max_len = temp_count
        temp_count = 0
if temp_count > max_len:
    max_len = temp_count
print(max_len) '''


# Решение 4.
days_list = []
max_len = 0
temp_count = 0
num_days = int(input('Введите количество исследуемых дней: '))
for i in range(num_days):
    temp = int(input(f'температура в день {i+1}-й: '))
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0
    if temp_count > max_len:
        max_len = temp_count
print(max_len)
