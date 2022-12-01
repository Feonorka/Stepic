num = int(input('Введите количество чисел: '))
count = 0
lst = list()
while count < num:
    count += 1
    for i in range(count):
        if len(lst) >= num:
            break
        else:
            lst.append(count)
        print(count, end=" ")