# 주사위 네개
#https://www.acmicpc.net/problem/2484
# 나의 풀이
def solution(lst):
    lst.sort()
    zusa = [0]*7
    result = 0
    case = 0
    
    if len(set(lst)) == 1:
        result = 50000 + lst[0]*5000
    else:
        for el in lst:
            zusa[el] +=1
        case = max(zusa)
        
        if case == 3:
            for i in range(len(zusa)):
                if zusa[i] == 3:
                    result = 10000 + i*1000
                    break
        elif case == 2:
            if len(set(lst)) == 2:
                result += 2000
                for i in range(len(zusa)):
                    if zusa[i] == 2:
                        result += i*500
            else:
                for i in range(len(zusa)):
                    if zusa[i] == 2:
                        result += 1000 + i*100
                        
        elif case == 1:
            result = lst[-1] * 100
    return result
    
n = int(input())
answer = []
for i in range(n):
    answer.append(solution(list(map(int, input().split()))))
print(max(answer))
                    
# 강의 풀이
def money():
  lst = sorted(list(map(int, input().split())))
  if len(set(lst)) == 1:
    return lst[0] * 5000 + 50000
  if len(set(lst)) == 2:
    if lst[1] == lst[2]:
      return 10000 + lst[1] * 1000
    else:
      return 2000 + (lst[1] + lst[2]) * 500
  for i in range(3):
    if lst[i] == lst[i+1]:        
      return 1000 + lst[i] * 100
  return lst[-1] * 100

N = int(input())

print(max(money() for i in range(N)))