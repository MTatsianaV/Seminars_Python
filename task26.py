''' Напишите программу, которая:
1. на вход принимает два числа A и B, 
2. возводит число А в целую степень B с помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8 '''
def degree_a_to_b(a, b):
    if b == 1: return a
    return degree_a_to_b(a , b - 1) * a
numberA = int(input("Введите A: "))
numberB = int(input("Введите B: "))
print(degree_a_to_b(numberA, numberB))