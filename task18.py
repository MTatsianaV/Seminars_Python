''' Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. 
Последняя строка содержит число X
Например:
5
1 2 3 4 5
6
-> 5 '''
len_mass = int(input("Введите длинну массива: "))
new_mass = []
for i in range(len_mass):
    el_mass = int(input('Введите значения элементов массива: '))
    new_mass.append(el_mass)
compared_number = int(input("Введите число X: "))
min_res = new_mass[0] - compared_number
next_number = new_mass[0]
if min_res < 0: min_res *= -1
for i in range(1, len(new_mass)):
    res = new_mass[i] - compared_number
    if res < 0: res *= -1
    if res < min_res: 
        min_res = res
        next_number = new_mass[i]
print(new_mass) 
print(f'-> {next_number}')   