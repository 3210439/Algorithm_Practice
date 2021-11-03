from itertools import permutations

def solution(numbers):
    numbers = list(map(str,numbers))
    strs = []
    permus = list(permutations(numbers,len(numbers)))

    for permu in permus:
        str1 = ''
        str1 = str1.join(permu)
        strs.append(str1)
            
    return max(strs)

print(solution([6, 10, 2]))