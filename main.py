def print_phonebook():
    with open("file.txt", 'r') as file:
        string = file.readlines()
        for i in string:
            print(i)

def add_in_phonebook():
    with open("file.txt", 'a') as file:
        new_contact = ''
        new_contact += input('Введите фамилию') + ', '
        new_contact += input('Введите имя') + ', '
        new_contact += input('Введите номер телефона') 
        file.write(new_contact + "\n")

def change_phonebook():
    with open("file.txt", 'r+') as file:
        phoneBook = {}
        string = file.readlines()
        for i in string:
            name, surname, phone = i.split(', ')
            phone = phone.replace('\n', '')
            phoneBook[phone] = [name, surname]

        find_contact = input("Введите имя или фамилию")
        new_name = input('Введите новое имя')
        new_surname = input('Введите новую фамилию')
        new_phone = input('Введите новый номер телефона')

        keys = [key for key in phoneBook if phoneBook[key][0] ==
                find_contact or phoneBook[key][1] == find_contact]
        phoneBook.pop(keys[0])
        phoneBook[new_phone] = [new_surname, new_name]

        data = ""
        for key in phoneBook:
            _ = phoneBook.get(key)
            data += _[0] + ", " + _[1] + ", " + key + "\n"
            with open("file.txt", 'w') as file:
                file.write("".join(data))

def delete_contact():
    with open("file.txt", 'r+') as file:
        phoneBook = {}
        string = file.readlines()
        for i in string:
            name, surname, phone = i.split(', ')
            phone = phone.replace('\n', '')
            phoneBook[phone] = [name, surname]

        find_contact = input("Введите имя или фамилию")
        keys = [key for key in phoneBook if phoneBook[key][0] ==
                find_contact or phoneBook[key][1] == find_contact]
        phoneBook.pop(keys[0])
        data = ""
        for key in phoneBook:
            _ = phoneBook.get(key)
            data += _[0] + ", " + _[1] + ", " + key + "\n"
            with open("file.txt", 'w') as file:
                file.write("".join(data))  
        
def print_menu_phonebook():
    print("----------------------------------------")
    print(" 1 - Показать телефоную книгу")
    print(" 2 - Добавить контакт")
    print(" 3 - Изменить контакт")
    print(" 4 - Удалить контакт")
    print(" 5 - Закрыть")
    print("----------------------------------------")

def main():
    while True:
        print_menu_phonebook()
        number_menu = int(input('Введите номер действия'))
        if number_menu == 1:
            print_phonebook()
        elif number_menu == 2:
            add_in_phonebook()
        elif number_menu == 3:
            change_phonebook()
        elif number_menu == 4:
            delete_contact()
        elif number_menu == 5:
            return False
        
main()