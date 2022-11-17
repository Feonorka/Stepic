def f(x):
    return x * 2

num = int(input())
spisok = [int(i) for i in num(input().split())]
i = 0
spisok = []
while i != num:
    spisok.append(int(input()))

    if i == 0:
        spisok[i] = f(spisok[i])
        i += 1

    elif spisok[i] != spisok[i - 1]: 
        spisok[i] = f(spisok[i])
        i += 1
    
for k in range(len(spisok)):
    print(spisok[k])


# избежать вычислений одинаковых элементов

