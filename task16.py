'''  Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
 Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
 В последующих строках записаны N целых чисел Ai. 
 Последняя строка содержит число X.
Например: 
5
1 2 3 4 5
3
-> 1 '''
len_mass = int(input("Введите длинну массива: "))
new_mass = []
for i in range(len_mass):
    el_mass = int(input('Введите значения элементов массива: '))
    new_mass.append(el_mass)
desired_number = int(input("Введите искомое число: "))
res = 0
for i in range(len(new_mass)):
    if new_mass[i] == desired_number:
        res +=1
print(new_mass) 
print(f'-> {res}')   