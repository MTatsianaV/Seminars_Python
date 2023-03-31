''' Дан массив, состоящий из целых чисел. 
Напишите программу, которая в данном массиве определит количество элементов, 
у которых два соседних и, при этом, оба соседних элемента меньше данного. 
Сначала вводится число N — количество элементов в массиве 
Далее записаны N чисел — элементы массива. 
Массив состоит из целых чисел.
Ввод: 5 -> 1 2 3 4 5
Вывод: 0
Ввод: 5 -> 1 5 1 5 1
Вывод: 2
*каждое число вводится с новой строки '''
def create_mass(len_mass):
    new_mass = []
    for i in range(len_mass):
        new_mass.append(int(input(f'Введите значение элемента {i}: ')))
    return new_mass
def seart_count(new_mass):
    count = 0
    for i in (1, len(new_mass_1)-2):    
        if new_mass_1[i+1] < new_mass_1[i] > new_mass_1[i-1]:
            count +=1
    return count
len_mass_1 = int(input("Введите длинну массива: "))
new_mass_1 = create_mass(len_mass_1)
print(new_mass_1)
print(seart_count(new_mass_1))