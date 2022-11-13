print("Введите значения: ",end='')
spisok = [int(i) for i in input().split()]
sum = 0
for i in range(len(spisok)):
    sum = sum + spisok[i]
print(sum)