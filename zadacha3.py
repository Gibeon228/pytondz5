from operator import truediv


list1 = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]

print(list1[0], list1[1], list1[2])
print(list1[3], list1[4], list1[5])
print(list1[6], list1[7], list1[8])

f = 0
while (((list1[0] == "_") or (list1[1] == "_") or (list1[2] == "_") or (list1[3] == "_") or (list1[4] == "_") or (list1[5] == "_") or (list1[6] == "_") or (list1[7] == "_") or (list1[8] == "_")) and (not(list1[0]== "X" and list1[1]== "X" and list1[2]== "X")) and (not (list1[0]== "O" and list1[1]== "O" and list1[2]== "O")) and (not(list1[3]== "X" and list1[4]== "X" and list1[5]== "X")) and not((list1[3]== "O" and list1[4]== "O" and list1[5]== "O")) and (not(list1[6]== "X" and list1[7]== "X" and list1[8]== "X")) and (not(list1[6]== "O" and list1[7]== "O" and list1[8]== "O")) and (not(list1[0]== "X" and list1[3]== "X" and list1[6]== "X")) and (not(list1[0]== "O" and list1[3]== "O" and list1[6]== "O")) and (not(list1[1]== "X" and list1[4]== "X" and list1[7]== "X")) and not((list1[1]== "O" and list1[4]== "O" and list1[7]== "O")) and (not(list1[2]== "X" and list1[5]== "X" and list1[8]== "X")) and (not(list1[2]== "O" and list1[5]== "O" and list1[8]== "O")) and (not(list1[0]== "X" and list1[4]== "X" and list1[8]== "X")) and (not(list1[0]== "O" and list1[4]== "O" and list1[8]== "O") and (not(list1[2]== "X" and list1[4]== "X" and list1[6]== "X")) and (not(list1[2]== "O" and list1[4]== "O" and list1[8]== "O")))):
    if (f == 0):
        print("Ходит игрок №1")
        print("Введите число от 0 до 8")
        a = int (input())
        while (((a<0) or (a>8)) or (list1[a] != "_")):
            a = int (input())
        list1[a] = "X"
        print(list1[0], list1[1], list1[2])
        print(list1[3], list1[4], list1[5])
        print(list1[6], list1[7], list1[8])
        if ((list1[0]== "X" and list1[1]== "X" and list1[2]== "X") or (list1[3]== "X" and list1[4]== "X" and list1[5]== "X") or (list1[6]== "X" and list1[7]== "X" and list1[8]== "X") or (list1[0]== "X" and list1[3]== "X" and list1[6]== "X") or (list1[1]== "X" and list1[4]== "X" and list1[7]== "X") or (list1[2]== "X" and list1[5]== "X" and list1[8]== "X") or (list1[0]== "X" and list1[4]== "X" and list1[8]== "X") or (list1[2]== "X" and list1[4]== "X" and list1[6]== "X")):
            print ("Победил игрок №1")
        f = 1
    else:
            print("Ходит игрок №2")
            print("Введите число от 0 до 8")
            b = int (input())
            while (((b<0) or (b>8)) or (list1[b] != "_")):
                b = int (input())
            list1[b] = "O"
            print(list1[0], list1[1], list1[2])
            print(list1[3], list1[4], list1[5])
            print(list1[6], list1[7], list1[8])
            f = 0
            if ((list1[0]== "O" and list1[1]== "O" and list1[2]== "O") or (list1[3]== "O" and list1[4]== "O" and list1[5]== "O") or (list1[6]== "O" and list1[7]== "O" and list1[8]== "O") or (list1[0]== "O" and list1[3]== "O" and list1[6]== "O") or (list1[1]== "O" and list1[4]== "O" and list1[7]== "O") or (list1[2]== "O" and list1[5]== "O" and list1[8]== "O") or (list1[0]== "O" and list1[4]== "O" and list1[8]== "O") or (list1[2]== "O" and list1[4]== "O" and list1[6]== "O")):
                print ("Победил игрок №2")
    if ((list1[0] != "_") and (list1[1] != "_") and (list1[2] != "_") and (list1[3] != "_") and (list1[4] != "_") and (list1[5] != "_") and (list1[6] != "_") and (list1[7] != "_") and (list1[8] != "_")):
        print ("Ничья")


