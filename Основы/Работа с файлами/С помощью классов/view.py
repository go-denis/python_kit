

 #Меню
def menu() -> input:
    print(
        'Главние меню: \n'
        '1) Открыть файл\n'
        '2) Сохранить файл \n'
        '3) Показать контакты \n'
        '4) Добавить контакт \n'
        '5) Найти контакт \n'
        '6) Изменить контакт \n'
        '7) Удалить контакт \n'
        '8) Выход \n')

    while True:
        choice = int(input('Введите номер действия: '))
        if choice.isdigit() and (0 < int(choice) < 9):
         
            return int(choice)

def show_contact(phone_book: list[dict]):
    print()
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20} '
                  f'{contact.get("phone"):<20} '
                  f'{contact.get("comment"):<20}')
        print()
    else:
        print('Телефоная книга не открыта или пуста!')

def new_contact() -> dict:
    print()
  
    name = input('Введите имя и фамилию контакта: ')
    phone = input('Введите телефонконтакта: ')
    comment = input('Введите комментарий контакта: ')
    
    print()
    
    return {'name': name, 'phone': phone, 'comment': comment}


def change_contact(book: list) -> tuple:
        show_contact(book)
        choice = int(input('Выберите контакт, который хотите изменить'))
        name = input('Введите новое имя или Enter, чтобы оставить его без измененеия')
        phone = input('Введите новый телефон или Enter, чтобы оставить его без измененеия')
        comment = input('Введите новый комментария или Enter, чтобы оставить его без измененеия')
        
        return choice - 1, {'name': name if name else book[choice - 1].get('name'),
                            'phone': phone if phone else book[choice - 1].get('phone'),
                            'comment': comment if comment else book[choice - 1].get('comment')
                            }


def select_to_delete(book: list):
     show_contact(book)
     return int(input('Введите номер элемента, который хотите удалить: ')) - 1

def input_request(text: str) -> str:
    request = input(f'Введите {text}: ')

def goodBye():
     print('Пока!!!')


    