from random import choice

def hoar_sorting(li):
  if len(li) <= 1:
    return li
  else:
    sup = choice(li)
    rigt_li = []
    left_li = []
    medium_li = []

    for i in li:
      if i < sup:
        rigt_li.append(i)
      elif i > sup:
        left_li.append(i)
      else:
        medium_li.append(i)
    
    return hoar_sorting(rigt_li) + medium_li + hoar_sorting(left_li)

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(0, 50))

# print(sorted(li) == hoar_sorting(li))