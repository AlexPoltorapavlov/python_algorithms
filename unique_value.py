# Создай функцию, которая из отсортированного списка возвращает только уникальные значения.

def uniq(li):
  uniq_li = [li[0]]

  for i in li:
    if uniq_li[-1] != i:
      uniq_li.append(i)

  return uniq_li

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(0, 50))

# li.sort()

# print(uniq(li))