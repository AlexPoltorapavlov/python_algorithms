def selection_sorting(li):
  for i in range(len(li)):
    min_index = i
    for j in range(i + 1, len(li)):
      if li[min_index] > li [j]:
        min_index = j

    li[min_index], li[i] = li[i], li[min_index]

  return li

# from random import randint

# li = []
# for i in range(100):
#   li.append(randint(0, 50))

# print(li, end="\n\n")

# print (selection_sorting(li))