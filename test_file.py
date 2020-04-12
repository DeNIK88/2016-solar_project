# coding: utf-8

def read_file():
    with open('solar_system — копия.txt') as file:
        lst = list()
        for line in file.readlines():
            if len(line.strip()) == 0 or line[0] == '#':
                continue
            lst.extend(line.strip().split(' '))
            # new_str = name.strip() # Удалит пробелы в начале и символы /n и в конце строки
            # split разрезает строку по пробелам.

        print(lst)

read_file()