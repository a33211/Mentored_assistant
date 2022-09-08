from typing import Tuple, Callable, List
from collections import UserDict


class AdressBook(UserDict):
    def add_record(self, string: str) -> str:
        self.data[string[::-1].upper()] = string.lower()

    def delete_record(self, key: str):
        self.data.pop(key)


    def stilyfy(self):
        pass

    def update(self, key, value):
        self.data.update(key, value)






adress_book = AdressBook()

def unknown_command(*args):
    return 'Unknown command'


def add(*args):
    if not args[0]:
        return 'Please add arguments'
    adress_book.add_record(args[0])
    return adress_book


def get_out(*args):
    pass


def delete(*args: str):
    if not args:
        return 'No info found'
    key = args[0][::-1].upper()
    adress_book.delete_record(key)
    return adress_book


def update(*args:str):
    if not args:
        return '11111111No args'
    key = args[0][::-1].upper()
    print(key)
    if not key:
        return 'No key found'
    value = input('please enter new value')
    return key, value


COMMANDS = {add: ['add'],
            delete: ['delete'],
            update: ['update'],
            get_out: ['exit', 'quit']}

def parser(string_command) -> Tuple[Callable, str]:
    for command, value in COMMANDS.items():
        for elem in value:
            if string_command.startswith(elem):
                return command, string_command.replace(elem, '').strip()
    return unknown_command, ''




def main():
    while True:
        user_input = input('>>> \n')
        command, value = parser(user_input)
        if command == get_out:
            break
        print(command(value))


if __name__ == '__main__':
    main()
