''' Напишите функцию same_by(characteristic, objects), 
которая проверяет, все ли объекты имеют одинаковое значение некоторой характеристики, 
и возвращают True, если это так. 
Если значение характеристики для разных объектов 
отличается - то False. 
Для пустого набора объектов, функция должна возвращать True. 
Аргумент characteristic - это функция, которая принимает объект и вычисляет его характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’) '''
def same_by(func, vals):
    return len(set(map(func, vals))) <= 1
''' res_val = []
    for item in vals:
        res_val.append(func(item))
    print(res_val)
    print(set(res_val))
    print(len(set(res_val)))
    if len(set(res_val)) <= 1:
        return True
    return False '''
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')