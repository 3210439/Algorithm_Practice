import random

def bubbleSort(data):
  IsSwap = False
  for index in range(len(data)-1):
    for index2 in range(len(data)-1-index):
      if data[index2] > data[index2+1]:
        data[index2], data[index2+1] = data[index2+1], data[index2]
        IsSwap = True
    if IsSwap == False:
      break
    IsSwap = False
  return data

data_list = random.sample(range(100), 50)
print(data_list)
print(bubbleSort(data_list))
