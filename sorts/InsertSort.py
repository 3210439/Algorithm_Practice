def InsertSort(data):
  for index in range(len(data)-1):
    for index2 in range(index+1,0,-1):
      if data[index2-1] > data[index2]:
        data[index2-1],data[index2] = data[index2],data[index2-1]
      else:
        break
  return data

import random

data_list = random.sample(range(100),50)
print(data_list)
print(InsertSort(data_list))