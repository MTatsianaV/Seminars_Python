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
def change_info():
    what_change = input("Введите информацию для изменения: ")
    with open(file_phones, 'r+', encoding='utf-8') as f: 
        for line in f:
            if what_change.casefold() in line.casefold():
                print(line.replace(what_change, input("Введите новую информацию: ")))         


file_phones = r'files_txt\telephonebook.txt'
change_info()