spisok = [int(i) for i in input().split()]
list = []
spisok.sort()
for i in range(len(spisok)):
    if spisok.count(spisok[i]) > 1:
        list.append(spisok[i])
        if spisok[i] in list:
            print(list[i], end=" ")
