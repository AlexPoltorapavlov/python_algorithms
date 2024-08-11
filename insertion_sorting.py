def insertion_sorting(li):
  sorted_li = [li[0]]
  for i in range(len(li)-1):
    if sorted_li[-1] <= li[i]:
      sorted_li.append(li[i])
    else:
      j = len(sorted_li) - 1
      while(sorted_li[j] > li[i] and j>=0):
        j-=1

      sorted_li.insert(j+1, li[i])

  return sorted_li

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(0, 50))

# print(li, end="\n\n")

# print (insertion_sorting(li))