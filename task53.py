''' Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи
(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной '''

def read_file():
    with open(file_phones, 'r', encoding='utf-8') as f:
        for line in f:
            print(line.strip())

def add_line():
    with open(file_phones, 'a', encoding='utf-8') as f:
        f.writelines('\n' + input("Введите новую строку: "))
        
def find_info():
    information_sought = input("Введите информацию для поиска: ")
    with open(file_phones, 'r', encoding='utf-8') as f:        
        for line in f:
            if information_sought.casefold() in line.casefold():
                print(line)
     


file_phones = r'files_txt\telephonebook.txt'
read_file()

''' def main():
    read_file() '''
    



''' if __name__ == '__name__':
    main() '''
''' main() '''

