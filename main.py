import pathlib
import os

#skip func
def skip():
    print(' ')
    print(' ')
    print(' ')

#show files
def show_files():
    currentDirectory = pathlib.Path('.')
    for currentFile in currentDirectory.iterdir():
        print(currentFile)

    skip()
    menu()

#open file
def open_file():
    name = input('Введите имя файла: ')
    menu_file(name)

#create file
def create_file():
    name = input('Введите название файла: ')
    file = open(name, 'tw', encoding = 'utf-8')
    file.close()
    print('Файл успешно создан!\n')
    skip()
    menu()

#exit
def end_programm():
    clear()

#read new file
def read_new_file(name):
    file = open(name, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end=' ')
        i += 1

    file.close()

#read file
def read_file(name):
    file = open(name, 'r', encoding='utf-8')
    i = 1
    for line in file:
        print(i, ' ', line, end=' ')
        i += 1

    file.close()
    menu_file(name)

#rewrite file
def rewrite_file(name):
    print('Введите текст. Enter -> переход на новую строку. Ctrl+C -> сохранить файл')
    text = []
    while True:
        try:
            line = input()
        except KeyboardInterrupt:
            break
        text.append(line)

    file = open(name, 'w', encoding='utf-8')
    for line in text:
        file.write(line + '\n')
    file.close()
    clear()
    print('Файл успешно записан! Содержимое файла ', name)
    read_new_file(name)

#clear console
def clear():
    os.system('clear')

#menu file
def menu_file(name):
    print('Выберите действие:\n1.Чтение\n2.Перезапись\n3.Закрыть файл')
    answer = input('-->')
    if answer == '1':
        clear()
        read_file(name)
    elif answer == '2':
        clear()
        rewrite_file(name)
    elif answer == '3':
        clear()
        close_file(name)
    else:
        menu()

#programm menu
def menu():
    print('1.Показать содержимое.\n2.Открыть файл.\n3.Создать файл.\n4.Завершить программу')
    answer = input('-->')
    if answer == '1':
        clear()
        show_files()
    elif answer == '2':
        clear()
        open_file()
    elif answer == '3':
        clear()
        create_file()
    elif answer == '4':
        clear()
        end_programm()
    else:
        clear()
        print('Неизвестная команда')
menu()
