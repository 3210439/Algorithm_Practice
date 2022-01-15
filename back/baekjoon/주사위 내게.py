# 주사위 네개
#https://www.acmicpc.net/problem/2484

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
                    
                    
                