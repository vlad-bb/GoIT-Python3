''' В этой домашней работе мы продолжим развивать нашего виртуального ассистента с CLI интерфейсом.

Наш ассистент уже умеет взаимодействовать с пользователем посредством командной строки,
получая команды и аргументы и выполняя нужные действия.
В этом задании нужно будет поработать над внутренней логикой ассистента, над тем, как хранятся данные,
какие именно данные и что с ними можно сделать.

Применим для этих целей объектно-ориентированное программирование.
Для начала выделим несколько сущностей (моделей) с которыми будем работать.

У пользователя будет адресная книга или книга контактов. Эта книга контактов содержит записи.
Каждая запись содержит некоторый набор полей.

Таким образом мы описали сущности (классы), которые необходимо реализовать.
Далее рассмотрим требования к этим классам и установим их взаимосвязь, правила, по которым они будут взаимодействовать.

Пользователь взаимодействует с книгой контактов, добавляя, удаляя и редактируя записи.
Также пользователь должен иметь возможность искать в книге контактов записи по одному или нескольким критериям (полям).

Про поля также можно сказать, что они могут быть обязательными (имя) и необязательными (телефон или email например).
Также записи могут содержать несколько полей одного типа (несколько телефонов например).
Пользователь должен иметь возможность добавлять/удалять/редактировать поля в любой записи.

В этой домашней работе вы должны реализовать такие классы:

Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей
и хранения обязательного поля Name.
Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
Класс Name, обязательное поле с именем.
Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
 Критерии приёма#
Реализованы все классы из задания.
Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение Record.name.value.
Record хранит объект Name в отдельном атрибуте.
Record хранит список объектов Phone в отдельном атрибуте.
Record реализует методы для добавления/удаления/редактирования объектов Phone.
AddressBook реализует метод add_record, который добавляет Record в self.data. '''


from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone) -> None:
        self.name = name
        self.phone = phone


class AddressBook(UserDict):
    def add_record(self, rec: Record):
        self.data[rec.name.value] = rec


phone_book = AddressBook()


def input_error(func):
    def wrapper(*args):
        try:
            return func(*args)
        except IndexError:
            return 'Give me: command, name and phone.'
        except KeyError:
            return 'Name not found'
        except ValueError:
            return 'Value is not correct'

    return wrapper

@input_error
def exit(*args):
    return "Good bye!"

@input_error
def greeting(*args):
    return "Hello!"


@input_error
def add(*args):
    name = Name(args[0])
    phone = Phone(args[1])
    rec = Record(name, phone)
    phone_book.add_record(rec)
    return f'Contact {args[0]} add successful'

@input_error
def change_phone(*args):
    rec = phone_book[args[0]]
    return f'Contact {args[0]} changed'

@input_error
def show_all(*args):
    return '\n'.join(f'{key}: {value}' for key, value in phone_book.items())

@input_error
def remove(*args):
    for key in phone_book.keys():
        if key is args[0]:
            phone_book.pop(Record)
    return f'Contact {args[0]} was deleted'


COMMANDS = {exit: ["exit", ".", "bye"], add: ["add", "добавь", "додай"], show_all: ["show all", "show"],
            change_phone: ['change', "обнови", "замени"], greeting: ['hello', 'hi'],
            remove: ['remove', 'delete', 'del', 'видалити']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")


def main():
    while True:
        user_input = input(">>> ")
        result, data = parse_command(user_input)
        print(result(*data))
        if result is exit:
            break


if __name__ == "__main__":
    main()
