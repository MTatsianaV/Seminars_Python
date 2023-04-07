file_phones = r'files_txt\telephonebook.txt'
with open(file_phones, 'w', encoding='utf-8') as f:
    f.writelines('Петров Денис Петрович +375291667533' + '\n' + 'Иванов Иван Иванович +375449852314' + '\n' 
                 + 'Максимов Максим Максимович +375295847235' + '\n' + 'Ковалев Евгений Петрович +375449854314' + '\n')