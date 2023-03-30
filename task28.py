''' Напишите рекурсивную функцию sum(a, b),
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1.
Также нельзя использовать циклы.
2 2 -> 4 '''
def sum_a_and_b(a, b):
        if b == 0 and a == 0: return 0
        if b == 0 and a != 0: return sum_a_and_b(a-1 , b) + 1
        if a == 0 and b != 0: return sum_a_and_b(a, b-1) + 1
        return sum_a_and_b(a-1 , b - 1) + 1 + 1
numberA = int(input("Введите A: "))
numberB = int(input("Введите B: "))
print(sum_a_and_b(numberA, numberB))