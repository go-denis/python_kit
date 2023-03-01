import os.path


class PhoneBook:
    src = "Основы/Работа с файлами/phone_guide.txt"

    def __init__(self,path):
        self.path = path
        self.menu()

    #Меню
    def menu(self):
        print(
        '1) Показать контакты\n'
        '2) Добавить контакт \n'
        '3) Найти контакт \n'
        '4) Изменить контакт \n'
        '5) Удалить контакт \n'
        '6) Выход \n')

        data = int(input('Введите номер действия: '))
        match data:
            case 1:
                print('Открываю справочник...')
                self.open_guide()
            case 2:
                print('Добавить контакт')
                self.add_contacts_in_guaide()
            case 3:
                print('Найти контакт')
                self.search_contact()
            case 4:
                print('Изменить контакт')
                self.replace_contact()
            case 5:
                print('Удалить контакт')
                self.del_contact()
            case 6:
                print('Выход...')
                exit(1)
        #return data


    #Открытие записной книжки
    def open_guide(self):
        if (self.chek() == True):
            with open(self.path, 'r', encoding= 'utf-8') as data:
                file = data.readlines()
                for i in file:
                    print(' '.join(i.split(';')))
        input('Нажмите Enter, чтобы выйти в меню')
        self.menu()

    #Добавляем новый контакт
    def add_contacts_in_guaide(self):
        if (self.chek() == True):
            with open(self.path, 'a', encoding= 'utf-8') as data:
                user_info = input('Введите данные для нового контакта в формате : "`Имя` `Телефон` `рабочий/сотовый`" -  ')
                user_info = ';'.join(user_info.split(' '))
                data.write(user_info +'\n')
        print('Данные записаны!')
        self.menu()

    def search_contact(self):

        if (self.chek() == True):
            search = input('Введите имя человека, чей номер вы желаете найти: ')

            with open(self.path, 'r', encoding= 'utf-8') as data:
                file = data.readlines()
                flag = False
                for i in iter(file):
                    if search in i:
                        print(' '.join(i.split(';')))
                        flag = True
                
                if flag == False:
                    change = int(input('Такой контакт не найден! \n Попробовать снова - 1\n Меню - 2 \n'))
                else:
                    change = int(input('Контакт успешно найден! \n Искать еще - 1\n Меню - 2 \n'))

                if change == 1:
                    self.search_contact()
                else:
                    self.menu()

    def replace_contact(self):
        if (self.chek() == True):

            contact = str(input('Введите имя человека, чей номер вы желаете изменить: '))
            
            flag = False
            with open(self.path, 'r', encoding= 'utf-8') as data:
                lines  = data.readlines()
                
                index = 0
                for i in iter(lines):
                    
                    if contact in i:
                        findContact = ' '.join(i.split(';'))
                        flag = True
                        print('Контакт найден: '+ findContact)

                        replaceContact = input('Введите новые данные для '+findContact+' \n В формате: "`Имя` `Телефон` `рабочий/сотовый`" -  \n')
                        replaceContact = str(';'.join(replaceContact.split(' ')))
                        lines[index] = replaceContact+'\n'
                        
                    index += 1 
                
                if flag == False:
                    change = int(input('Такой контакт не найден! \n Попробовать снова - 1\n Меню - 2 \n'))
                    if change == 1:
                        self.replace_contact()
                    else:
                        self.menu()

                with open(self.path, 'w', encoding= 'utf-8') as data:
                    data.writelines(lines)
                    change = int(input('Контакт изменен! \n Поменят еще один - 1\n Меню - 2 \n'))
                    if change == 1:
                        self.replace_contact()
                    else:
                        self.menu()
        
    def del_contact(self):
        if (self.chek() == True):

            contact = str(input('Введите имя человека, чей номер вы желаете удалить: '))
            
            flag = False
            with open(self.path, 'r', encoding= 'utf-8') as data:
                lines  = data.readlines()
                non_empty_lines = (line for line in lines if not line.isspace())
                index = 0
                for i in lines:
                    print(i)
                    if contact in i:
                        findContact = ' '.join(i.split(';'))
                        flag = True
                        print('Контакт найден: '+ findContact)
                        lines[index] = '\n'

                        
                    index += 1 
                
                if flag == False:
                    change = int(input('Такой контакт не найден! \n Попробовать снова - 1\n Меню - 2 \n'))
                    if change == 1:
                        self.del_contact()
                    else:
                        self.menu()
            #non_empty_lines = (line for line in lines if not line.isspace()) 
            with open(self.path, 'w', encoding= 'utf-8') as data:
                #Удаление нашей строки
                data.writelines(lines)       

            change = int(input('Контакт удален! \n Удалить еще один - 1\n Меню - 2 \n'))
            
            if change == 1:
                self.del_contact()
            else:
                self.menu()
            

    #Создание новой записной книжки и запись в нее инфы
    def create_new_guide(self):
        my_file = open(self.path, "w+", encoding= 'utf-8')
        print('Введите данные для нового контакта в формате - "`Имя` `Телефон` `рабочий/сотовый`": ')
        text = str(input())
        my_file.write(';'.join(text.split(' '))+'\n')
        my_file.close()
        print('Файл создан и изменения внесены !')
        self.menu()

    #Проверка открытия файла
    def chek(self):
        flag = os.path.exists(self.path)
        if (flag == False):
                print('Файла не существует, создать новый введите - 1, если нет, введите - 2')
                change = int(input())

                if (change == 1):
                    self.create_new_guide()
                elif (change == 2):
                    self.menu()

        return flag

