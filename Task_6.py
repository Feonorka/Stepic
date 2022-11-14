print("Введите строку: ", end=' ')
spisok = [int(i) for i in input().split()]
list = []
spisok.sort()
for i in range(len(spisok)):
    if spisok.count(spisok[i]) > 1:
        if spisok[i] not in list:
            list.append(spisok[i])
for k in range(len(list)):
    print(list[k], end=" ")

n = 5
list = [[0] * n for i in range(n)]
print(list)
list = [[0 for j in range(n)] for i in range(n)] 
print(list)