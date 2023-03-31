''' Определить индексы элементов массива (списка),
значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
        min = 5, max = 14
Вывод: [1, 9, 13, 14, 19] '''
def element_index(given_array, min_el, max_el):
    list_index = []
    for i in range(len(given_array)):
        if min_el <= given_array[i] <= max_el:
            list_index.append(i)
    return list_index
array_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
min_element = int(input("Введите минимальное значение элемента: "))
max_element = int(input("Введите максимальное значение элемента: "))  
print(element_index(array_1, min_element, max_element))    
