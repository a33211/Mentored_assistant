from typing import Tuple, Callable, List
from collections import UserDict, UserList


# class AdressBook(UserDict):
#     def add_record(self, values: List[str]) ->str:
#         self.data[values[::-1].upper()] = values
#
#     def delete_record(self, key: str):
#         self.data.pop(key)
#
#     def stylify(self):
#         pass
#
#     def update(self, key, value):
#         self.data.update(key, value)


class Research():
    def __init__(self, res_name, res_date, iter_number):
        self.res_name = res_name
        self.res_date = res_date
        self.iter_number = iter_number

    def __repr__(self):
        return ''.join([f'{k}: {v}' for k, v in self.__dict__.items()])
    #def add_record(self, values: Dict[str]):



class ResearchKeep(UserDict):
    def add_entire_res(self, res: Research):
        self.data[res.res_name] = res

    def delete_entire_res(self, res: Research):
        self.data[res.res_name] = res

    def show_entire_avg(self, key):
        pass

    def show_avg_by_date(self, key):
        pass

research = ResearchKeep()

def unknown_command(*args):
    return 'Unknown command'


def add(*args):
    # if not args[0]:
    #     return 'Please add arguments'
    res_info = {'res_name': None,
                'res_date': None,
                'iter_number': None}

    for key, value in res_info.items():
        if value is None:
            user_input = input(f'Please enter {key}')
            res_info[key] = user_input
        # Enter possible name limitations
    listed_args = res_info.values()
    res = Research(listed_args)
    research.add_entire_res(res)





def get_out(*args):
    pass


def delete(*args: str):
    if not args:
        return 'No info found'
    key = args[0]
    research.delete_record(key)
    return research


def update(*args: str):
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
        user_input = input('>>>')
        command = parser(user_input)
        if command == get_out:
            break


if __name__ == '__main__':
    main()
