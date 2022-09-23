# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Пример: aaaffffcc->a3f4c2


str1 = "aaaffffcc"
str2 = "a3f4c2"
str3 = ""
str4 = ""
i=0
sum = 1
count =0
while (i<(len(str1)-1)):
    if (str1 [i] == str1 [i+1]):
        sum+=1
        i+=1
    else:
        str3+=str1[count]
        str3+=str(sum)
        sum = 1
        i+=1
        count = i
else:
        str3+=str1[count]
        str3+=str(sum)
print(str3)


for i in range (0, len(str2), 2):
    count = int(str2[i+1])
    for j in range (count):
        str4+= str2[i]
print (str4)
