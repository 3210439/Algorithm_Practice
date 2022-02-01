def solution(N, number):
    
    if number == N:
        return 1
    
    answer = -1
    # 큰 문제 -> 여러개의 작은 문제들로 쪼개어 접근
    _li = [set() for i in range(8)]
    print(_li)
    
    # _li
    # set() set() set() set() set() set() set() set()
    # 5     55    5-5   5+5   5*5   5//5
    
    # 1 2  3   4    5     6      7       8
    # 5 55 555 5555 55555 555555 5555555 55555555
    for i in range(len(_li)):
        _li[i].add(int(str(N)*(i+1)))
        
    for i in range(1, 8):
        for j in range(i):
            for op1 in _li[j]:
                for op2 in _li[i-j-1]:
                    _li[i].add(op1+op2)
                    _li[i].add(op1-op2)
                    _li[i].add(op1*op2)
                    if op2 != 0:
                        _li[i].add(op1//op2)
        if number in _li[i]:
            answer = i+1
            break
    
    return answer