def min_value(li):
  if li is None:
    return TypeError

  min_val = li[0]
  for i in li:
    if i < min_val:
      min_val = i

  return min_val

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(-50, 50))

# print(min_value(li))