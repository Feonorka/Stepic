def f(x):
    return x * 2

num = int(input())
i = 0
spisok = []
num_list = []
while i != num:
    spisok.append(int(input()))
    i += 1

for k in range(len(spisok)):

    if k == 0:
        num_list.append(int(f(spisok[k])))
        print(num_list[k])
        k += 1
    elif spisok[k] == spisok[k - 1]:
        num_list.append(int(num_list[k - 1]))
        print(num_list[k])
        k += 1
    else:
        num_list.append(int(f(spisok[k])))
        print(num_list[k])
        k += 1
