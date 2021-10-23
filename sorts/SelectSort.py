def SelectSort(data):
  for index in range(len(data)-1):
    lowest = index
    for index2 in range(index+1, len(data)):
      if data[lowest] > data[index2]:
        lowest = index2
    data[lowest], data[index] = data[index], data[lowest]
  return data

import random

data_list = random.sample(range(100),20)
print(data_list)
print(SelectSort(data_list))