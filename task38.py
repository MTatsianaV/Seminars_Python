''' Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, 
и Вы должны реализовать функционал для изменения и удаления данных. '''
def print_info():
    with open(file_phones, 'r', encoding='utf-8') as f:
        count = 1
        for line in f:
            print(f'{count}.{line.strip()}')
            count += 1

def create_mass():
    with open(file_phones, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        table = []
        for line in lines:
            line = line.rstrip("\n")
            row = line.split(" ")
            new_row = [row[0], row[1], row[2], (row[3])]
            table.append(new_row)
    return (table)

def search_row(matrix, search_info):
    with open(file_phones, 'r', encoding='utf-8') as f:        
        count = -1
        for line in f:
            count += 1
            if search_info.casefold() in line.casefold():
                print(line)                          
                return count
        else: print("Таких данных в справочнике нет.")

def delete_line(matrix, row_nums):
    with open(file_phones, 'w+', encoding='utf-8') as f:
        del matrix[row_nums]
        for row in matrix:
            f.write(" ".join(str(element) for element in row))
            f.write("\n")

def add_line():
    with open(file_phones, 'a', encoding='utf-8') as f:
        f.writelines(input("Введите новую строку: "))

def change_info(matrix, row_nums):
    with open(file_phones, 'w+', encoding='utf-8') as f:
        change_column = int(input("Какие данные Вы хотели бы изменить (фамилия - 1, имя - 2, отчество - 3, номер телефона - 4): ")) - 1
        if change_column < 0 or change_column > 3:
                print("Некорректный выбор.")
                exit()
        column_new_info = input("Введите новое значение: ")
        matrix[row_nums][change_column] = column_new_info
        for row in matrix:
            f.write(" ".join(str(element) for element in row))
            f.write("\n")
        
def making_changes():
    print_info()
    table_phones = create_mass()
    view_changes = int(input(
        "Выберите вид изменений (удалить строку - 1, добавить строку - 2, внести изменения - 3): "))
    if (view_changes == 1):
        view_seart = int(input(
        "Как будем искать строку (по номеру строки - 1, по содержимому - 2): "))
        if (view_seart == 1):
            row_num = int(input("Введите номер строки для удаления: ")) - 1
            if (0 <= row_num < len(table_phones)):
                delete_line(table_phones, row_num)
            else: print("Такой строки нет!")
        if (view_seart == 2):
            information_sought = input("Введите информацию для поиска: ")
            row_num = search_row(table_phones, information_sought)
            if (type(row_num) == int):
                delete_line(table_phones, row_num)
            else: exit()        
    if (view_changes == 2): 
        add_line()       
    if (view_changes == 3):
        view_seart = int(input("Выберите тип поиска строки для внесения изменений (по номеру строки - 1, по содержимому - 2): "))
        if (view_seart == 1):
            row_num = int(input("Введите номер строки для внесения изменений: ")) - 1
            change_info(table_phones, row_num)
        if (view_seart == 2):
            information_sought = input("Введите информацию для поиска: ")
            row_num = search_row(table_phones, information_sought)
            print(row_num)
            if (0 <= row_num < len(table_phones)): 
                change_info(table_phones, row_num)
            else: print("Таких данных нет!")        

file_phones = r'files_txt\telephonebook.txt'
making_changes()