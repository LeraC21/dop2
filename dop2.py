import re
#import random
from collections import UserDict
slov_find = open("synonyms.txt", "r+")


def find_word():
    slov_find.seek(0)
    n = 0
    user_word = input(str("Найти слово: "))
    for line in slov_find:
        if user_word in line:
            n = 1

            print(line.strip())

            syn = re.split(r"[-;]", line)
            print(syn[1])
            choice(user_word, line)
    if n == 0:
        print("Cлово не найдено...")
        main_program(user_word)


def choice(user_word, line):
    add_choice = input("Нравится синоним?:  ")
    if add_choice == 'нет' or add_choice == 'no':
        print("сейчас добавим")
        return AddSynonims(user_word, line)
    else:
        return main_program(user_word)


def AddSynonims(user_word, line):
    x = input("Введите слово: ")
    newwords = line.replace('\n','').title() + " - " + x.title() + "\n"
    slov_find.write(newwords)
    #slov_find как строку удалить???
    print("синоним добавлен")
    return


def main_program(user_word):
    while True:
        if user_word == "stop":
            exit(0)
        else:
            find_word()
main_program("")

4
