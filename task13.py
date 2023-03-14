'''Уставшие от необычно теплой зимы, жители решили узнать, 
действительно ли это самая длинная оттепель за всю историю 
наблюдений за погодой. Они обратились к синоптикам, а те, в 
свою очередь, занялись исследованиями статистики за 
прошлые годы. Их интересует, сколько дней длилась самая 
длинная оттепель. Оттепелью они называют период, в 
который среднесуточная температура ежедневно превышала 
0 градусов Цельсия. Напишите программу, помогающую 
синоптикам в работе.
Пользователь вводит число N – общее количество
рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
располагается N целых чисел.
Каждое число – среднесуточная температура в
соответствующий день. Температуры – целые числа и лежат в
диапазоне от –50 до 50
Input: 6 -> -20 30 -40 50 10 -10
Output: 2'''
n = int(input())  # ввод количества дней
temps = list(map(int, input().split()))  # ввод температур в список

max_len = 0  # переменная для хранения максимальной длины оттепели
current_len = 0  # переменная для хранения текущей длины оттепели

for temp in temps:
    if temp > 0:  # если температура выше нуля, то это продолжение оттепели
        current_len += 1
    else:  # иначе оттепель закончилась
        max_len = max(max_len, current_len)  # обновляем максимальную длину
        current_len = 0  # обнуляем текущую длину

max_len = max(max_len, current_len)  # проверяем последнюю оттепель

print(max_len)  # выводим результат

num_days = int(input('Num days--> '))
days_list = []

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 10) -> [5, 6, 7, 8, 9]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]
'''for i in range(num_days):
    day = int(input('Day--> '))
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

print(max_len)'''

'''# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2


num_days = int(input('Num days--> '))
days_list = []

# range(5) -> [0, 1, 2, 3, 4]
# range(5, 10) -> [5, 6, 7, 8, 9]
# range(1, 11, 2) -> [1, 3, 5, 7, 9]
for i in range(num_days):
    day = int(input(f'Day_{i}--> '))
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

print(max_len)'''


'''max_len = 0
temp_count = 0
num_days = int(input('Num days--> '))
for i in range(num_days):
    temp = int(input(f'Day_{i}--> '))
    if temp > 0:
        temp_count += 1
    else:
        temp_count = 0

    if temp_count > max_len:
        max_len = temp_count

print(max_len)'''



