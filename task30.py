''' Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
Формула для получения n-го члена прогрессии: An = A1 + (n-1) * d
Каждое число вводится с новой строки.
Ввод: 7 2 5
Вывод: 7 9 11 13 15 '''
def create_mass(first_el, step_, len_arr):
    new_mass = []
    for i in range(len_arr):
        new_mass.append(first_el + i * step_)
    return new_mass
first_element = int(input("Введите значение первого элемента: "))
step_between_elements = int(input("Введите разницу между элементами: "))
len_array = int(input("Введите количество элементов: "))
print(create_mass(first_element, step_between_elements, len_array))