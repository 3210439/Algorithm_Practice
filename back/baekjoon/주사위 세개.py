#https://www.acmicpc.net/problem/2480

# first
lst = list(map(int, input().split()))
result= 0
zusa = [0]*(7)

def findBest(lst):
    for el in lst:
        zusa[el] += 1
        if zusa[el] == 2:
            return el
    return -1
    

if len(set(lst)) == 1:
    result = 10000 + lst[0]*1000
elif len(set(lst)) == 2:
    sameNon = findBest(lst)
    result = 1000 + sameNon*100
else:
    result = max(lst) * 100
    
print(result)

# second
lst = sorted(list(map(int, input().split())))

if len(set(lst)) == 1:
  print(10000 + lst[0] * 1000)
elif len(set(lst)) == 2:
  print(10000 + lst[1] * 100)
else:
  print(lst[2] * 100)