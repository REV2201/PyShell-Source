#========================================PyShell, Исходный код, Николай Пузанов 2025.===========================================
#==============================================Код находится под лицензией MIT==================================================

#Рекомандуется редактировать код в Notepad++

import os           #Для запуска команд
import sys
import subprocess
import colorama     #Для цветовой палитры
from colorama import Fore, Back, Style   #Импорт зависимостей Colorama


os.system('color 1f')       #Установка цвета. Фон синий, текст белый.

def main():
    while True:  # Используем цикл для постоянного ожидания команд
        try:
            print(Back.WHITE + Fore.BLACK + "PyShell")
            print(Back.WHITE + Fore.BLACK + "Исходный код: " + Fore.BLUE + "github.com/REV2201/PyShell-Source/" + Style.RESET_ALL)
            incom = input(Back.BLUE + Fore.WHITE + os.getcwd() + '> ' + Style.RESET_ALL + Back.BLUE + Fore.YELLOW)   #Поле ввода команды

            if incom == "exit":
                break  # Выходим из цикла, а не завершаем программу сразу
            if incom == "cls":  #Если мы введем команду CLS без этого оператора, то тогда очищаться экран не будет.
                os.system('cls')

            # Используем subprocess для запуска команды
            process = subprocess.Popen(incom, shell=True,
                                     stdout=subprocess.PIPE,
                                     stderr=subprocess.PIPE,
                                     universal_newlines=True)  # Добавлена обработка текста

            # Получаем вывод и ошибки
            stdout, stderr = process.communicate()

            # Выводим результаты
            if stdout:
                print(stdout)
            if stderr:
                print(stderr, file=sys.stderr)  # Выводим ошибки в stderr

        except FileNotFoundError:
            print(f"Команда '{incom}' не найдена.", file=sys.stderr)
        except Exception as e:
            print(f"Произошла ошибка: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()