spisok = []
spisok.append(int(input()))
#sum = 1
i = 0
while sum != 0:
    spisok.append(int(input()))
    
    if i == 0:
        sum = 0
        sum = sum + spisok[i]
        i += 1
    else:
        sum = sum + spisok[i]
        i += 1
    

a = int(input())
i = a
sum = 0
if a == 0:
    sum = a
while i != 0:
    i = int(input())
    sum += i
print(sum + a)