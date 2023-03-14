'''По данному целому неотрицательному n 
вычислите значение n!. N! = 1 * 2 * 3 * … * N 
(произведение всех чисел от 1 до N) 0! = 1 
Решить задачу используя цикл while
Input: 5
Output: 120'''
number = int(input("Введите значение числа N: "))
if number < 0:
    print("Вы ввели отрицательное число!")
elif number == 0:
    print(f"Факториал числа {number} равен 1")
else:
    i = 1
    res = 1
    while i <= number:
        res = i*res
        i += 1
    print(f"Факториал числа {number} равен {res}")