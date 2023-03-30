''' Хакер Василий получил доступ к классному журналу 
и хочет заменить все свои минимальные оценки на максимальные. 
Напишите программу, которая заменяет оценки Василия, но наоборот: 
все максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1 '''
def substitution_of_grades(list):
    max_grade = max(list)
    min_grade = min(list)
    for i in range(len(list)):
        if list[i] == max_grade:
            list[i] = min_grade
    return list
n = int(input("Введите число: "))
estimates = []
for i in range(n):
    grade = int(input('Введице оценку: '))
    estimates.append(grade)
print(estimates)
print(substitution_of_grades(estimates))
