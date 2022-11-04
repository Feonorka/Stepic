print("Введите первое число: ", end="")
a = int(input())
print("Введите второе число: ", end="")
b = int(input())

count = 0
num = 0
for i in range(a, b + 1):
    if i % 3 == 0:
        num= num + 1
        count = count + i
res = count / num
print(res)