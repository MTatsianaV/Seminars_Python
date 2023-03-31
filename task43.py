''' Дан список чисел. 
Посчитайте, сколько в нем пар элементов, равных друг другу. 
Считается, что любые два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. 
Вводится список чисел. Все числа списка находятся на разных строках.
Ввод: 
1 2 3 2 3 
Вывод: 2 '''
def create_mass(len_mass):
    new_mass = []
    for i in range(len_mass):
        new_mass.append(int(input(f'Введите значение элемента {i}: ')))
    return new_mass
def seart_count_pairs(new_mass):
    count_pairs = 0
    for i in range(len(new_mass)):
        for j in range(i+1, len(new_mass)):         
                if new_mass[i] == new_mass[j]:
                    count_pairs += 1
    return count_pairs
len_mass_1 = int(input("Введите длинну массива: "))
new_mass_1 = create_mass(len_mass_1)
print(new_mass_1)
print(seart_count_pairs(new_mass_1))