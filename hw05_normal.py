
__author__ = 'Белинский Андрей Петрович'

# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import hw05_easy as hwfunc


ans = ''
while True:
    ans = input('Для выхода нажмите q\n'
                 '[1] - перейти в другую папку\n'
                 '[2] - просмотреть содержимое текущей папки\n'
                 '[3] - удалить папку\n'
                 '[4] - создать папку\n')

    if ans == '1':
        ans_1 = input('Введите папку для перехода\n')

        try:
            hwfunc.os.chdir(ans_1)
        except FileNotFoundError:
            print('Невозможно перейти\n')
        else:
            print('Успешно перешел\n')
            print(hwfunc.os.getcwd())

    elif ans == '2':
        print(hwfunc.list_dir())
    elif ans == '3':
        ans_3 = input('Введите название папки для удаления\n')

        try:
            hwfunc.remove_dir(ans_3)
        except FileNotFoundError:
            print('Невозможно удалить\n')
        else:
            print('Успешно удалено\n')

    elif ans == '4':
        ans_4 = input('Введите название для новой папки\n')

        try:
            hwfunc.make_dir(ans_4)
        except FileExistsError:
            print('Невозможно создать\n')
        else:
            print('Успешно создано\n')

    elif ans.lower() == 'q':
        sys.exit()
    else:
        print('Неверная команда\n')
