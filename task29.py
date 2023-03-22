''' Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
“Задана последовательность неотрицательных целых чисел. 
Требуется определить значение наибольшего элемента последовательности, 
которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
Однако 2 друга оказались не такими смышлеными. 
Никто из ребят не смог до конца сделать это задание. 
Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
За помощью товарищи обратились к Вам, студентам.
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)
Петя:
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n) '''
# Ваня
''' n = int(input())
max_number = n           # 1-я ошибка
while n != 0:
    if max_number < n:      #2-я ошибка
        max_number = n
    n = int(input())        #3-я ошибка
print(max_number) '''

# Петя
''' n = int(input())
max_number = -1
while n != 0:                # 1-я ошибка      
    
    if max_number < n:
        max_number = n      #2-я ошибка
    n = int(input())        #3-я ошибка
             #3-я ошибка
print(max_number)            #4-я ошибка '''

# Решение через моржовый оператор
max_number = -1
while (n := int(input())) != 0:                      
    if max_number < n:
        max_number = n     
print(max_number) 

# Ответ: больше ошибок у Пети.