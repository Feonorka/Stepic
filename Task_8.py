# не решена
num = int(input())
spisok = []
list = []
for i in range(num):
    spisok.append(i)
    print(spisok)
for i in range(len(spisok)):
    list.append(str(spisok[i]) * i)
print(list)