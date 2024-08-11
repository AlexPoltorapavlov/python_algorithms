def buble_sorting(li):
  n = 0
  while(n < len(li) - 1):
    for i in range(n + 1, len(li)):
      if li[n] > li[i]:
        li[n], li[i] = li[i], li[n]
    
    n+=1
  return li

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(0, 50))

# print(li)

# print (buble_sorting(li))