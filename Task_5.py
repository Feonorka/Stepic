spisok = [int(i) for i in input().split()]
sum = 0
for i in range(len(spisok)):
    if len(spisok) == 1:
        sum = spisok[i]
        print (sum, end=" ")
    elif i - 1 < 0:
        sum = spisok[1] + spisok[-1]
        print (sum, end=" ")
    elif i + 1 == len(spisok):
        sum = spisok[i-1] + spisok[0]
        print (sum, end=" ")
    else:
        sum = spisok[i-1] + spisok[i+1]
        print (sum, end=" ")