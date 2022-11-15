lst = [int(i) for i in input().split()]
num = int(input())
start = 0
end = len(lst)
list = []

if num not in lst:
  print("Отсутствует")
else:
  for i in range(len(lst)):
    if num in lst[start::]:
      ipos = lst.index(num, start, end)
    else:
      break
    if ipos not in list:
      list.append(ipos)
      start = ipos + 1

list.sort()
for k in range(len(list)):
  print(list[k], end=" ")