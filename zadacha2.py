# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
import random
from random import randint
from re import I

# def play(a,b):

    

print("Выберите с кем играть. 1 - игрок против игрока, 2 - игрок против бота (easy), 3 - игрок против бота (hard)")
n = int(input())
col = 2021
if ((n<1) or (n>3)):
    print ("Ввели некоректные данные")
elif (n==1):
    xod = randint(1, 2)
    if (xod == 1):
        print ("Ходит игрок #1 первым")
        while (col > 0):
            print("Ход игрока #1")
            print (f"На столе осталось, ",col," конфет" )
            number_one_player = int(input())
            while (number_two_player > 28):
                print ("Вы играете не по правилам, введите число от 1 до 28")
                number_two_player = int(input())
            col -= number_one_player
            if (col < 1):
                print("Победил игрок №1")
            else:
                print (f"На столе осталось, ",col," конфет" )
                print ("Ход игрока номер №2")
                number_two_player = int(input())
                while (number_two_player > 28):
                    print ("Вы играете не по правилам, введите число от 1 до 28")
                    number_two_player = int(input())
                col -= number_two_player
                if (col < 1):
                    print ("Победил игрок №2")
    else:
        print ("Ходит игрок №2 первым")
        while (col > 0):
            print("Ход игрока #2")
            print (f"На столе осталось, ",col," конфет" )
            number_two_player = int(input())
            while (number_two_player > 28):
                print ("Вы играете не по правилам, введите число от 1 до 28")
                number_two_player = int(input())
            col -= number_two_player
            if (col < 1):
                print("Победил игрок №2")
            else:
                print (f"На столе осталось, ",col," конфет" )
                print ("Ход игрока номер №1")
                number_one_player = int(input())
                while (number_one_player > 28):
                    print ("Вы играете не по правилам, введите число от 1 до 28")
                    number_one_player = int(input())
                col -= number_one_player
                if (col < 1):
                    print ("Победил игрок №1")
elif (n==2):
    xod = randint(1, 2)
    if (xod == 1):
        print ("Игрок ходит первым")
        while (col > 1):
            print("Сделайте ход")
            print(f"На столе осталось",col," конфет")
            number_player = int(input())
            while (number_player > 28):
                print("Вы играете нечестно, введите число от 1 до 28")
                number_player = int (input())
            col -= number_player
            if (col <1):
                print ("Вы победили")
            else:
                number_bot = randint(1, 28)
                col -= number_bot
                if (col < 1):
                    print ("Вы проиграли")
    else:
        print ("ИИ ходит первым")
        while (col > 0):
            number_bot = randint(1,28)
            col -= number_bot
            if (col < 1):
                print ("Вы проиграли")
            else:
                print("Сделайте ход")
                print(f"На столе осталось",col," конфет")
                number_player = int(input())
                while (number_player > 28):
                    print("Вы играете нечестно, введите число от 1 до 28")
                    number_player = int (input())
                col -= number_player
                if (col <1):
                    print ("Вы победили")
else:
        xod = randint(1, 2)
        if (xod == 1):
            print ("Игрок ходит первым")
            while (col > 1):
                print("Сделайте ход")
                print(f"На столе осталось",col," конфет")
                number_player = int(input())
                while (number_player > 28):
                    print("Вы играете нечестно, введите число от 1 до 28")
                    number_player = int (input())
                col -= number_player
                if (col <1):
                    print ("Вы победили")
                else:
                    number_bot = 1
                    if (col<29):
                        number_bot = col  
                    else:
                        for i in range (28):
                            if ((col-i) % 29 == 0):
                                number_bot = i
                    col -= number_bot
                    if (col < 1):
                        print ("Вы проиграли")
        else:
            print ("ИИ ходит первым")
            while (col > 0):
                if col < 29:
                    number_bot = col
                else:
                    for i in range (28):
                        if ((col-i) % 29 == 0):
                            number_bot = i 
                col -= number_bot
                if (col < 1):
                    print ("Вы проиграли")
                else:
                    print("Сделайте ход")
                    print(f"На столе осталось",col," конфет")
                    number_player = int(input())
                    while (number_player > 28):
                        print("Вы играете нечестно, введите число от 1 до 28")
                        number_player = int (input())
                    col -= number_player
                    print (f"После хода игрока осталось", col," конфет")
                    if (col <1):
                        print ("Вы победили")