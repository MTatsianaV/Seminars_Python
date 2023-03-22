''' Напишите программу, которая принимает на вход строку, 
и отслеживает, сколько раз каждый символ уже встречался. 
Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split() '''
# Решение 1 (через словарь).
my_str = 'a a a b c a a d c d d'
my_str = my_str.split(" ")
print(my_str)
new_str = {}
for i in my_str:
    if i not in new_str:
        new_str[i] = 0
        print(i, end=' ')
    elif i in new_str:
        new_str[i] += 1
        print(f'{i}_{new_str[i]}', end=' ')
print()

# Решение 2 (через список).
my_str = 'a a a b c a a d c d d'
my_str = my_str.split(" ")
print(my_str)
i,n,str = 0, len(my_str), ''
while i<n:
    if my_str[:i].count(my_str[i]) == 0: str += f' {my_str[i]}'
    else: str += f' {my_str[i]}_{my_str[:i].count(my_str[i])}'
    i+=1
print(str)

# Решение 3 (через строку, без функции .split()).
my_str = 'a a a b c a a d c d d'
my_str = my_str.replace(' ','')
print(my_str)
i,n,str = 0, len(my_str), ''
while i<n:
    if my_str[:i].count(my_str[i]) == 0: str += f' {my_str[i]}'
    else: str += f' {my_str[i]}_{my_str[:i].count(my_str[i])}'
    i+=1
print(str)