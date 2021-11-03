def solution(numbers):
    answer = ''
    strs = list()
    
    for i,num in enumerate(numbers):
        if num == 1000:
          strs.append('1.000')
        elif num == 100:
          strs.append('1.00')
        elif num >100:
          strs.append(str(num*0.01))
        elif num >= 10:
          strs.append(str(num*0.1))
        else:
           strs.append(str(num))
    print(strs)
    strs.sort(reverse=True)
    

    for i,str1 in enumerate(strs):
        strs[i] = str1.replace(".","")
    
    print(strs)
    
    answer = ''.join(strs)
    
    return answer


print(solution([3, 30, 34, 5, 9]))