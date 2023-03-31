''' Даны два массива чисел. 
Требуется вывести те элементы первого массива 
(в том порядке, в каком они идут в первом массиве), 
которых нет во втором массиве. 
Пользователь вводит число N - количество элементов в первом массиве, 
затем N чисел - элементы массива. 
Затем число M - количество элементов во втором массиве. 
Затем элементы второго массива
Ввод (каждое число вводится с новой строки): 
7 -> 3 1 3 4 2 4 12
6 -> 4 15 43 1 15 1 
Вывод: 3 3 2 12 '''

def create_mass(len_mass):
    new_mass = []
    for i in range(len_mass):
        new_mass.append(int(input(f'Введите значение элемента {i}: ')))
    return new_mass
len_mass_1 = int(input("Введите длинну первого массива: "))
new_mass_1 = create_mass(len_mass_1)
len_mass_2 = int(input("Введите длинну второго массива: "))
new_mass_2 = create_mass(len_mass_2)
print(new_mass_1)
print(new_mass_2)
res_mas = []
for item in new_mass_1:
    if item not in new_mass_2:
        res_mas.append(item)
print(res_mas)