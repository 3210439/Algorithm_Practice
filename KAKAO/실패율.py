def solution(N, stages):
    answer = []
    temp = []
    for i in range(1,N+1):
        clear = 0
        fail = 0
        for j in range(len(stages)):
            if stages[j] >= i:
                clear += 1
            if stages[j] == i:
                fail += 1
        if fail > 0 and clear > 0 : 
            temp.append((i,float(fail/clear)))
        else:
            temp.append((i,0))
    print(temp)
    temp.sort(key=lambda x : -x[1])
    for i in range(len(temp)):
        answer.append(temp[i][0])
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N,stages))