'''Найдите сумму цифр трехзначного числа. 
123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0)'''

number = int(input("Введите трёхзначное число: "))
if (number < -999) or (-100 < number < 100) or (number > 999):
    print("Вы ввели неверное число! ")
elif number <= -100:
    number *= -1
    print(number//100 + number//10 % 10 + number % 10)
else:
    print(number//100 + number//10 % 10 + number % 10)
