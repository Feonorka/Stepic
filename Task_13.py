#Напишите функцию f(x), которая возвращает значение следующей функции, определённой на всей числовой прямой:

def f(x):
  if x <= -2:
    res = 1 - (x + 2)*(x + 2)
  elif -2 <= x <= 2:
    res = - (x / 2)
  elif 2 < x:
    res = 1 + (x - 2)*(x - 2)
  return res