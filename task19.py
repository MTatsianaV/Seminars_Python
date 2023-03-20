''' Дана последовательность из N целых чисел 
и число K. 
Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
на K элементов вправо, 
K – положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [4, 5, 1, 2, 3] '''
list = [1, 2, 3, 4, 5]
k = 3 % len(list)

# Решение 1.
new_list = (list[k:] + list[:k])
print(new_list)

# Решение 2.
'''while k >0:
    list.append(list.pop(0))
    k-=1
print(list)  '''

# Решение 3.
''' for i in range(k-1):
    num = list.pop(-1)
    list.insert(0, num)
print(list)
 '''