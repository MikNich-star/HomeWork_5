import os
import shutil
import sys
import functions as f

while True:
    print('1.Создать папку')
    print('2.Удалить файл/папку')
    print('3.Копировать файл/папку')
    print('4.Просмотр содержимого рабочей директории')
    print('5.Просмотр папок')
    print('6.Просмотр файлов')
    print('7.Создатель программы')
    print('8.Просмотр информации об операционной системе')
    print('9.Играть в викторину')
    print('10.Мой банковский счет')
    print('11.Смена рабочей директории')
    print('12.Выход')
    choice = input('Выберите пункт меню')
    if choice == '1':
        os.mkdir(input(''))
    elif choice == '2':
        os.rmdir(input(''))
    elif choice == '3':
        shutil.copy(input(''), input(''))
    elif choice == '4':
        input(os.getcwd())
    elif choice == '5':
        input(os.listdir())
    elif choice == '6':
        print(f.show_files())
    elif choice == '7':
        print('PYTNON COMPANY')
    elif choice == '8':
        print(sys.platform)
    elif choice == '9':
        input(f.game())
    elif choice == '10':
        input(f.bill_fun())
    elif choice == '11':
        os.chdir(path=input(''))
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')