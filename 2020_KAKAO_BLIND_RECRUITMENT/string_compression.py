#https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3

def solution(s):
    answer = 0
    strs = []
    strs.append(s)
    
    if len(s) < 2:
        return 1
    half_l = len(s)//2
    for size in range(1,half_l+1):
        count = 0
        word = ""
        remainder = len(s)%size
        share = len(s)//size
        for start in range(0, share*size-size, size):
            f = s[start:size+start]
            b = s[size+start:2*size+start]
            count += 1
            if f != b :
                if count == 1:
                    word += f
                else:
                    word += str(count) + f
                count = 0
                
                if 2*size+start == share*size:
                    word += b
            elif 2*size+start == share*size:
                word += str(count+1) + f
                break
        word += s[share*size:len(s)]
        strs.append(word)
        min = 1000
        for i in range(len(strs)):
            if min > len(strs[i]):
                min = len(strs[i])
    
    return min