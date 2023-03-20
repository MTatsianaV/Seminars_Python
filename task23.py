''' Дан массив, состоящий из целых чисел. 
Напишите программу, которая подсчитает количество элементов массива, 
больших предыдущего (элемента с предыдущим номером) 
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3) '''
start_list = [0, -1, 5, 2, 3]
count_nums = 0
for i in range(1, len(start_list)):
    if start_list[i] > start_list[i-1]:
        count_nums +=1
print(count_nums)