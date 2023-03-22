''' В фермерском хозяйстве в Карелии выращивают чернику. 
Она растет на круглой грядке, причем кусты высажены только по окружности. 
У каждого куста есть ровно два соседних. 
Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
выросло различное число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники.
Эта система состоит из управляющего модуля и нескольких собирающих модулей.
Собирающий модуль за один заход, находясь непосредственно перед некоторым
кустом, собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может
собрать за один заход собирающий модуль, находясь перед некоторым кустом
заданной во входном файле грядки.
4 -> 1 2 3 4
9 '''
number_of_bushes = int(input("Введите количество кустов на грядке: "))
bush_yield = []
for i in range(number_of_bushes):
    bush = int(input('Введите урожайность каждого куста: '))
    bush_yield.append(bush)
print(bush_yield)
sum_bush_yield = bush_yield[0] + bush_yield[1] + bush_yield[2]
max_yield = sum_bush_yield
for i in range(1, len(bush_yield)):    
    if i < (len(bush_yield) - 2):
        sum_bush_yield = bush_yield[i] + bush_yield[i+1] + bush_yield[i+2]
    elif i == (len(bush_yield) - 2):
        sum_bush_yield = bush_yield[i] + bush_yield[i+1] + bush_yield[0]
    elif i == (len(bush_yield) - 1):
        sum_bush_yield = bush_yield[i] + bush_yield[0] + bush_yield[1]
    if sum_bush_yield > max_yield: max_yield = sum_bush_yield
print(max_yield)